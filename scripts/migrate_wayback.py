#!/usr/bin/env python3
from __future__ import annotations

import re
import time
import pathlib
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from dateutil import parser as dateparser

ROOT = pathlib.Path(__file__).resolve().parents[1]
URLS_TXT = ROOT / "scripts" / "urls.txt"
OUT_DIR = ROOT / "src" / "content" / "blog"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "watarutaru-migrator/1.0"})

WAYBACK_RE = re.compile(r"^https?://web\.archive\.org/web/(\d{14})/(https?://.+)$")


@dataclass
class Parsed:
    wayback_url: str
    original_url: str
    archived_at: str  # YYYYMMDDhhmmss
    slug: str
    title: str
    date_iso: str
    body_md: str
    description: str


def normalize_slug(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"[^a-z0-9\-_]", "", s)
    s = s.strip("-_")
    return s or "post"


def extract_slug_from_original(original_url: str) -> str:
    path = re.sub(r"https?://[^/]+", "", original_url).strip("/")
    if not path:
        return "index"
    return normalize_slug(path.split("/")[-1])


def parse_wayback(url: str) -> tuple[str, str, str]:
    m = WAYBACK_RE.match(url.strip())
    if not m:
        raise ValueError(f"Not a Wayback URL: {url}")
    archived_at = m.group(1)
    original_url = m.group(2)
    return archived_at, original_url, url.strip()


def pick_main(soup: BeautifulSoup):
    selectors = ["article", ".entry-content", ".post-content", ".post", "main", "#content"]
    for sel in selectors:
        el = soup.select_one(sel)
        if el and len(el.get_text(strip=True)) > 200:
            return el
    return soup.body or soup


def extract_title(soup: BeautifulSoup, fallback: str) -> str:
    og = soup.select_one('meta[property="og:title"]')
    if og and og.get("content"):
        t = og["content"].strip()
        if t:
            return t

    h1 = soup.find("h1")
    if h1:
        t = h1.get_text(" ", strip=True)
        if t:
            return t

    if soup.title and soup.title.string:
        t = soup.title.string.strip()
        if t:
            return t

    return fallback


def extract_date(soup: BeautifulSoup, archived_at: str) -> str:
    time_el = soup.find("time")
    if time_el and time_el.get("datetime"):
        try:
            return dateparser.parse(time_el["datetime"]).isoformat()
        except Exception:
            pass

    meta = soup.select_one(
        'meta[property="article:published_time"], meta[name="date"], meta[name="pubdate"]'
    )
    if meta and meta.get("content"):
        try:
            return dateparser.parse(meta["content"]).isoformat()
        except Exception:
            pass

    # 取れなければWaybackのタイムスタンプを採用
    return dateparser.parse(archived_at).isoformat()


def extract_description(soup: BeautifulSoup) -> str:
    meta = soup.select_one('meta[name="description"], meta[property="og:description"]')
    if meta and meta.get("content"):
        return meta["content"].strip()
    return ""


def to_markdown(main_el) -> str:
    for tag in main_el.select("script, style, nav, header, footer, aside"):
        tag.decompose()
    html = str(main_el)
    md_text = md(html, heading_style="ATX")
    md_text = re.sub(r"\n{3,}", "\n\n", md_text).strip() + "\n"
    return md_text


def escape_yaml(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def write_markdown(p: Parsed) -> pathlib.Path:
    out_path = OUT_DIR / f"{p.slug}.md"
    if out_path.exists():
        i = 2
        while (OUT_DIR / f"{p.slug}-{i}.md").exists():
            i += 1
        out_path = OUT_DIR / f"{p.slug}-{i}.md"

    fm_lines = [
        "---",
        f'title: "{escape_yaml(p.title)}"',
        f"slug: {p.slug}",
        f"date: {p.date_iso}",
        "category: blog",
        "tags: []",
        f'description: "{escape_yaml(p.description)}"' if p.description else 'description: ""',
        f'originalUrl: "{escape_yaml(p.original_url)}"',
        f'sourceUrl: "{escape_yaml(p.wayback_url)}"',
        f"archivedAt: {p.archived_at}",
        "---",
        "",
    ]
    out_path.write_text("\n".join(fm_lines) + p.body_md, encoding="utf-8")
    return out_path


def run():
    if not URLS_TXT.exists():
        raise FileNotFoundError(f"Missing: {URLS_TXT}")

    urls = [
        line.strip()
        for line in URLS_TXT.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]
    print(f"Input URLs: {len(urls)}")

    ok = 0
    ng = 0
    for idx, u in enumerate(urls, start=1):
        try:
            archived_at, original_url, wayback_url = parse_wayback(u)
            slug = extract_slug_from_original(original_url)

            print(f"[{idx}/{len(urls)}] {slug}")
            r = SESSION.get(wayback_url, timeout=30)
            r.raise_for_status()

            soup = BeautifulSoup(r.text, "html.parser")
            main_el = pick_main(soup)

            title = extract_title(soup, fallback=slug)
            date_iso = extract_date(soup, archived_at)
            desc = extract_description(soup)
            body_md = to_markdown(main_el)

            out = write_markdown(
                Parsed(
                    wayback_url=wayback_url,
                    original_url=original_url,
                    archived_at=archived_at,
                    slug=slug,
                    title=title,
                    date_iso=date_iso,
                    body_md=body_md,
                    description=desc,
                )
            )
            print(f"  -> wrote {out.relative_to(ROOT)}")
            ok += 1
            time.sleep(1.0)  # Waybackに優しく
        except Exception as e:
            ng += 1
            print(f"  !! failed: {u}\n     {e}")

    print(f"\nDone. OK={ok} NG={ng}")


if __name__ == "__main__":
    run()

#!/usr/bin/env python3
"""
Image download script
Downloads images from Web Archive and saves them to public/images/
"""

import os
import re
import time
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

def extract_image_urls(blog_dir):
    """Extract all image URLs from blog markdown files"""
    urls = set()

    for md_file in Path(blog_dir).glob('*.md'):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all image URLs
        matches = re.findall(r'!\[.*?\]\((https://web\.archive\.org[^\)]+)\)', content)
        urls.update(matches)

    return sorted(urls)

def get_local_path(archive_url):
    """Convert Web Archive URL to local path

    From: https://web.archive.org/web/20220526034218im_/http://watarutaru.com/wp/wp-content/uploads/2016/07/irohanomu_top.jpg
    To: /images/2016/07/irohanomu_top.jpg
    """
    # Extract the original path
    match = re.search(r'uploads/(.+)$', archive_url)
    if match:
        return f"/images/{match.group(1)}"
    return None

def download_image(url, local_path, retries=3):
    """Download image from URL and save to local path"""

    local_file = Path(f"/Users/wataru.saito/Desktop/watarutaru-site/public{local_path}")

    # Create directory if it doesn't exist
    local_file.parent.mkdir(parents=True, exist_ok=True)

    # Skip if already exists
    if local_file.exists():
        print(f"  ⏭️  Already exists: {local_path}")
        return True

    # Download with retries
    for attempt in range(retries):
        try:
            print(f"  📥 Downloading: {local_path}... ", end='', flush=True)

            # Add user agent to avoid blocking
            req = urllib.request.Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0'}
            )

            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()

            with open(local_file, 'wb') as f:
                f.write(data)

            print(f"✅ ({len(data):,} bytes)")

            # Be nice to Web Archive
            time.sleep(0.5)
            return True

        except Exception as e:
            if attempt < retries - 1:
                print(f"⚠️  Retry {attempt + 1}/{retries}")
                time.sleep(2)
            else:
                print(f"❌ Failed: {e}")
                return False

    return False

def main():
    blog_dir = '/Users/wataru.saito/Desktop/watarutaru-site/src/content/blog_backup'

    print("🔍 Extracting image URLs from blog posts...\n")
    urls = extract_image_urls(blog_dir)

    print(f"Found {len(urls)} unique images\n")

    success_count = 0
    skip_count = 0
    fail_count = 0

    for i, url in enumerate(urls, 1):
        local_path = get_local_path(url)

        if not local_path:
            print(f"[{i}/{len(urls)}] ⚠️  Could not parse URL: {url}")
            fail_count += 1
            continue

        print(f"[{i}/{len(urls)}]")

        local_file = Path(f"/Users/wataru.saito/Desktop/watarutaru-site/public{local_path}")
        if local_file.exists():
            skip_count += 1
        elif download_image(url, local_path):
            success_count += 1
        else:
            fail_count += 1

    print(f"\n✨ Done!")
    print(f"   Downloaded: {success_count} images")
    print(f"   Skipped: {skip_count} images (already existed)")
    print(f"   Failed: {fail_count} images")

if __name__ == '__main__':
    main()

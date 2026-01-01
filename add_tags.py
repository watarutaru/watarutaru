#!/usr/bin/env python3
"""
Add appropriate tags to blog posts based on their content
"""

import re
from pathlib import Path

# Define tags for each post based on content analysis
TAGS_MAP = {
    "170323_essay.md": ["合唱", "エッセイ", "音楽"],
    "20150915.md": ["合唱", "はらわた", "演奏"],
    "blog.md": ["お知らせ", "近況"],
    "bunfree-guide06.md": ["合唱", "文藝春秋", "出版"],
    "bunfree-guide07.md": ["合唱", "文藝春秋", "出版"],
    "concert170401.md": ["合唱", "演奏会", "お知らせ"],
    "daijinakoto-a-capella.md": ["合唱", "はらわた", "演奏", "編曲"],
    "daijinakoto.md": ["合唱", "作曲", "はらわた"],
    "drama-omoko.md": ["演劇", "制作"],
    "g-revenge2014.md": ["合唱", "イベント", "東葛"],
    "g-revenge2015-01.md": ["合唱", "イベント", "東葛"],
    "go-go-hawaii.md": ["旅行", "ハワイ"],
    "groove-web.md": ["Webサイト", "制作"],
    "harawata.md": ["合唱", "はらわた", "演奏"],
    "hello-watarutaru-com.md": ["お知らせ", "Webサイト"],
    "imawatamaru-vol6.md": ["ラジオ", "今わたまるラジオ"],
    "imawatamaru07.md": ["ラジオ", "今わたまるラジオ"],
    "imawatamaru6.md": ["ラジオ", "今わたまるラジオ"],
    "irohanomu.md": ["合唱", "演奏会", "お知らせ"],
    "ln-waseda-center-exam.md": ["ライトノベル", "受験", "早稲田"],
    "movie-dogeza-yukachan.md": ["動画", "制作"],
    "mukashiha-yokatta.md": ["合唱", "エッセイ"],
    "nibammenoippo.md": ["合唱", "作曲", "エッセイ"],
    "oni10soku-1.md": ["音楽", "制作", "ネタ"],
    "revenge-chu.md": ["合唱", "イベント", "東葛"],
    "see-you-again-2015.md": ["合唱", "演奏", "はらわた"],
    "tenkyoki.md": ["エッセイ", "転職"],
    "テスト.md": ["test"],
}

def update_tags(file_path: Path, tags: list):
    """Update tags in a markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split frontmatter and body
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            body = parts[2]

            # Replace tags line
            tags_str = ', '.join(f'"{tag}"' for tag in tags)
            new_frontmatter = re.sub(
                r'^tags: \[.*\]',
                f'tags: [{tags_str}]',
                frontmatter,
                flags=re.MULTILINE
            )

            # Write back
            new_content = f"---{new_frontmatter}---{body}"
            with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
                f.write(new_content)

            print(f"✅ {file_path.name}: {tags}")
            return True
        else:
            print(f"⚠️  {file_path.name}: No frontmatter found")
            return False

    except Exception as e:
        print(f"❌ {file_path.name}: Error - {e}")
        return False

def main():
    blog_dir = Path('/Users/wataru.saito/Desktop/watarutaru-site/src/content/blog')

    print("Adding tags to blog posts...\n")

    updated_count = 0
    for filename, tags in TAGS_MAP.items():
        file_path = blog_dir / filename
        if file_path.exists():
            if update_tags(file_path, tags):
                updated_count += 1
        else:
            print(f"⚠️  {filename}: File not found")

    print(f"\n✨ Done! Updated {updated_count} files")

if __name__ == '__main__':
    main()

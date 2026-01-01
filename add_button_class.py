#!/usr/bin/env python3
"""
Add button class to certain links in markdown files
"""

import re
from pathlib import Path

def should_be_button(link_text):
    """Check if a link should be converted to a button"""
    # 全てのリンクをボタンに変換
    return True

def convert_links_to_buttons(content):
    """Convert markdown links to HTML links with button class"""

    # Pattern to match markdown links: [text](url) - but NOT images ![text](url)
    # Negative lookbehind to exclude images
    pattern = r'(?<!!)\[([^\]]+)\]\(([^\)]+)\)'

    def replace_func(match):
        text = match.group(1)
        url = match.group(2)

        if should_be_button(text):
            return f'<a href="{url}" class="button">{text}</a>'
        else:
            return match.group(0)  # Keep original

    return re.sub(pattern, replace_func, content)

def process_file(file_path):
    """Process a single markdown file"""
    print(f"Processing: {file_path.name}... ", end='', flush=True)

    try:
        with open(file_path, 'r', encoding='utf-8', errors='strict') as f:
            content = f.read()

        original_content = content

        # Split frontmatter and body
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            body = parts[2]

            # Convert links in body only
            new_body = convert_links_to_buttons(body)

            if new_body != body:
                new_content = f"---{frontmatter}---{new_body}"

                with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
                    f.write(new_content)
                print("✅ Updated")
                return True
            else:
                print("⏭️  No changes needed")
                return False
        else:
            print("⚠️  No frontmatter found")
            return False

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    blog_dir = Path('/Users/wataru.saito/Desktop/watarutaru-site/src/content/blog')
    md_files = sorted(blog_dir.glob('*.md'))

    print(f"Found {len(md_files)} markdown files\n")

    updated_count = 0

    for md_file in md_files:
        if process_file(md_file):
            updated_count += 1

    print(f"\n✨ Done!")
    print(f"   Updated: {updated_count} files")
    print(f"   Skipped: {len(md_files) - updated_count} files")

if __name__ == '__main__':
    main()

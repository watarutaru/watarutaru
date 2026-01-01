#!/usr/bin/env python3
"""
Fix images that were converted to buttons
"""

import re
from pathlib import Path

def fix_images(content):
    """Convert <a> buttons back to markdown images"""

    # Pattern 1: !<a href="url" class="button">alt</a>
    pattern1 = r'!<a href="([^"]+)" class="button">([^<]+)</a>'
    content = re.sub(pattern1, lambda m: f'![{m.group(2)}]({m.group(1)})', content)

    # Pattern 2: <a href="image" class="button">![alt</a>](link)
    # This is a broken clickable image
    pattern2 = r'<a href="([^"]+)" class="button">!\[([^\]]+)</a>\]\(([^\)]+)\)'
    content = re.sub(pattern2, lambda m: f'[![{m.group(2)}]({m.group(1)})]({m.group(3)})', content)

    return content

def process_file(file_path):
    """Process a single markdown file"""
    print(f"Processing: {file_path.name}... ", end='', flush=True)

    try:
        with open(file_path, 'r', encoding='utf-8', errors='strict') as f:
            content = f.read()

        new_content = fix_images(content)

        if new_content != content:
            with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
                f.write(new_content)
            print("✅ Fixed")
            return True
        else:
            print("⏭️  No changes needed")
            return False

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    blog_dir = Path('/Users/wataru.saito/Desktop/watarutaru-site/src/content/blog')
    md_files = sorted(blog_dir.glob('*.md'))

    print(f"Found {len(md_files)} markdown files\n")

    fixed_count = 0

    for md_file in md_files:
        if process_file(md_file):
            fixed_count += 1

    print(f"\n✨ Done!")
    print(f"   Fixed: {fixed_count} files")

if __name__ == '__main__':
    main()

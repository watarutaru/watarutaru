#!/usr/bin/env python3
"""
Blog post cleanup script
Removes Web Archive artifacts and unnecessary content from markdown files
"""

import os
import re
from pathlib import Path

def clean_post(file_path):
    """Clean a single blog post file"""
    # Read with explicit UTF-8 encoding and error handling
    with open(file_path, 'r', encoding='utf-8', errors='strict') as f:
        content = f.read()

    # Split frontmatter and body
    parts = content.split('---', 2)
    if len(parts) < 3:
        print(f"⚠️  Skipping {file_path.name}: Invalid frontmatter")
        return False

    frontmatter = parts[1]
    body = parts[2]

    # Find the first ## heading (article title)
    lines = body.split('\n')
    start_index = None

    for i, line in enumerate(lines):
        if line.strip().startswith('## '):
            start_index = i
            break

    if start_index is None:
        print(f"⚠️  Skipping {file_path.name}: No ## heading found")
        return False

    # Find where to stop (SNS buttons, footer, etc.)
    end_markers = [
        '[ページの一番上に戻る]',
        '関連してそうな記事',
        '[Facebook]',
        '© 20',
        '[古い→]'
    ]

    end_index = len(lines)
    for i in range(start_index, len(lines)):
        line = lines[i].strip()
        if any(marker in line for marker in end_markers):
            end_index = i
            break

    # Extract clean body (skip the ## heading line itself)
    clean_body_lines = lines[start_index+1:end_index]

    # Remove trailing empty lines
    while clean_body_lines and not clean_body_lines[-1].strip():
        clean_body_lines.pop()

    clean_body = '\n'.join(clean_body_lines)

    # Fix Web Archive image URLs
    # From: https://web.archive.org/web/20220526034218im_/http://watarutaru.com/wp/wp-content/uploads/...
    # To: /images/...
    clean_body = re.sub(
        r'https://web\.archive\.org/web/\d+im_/http://watarutaru\.com/wp/wp-content/uploads/',
        '/images/',
        clean_body
    )

    # Fix other Web Archive URLs
    clean_body = re.sub(
        r'https://web\.archive\.org/web/\d+/http://watarutaru\.com/',
        '/',
        clean_body
    )
    clean_body = re.sub(
        r'/web/\d+/http://watarutaru\.com/',
        '/',
        clean_body
    )

    # Reconstruct the file
    new_content = f"---{frontmatter}---\n\n{clean_body}\n"

    # Write back with explicit UTF-8 encoding and newline handling
    with open(file_path, 'w', encoding='utf-8', newline='\n', errors='strict') as f:
        f.write(new_content)

    return True

def main():
    blog_dir = Path('/Users/wataru.saito/Desktop/watarutaru-site/src/content/blog')

    if not blog_dir.exists():
        print(f"❌ Blog directory not found: {blog_dir}")
        return

    md_files = list(blog_dir.glob('*.md'))
    print(f"Found {len(md_files)} markdown files\n")

    success_count = 0
    skip_count = 0

    for file_path in md_files:
        print(f"Processing: {file_path.name}... ", end='')
        if clean_post(file_path):
            print("✅")
            success_count += 1
        else:
            skip_count += 1

    print(f"\n✨ Done!")
    print(f"   Cleaned: {success_count} files")
    print(f"   Skipped: {skip_count} files")

if __name__ == '__main__':
    main()

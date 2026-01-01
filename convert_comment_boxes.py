#!/usr/bin/env python3
"""
Convert h5 + p patterns to comment-box divs
"""

import re
from pathlib import Path

def convert_comment_boxes(content):
    """Convert h5 headers followed by paragraphs to comment-box divs"""

    # Pattern: ##### heading\n\nparagraph(s)
    # We need to capture h5 and all following paragraphs until next heading or empty line
    lines = content.split('\n')
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if this is an h5 heading
        if line.startswith('#####'):
            h5_text = line[5:].strip()
            i += 1

            # Skip empty lines after h5
            while i < len(lines) and lines[i].strip() == '':
                i += 1

            # Collect paragraph content until next heading or double empty line
            paragraphs = []
            while i < len(lines):
                current = lines[i]

                # Stop at next heading
                if current.startswith('#'):
                    break

                # Stop at HTML tags (like <a>, <div>)
                if current.strip().startswith('<') and not current.strip().startswith('<!--'):
                    break

                # Add non-empty lines
                if current.strip():
                    paragraphs.append(current)
                    i += 1
                else:
                    # Check if next line is also empty (double empty line = end of section)
                    if i + 1 < len(lines) and lines[i + 1].strip() == '':
                        i += 1  # Skip this empty line
                        break
                    else:
                        # Single empty line within paragraph - include it
                        paragraphs.append(current)
                        i += 1

            # Create comment-box div
            if paragraphs:
                result.append('<div class="comment-box">')
                result.append(f'<h5>{h5_text}</h5>')
                result.append('')
                result.extend(paragraphs)
                result.append('</div>')
                result.append('')
            else:
                # h5 without content - keep as is
                result.append(line)

        else:
            result.append(line)
            i += 1

    return '\n'.join(result)

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

            # Convert comment boxes in body only
            new_body = convert_comment_boxes(body)

            if new_body != body:
                new_content = f"---{frontmatter}---{new_body}"

                with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
                    f.write(new_content)
                print("✅ Converted")
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

    converted_count = 0

    for md_file in md_files:
        if process_file(md_file):
            converted_count += 1

    print(f"\n✨ Done!")
    print(f"   Converted: {converted_count} files")

if __name__ == '__main__':
    main()

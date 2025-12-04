#!/usr/bin/env python3
"""
Convert HTML in Markdown files to proper Markdown

This script processes markdown files that contain excessive HTML and converts
them to clean markdown format.
"""

import re
from pathlib import Path
import sys


def convert_html_to_markdown(content: str) -> str:
    """Convert HTML elements to markdown equivalents."""

    # Remove wrapper divs
    content = re.sub(r'<div[^>]*>', '', content)
    content = re.sub(r'</div>', '', content)

    # Convert h2 headers
    content = re.sub(
        r'<h2[^>]*>(.*?)</h2>',
        r'## \1',
        content,
        flags=re.DOTALL
    )

    # Convert h3 headers
    content = re.sub(
        r'<h3[^>]*>(.*?)</h3>',
        r'### \1',
        content,
        flags=re.DOTALL
    )

    # Convert strong wrapped paragraphs to headers (H2)
    # Pattern: <p ...><strong>Text</strong>:</p> -> ## Text
    content = re.sub(
        r'<p[^>]*><strong>(.*?)</strong>:?\s*</p>',
        r'## \1',
        content
    )

    # Convert strong text (bold)
    content = re.sub(r'<strong>(.*?)</strong>', r'**\1**', content)

    # Convert em text (italic)
    content = re.sub(r'<em>(.*?)</em>', r'*\1*', content)

    # Convert br tags
    content = re.sub(r'<br\s*/?>', '\n', content)

    # Convert simple paragraphs
    content = re.sub(
        r'<p[^>]*>(.*?)</p>',
        r'\1\n',
        content,
        flags=re.DOTALL
    )

    # Convert unordered lists
    # First, mark list boundaries
    content = re.sub(r'<ul[^>]*>', '\n__UL_START__\n', content)
    content = re.sub(r'</ul>', '\n__UL_END__\n', content)

    # Convert list items to markdown
    # Handle nested lists by preserving structure
    lines = content.split('\n')
    result_lines = []
    ul_depth = 0

    for line in lines:
        if '__UL_START__' in line:
            ul_depth += 1
            continue
        elif '__UL_END__' in line:
            ul_depth -= 1
            continue
        elif '<li' in line:
            # Extract content from li tag
            match = re.search(r'<li[^>]*>(.*?)(?:</li>|$)', line, re.DOTALL)
            if match:
                content_text = match.group(1).strip()
                # Remove any remaining tags
                content_text = re.sub(r'<[^>]+>', '', content_text)
                # Decode HTML entities
                content_text = content_text.replace('&nbsp;', ' ')
                content_text = content_text.replace('&amp;', '&')
                content_text = content_text.replace('&lt;', '<')
                content_text = content_text.replace('&gt;', '>')

                # Clean up excessive whitespace
                content_text = re.sub(r'\s+', ' ', content_text).strip()

                # Create proper indentation
                indent = '  ' * (ul_depth - 1)
                result_lines.append(f'{indent}- {content_text}')
        else:
            result_lines.append(line)

    content = '\n'.join(result_lines)

    # Clean up any remaining HTML tags
    content = re.sub(r'<[^>]+>', '', content)

    # Decode common HTML entities
    content = content.replace('&nbsp;', ' ')
    content = content.replace('&amp;', '&')
    content = content.replace('&lt;', '<')
    content = content.replace('&gt;', '>')
    content = content.replace('&quot;', '"')
    content = content.replace('&#39;', "'")

    # Clean up excessive whitespace
    content = re.sub(r' +', ' ', content)  # Multiple spaces to single
    content = re.sub(r'\n\n\n+', '\n\n', content)  # Max 2 newlines
    content = re.sub(r'^\s+', '', content, flags=re.MULTILINE)  # Leading whitespace on lines

    # Ensure blank lines around headers
    content = re.sub(r'(\n)(#{1,6} )', r'\1\n\2', content)
    content = re.sub(r'(#{1,6} .+?)(\n)([^#\n])', r'\1\2\n\3', content)

    # Clean up extra newlines at start
    content = content.lstrip('\n')

    # Ensure file ends with single newline
    content = content.rstrip() + '\n'

    return content


def process_file(filepath: Path) -> bool:
    """Process a single markdown file."""
    try:
        print(f"Processing {filepath.name}...")

        with open(filepath, 'r', encoding='utf-8') as f:
            original = f.read()

        # Check if file has HTML
        if '<' not in original or '>' not in original:
            print(f"  ✓ No HTML found, skipping")
            return False

        # Split frontmatter and content
        parts = original.split('---\n', 2)
        if len(parts) == 3:
            # Has frontmatter
            frontmatter = parts[1]
            content = parts[2]

            # Convert content
            converted_content = convert_html_to_markdown(content)

            # Reassemble
            result = f"---\n{frontmatter}---\n{converted_content}"
        else:
            # No frontmatter
            result = convert_html_to_markdown(original)

        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(result)

        print(f"  ✓ Converted")
        return True

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def main():
    if len(sys.argv) > 1:
        # Process specific files/directories
        paths = [Path(p) for p in sys.argv[1:]]
    else:
        # Process assignments, content, and quizzes by default
        script_dir = Path(__file__).parent
        base_dir = script_dir.parent
        paths = [
            base_dir / 'assignments',
            base_dir / 'content',
            base_dir / 'quizzes'
        ]

    total_processed = 0
    total_converted = 0

    for path in paths:
        if path.is_file() and path.suffix == '.md':
            total_processed += 1
            if process_file(path):
                total_converted += 1
        elif path.is_dir():
            for md_file in sorted(path.glob('*.md')):
                total_processed += 1
                if process_file(md_file):
                    total_converted += 1

    print(f"\n✓ Processed {total_processed} files, converted {total_converted}")


if __name__ == '__main__':
    main()

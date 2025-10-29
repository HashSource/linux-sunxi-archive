#!/usr/bin/env python3

"""Convert MediaWiki HTML pages to compact Markdown format."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import html2text

# Compile regex patterns once for performance
TITLE_PATTERN = re.compile(r"<title>(.*?)</title>", re.IGNORECASE)
EDIT_LINKS_PATTERN = re.compile(r"\[edit\]\([^)]+\)")
NAV_MENU_PATTERN = re.compile(r"## Navigation menu.*", re.DOTALL)
RETRIEVED_FROM_PATTERN = re.compile(r"Retrieved from.*", re.DOTALL)
JUMP_TO_PATTERN = re.compile(r"\[Jump to .*?\]\[.*?\]")
SUNXI_SUBTITLE_PATTERN = re.compile(r"^From linux-sunxi\.org\s*\n", re.MULTILINE)
BLANK_LINES_PATTERN = re.compile(r"\n{3,}")


@dataclass
class ConversionStats:
    """Statistics for HTML to Markdown conversion."""

    total: int = 0
    successful: int = 0
    failed: int = 0

    @property
    def failure_rate(self) -> float:
        return (self.failed / self.total * 100) if self.total > 0 else 0.0


def configure_converter() -> html2text.HTML2Text:
    """Create and configure html2text converter for optimal output."""
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.ignore_images = False
    converter.ignore_emphasis = False
    converter.body_width = 0
    converter.single_line_break = True
    converter.mark_code = True
    converter.unicode_snob = True
    converter.skip_internal_links = False
    converter.inline_links = False
    converter.protect_links = True
    converter.ignore_tables = False
    return converter


def extract_title(html_content: str) -> str:
    """Extract and clean page title from HTML content."""
    if match := TITLE_PATTERN.search(html_content):
        title = match.group(1)
        return (
            title.replace(" - linux-sunxi.org", "")
            .replace("linux-sunxi.org", "")
            .strip()
        )
    return ""


def clean_markdown(markdown: str) -> str:
    """Remove MediaWiki navigation and UI elements from markdown."""
    markdown = EDIT_LINKS_PATTERN.sub("", markdown)
    markdown = NAV_MENU_PATTERN.sub("", markdown)
    markdown = RETRIEVED_FROM_PATTERN.sub("", markdown)
    markdown = JUMP_TO_PATTERN.sub("", markdown)
    markdown = SUNXI_SUBTITLE_PATTERN.sub("", markdown)
    markdown = BLANK_LINES_PATTERN.sub("\n\n", markdown)
    return markdown.strip()


def convert_file(
    html_path: Path, output_path: Path, converter: html2text.HTML2Text
) -> bool:
    """
    Convert a single HTML file to Markdown.

    Args:
        html_path: Path to input HTML file
        output_path: Path to output Markdown file
        converter: Configured html2text converter instance

    Returns:
        True if conversion succeeded, False otherwise
    """
    try:
        html_content = html_path.read_text(encoding="utf-8")

        # Convert to markdown
        markdown = converter.handle(html_content)
        markdown = clean_markdown(markdown)

        # Add title if available
        if title := extract_title(html_content):
            if title not in markdown[:100]:
                markdown = f"# {title}\n\n{markdown}"

        # Write output
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown + "\n", encoding="utf-8")

        return True

    except (IOError, OSError) as e:
        print(f"Error converting {html_path}: {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Unexpected error converting {html_path}: {e}", file=sys.stderr)
        return False


def find_html_files(source_dir: Path) -> list[Path]:
    """Find all HTML files in the source directory."""
    return sorted(source_dir.rglob("*.html"))


def calculate_sizes(source_dir: Path, output_dir: Path) -> tuple[int, int]:
    """Calculate total sizes of HTML and Markdown files."""
    html_size = sum(f.stat().st_size for f in source_dir.rglob("*.html"))
    md_size = sum(f.stat().st_size for f in output_dir.rglob("*.md"))
    return html_size, md_size


def convert_files(
    html_files: list[Path],
    source_dir: Path,
    output_dir: Path,
    progress_interval: int = 50,
) -> ConversionStats:
    """
    Convert multiple HTML files to Markdown.

    Args:
        html_files: List of HTML files to convert
        source_dir: Source directory containing HTML files
        output_dir: Output directory for Markdown files
        progress_interval: Show progress every N files

    Returns:
        ConversionStats with conversion results
    """
    stats = ConversionStats(total=len(html_files))
    converter = configure_converter()

    for i, html_path in enumerate(html_files, 1):
        rel_path = html_path.relative_to(source_dir)
        output_path = output_dir / rel_path.with_suffix(".md")

        if convert_file(html_path, output_path, converter):
            stats.successful += 1
        else:
            stats.failed += 1

        if i % progress_interval == 0 or i == stats.total:
            progress_pct = i * 100 // stats.total
            print(f"Progress: {i}/{stats.total} ({progress_pct}%)")

    return stats


def print_summary(stats: ConversionStats, source_dir: Path, output_dir: Path) -> None:
    """Print conversion summary statistics."""
    separator = "=" * 60

    print()
    print(separator)
    print(f"Successfully converted: {stats.successful}")
    print(f"Failed: {stats.failed}")
    print(f"Total: {stats.total}")
    print(f"Output location: {output_dir.absolute()}")

    if output_dir.exists():
        html_size, md_size = calculate_sizes(source_dir, output_dir)
        reduction = (1 - md_size / html_size) * 100 if html_size > 0 else 0

        print(f"HTML size: {html_size / 1024 / 1024:.2f} MB")
        print(f"Markdown size: {md_size / 1024 / 1024:.2f} MB")
        print(f"Size reduction: {reduction:.1f}%")

    print(separator)


def main() -> int:
    """Main entry point for the conversion script."""
    parser = argparse.ArgumentParser(
        description="Convert MediaWiki HTML pages to Markdown format"
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("linux-sunxi.org"),
        help="Source directory containing HTML files (default: linux-sunxi.org)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("linux-sunxi-markdown"),
        help="Output directory for Markdown files (default: linux-sunxi-markdown)",
    )
    parser.add_argument(
        "--progress",
        type=int,
        default=50,
        help="Show progress every N files (default: 50)",
    )

    args = parser.parse_args()

    if not args.source.exists():
        print(f"Error: Source directory not found: {args.source}", file=sys.stderr)
        return 1

    html_files = find_html_files(args.source)

    if not html_files:
        print(f"Warning: No HTML files found in {args.source}", file=sys.stderr)
        return 0

    print(f"Found {len(html_files)} HTML files")
    print(f"Output directory: {args.output}")
    print()

    stats = convert_files(html_files, args.source, args.output, args.progress)
    print_summary(stats, args.source, args.output)

    return 1 if stats.failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
Conservative formatter for Mount&Blade Warband module-system files.

This is intentionally not a Python formatter. The module system uses valid-ish
Python as a data DSL, and generic formatters tend to destroy troop tables and
operation blocks. By default this tool only reports what would change when
opt-in cleanup flags are enabled. Leading-tab normalization, trailing whitespace
cleanup, operation indentation, and long-line wrapping are opt-in. Long-line
wrapping only runs on lines that can be split safely at top-level commas.
"""

from __future__ import annotations

import argparse
import difflib
import re
from pathlib import Path
from typing import Iterable


DEFAULT_MODULE_DIR = Path("Source/Source - Floris Expanded Mod Pack/Module")
INDENT = "  "
OPENERS = "([{"
CLOSERS = ")]}"
CLOSE_TO_OPEN = {")": "(", "]": "[", "}": "{"}
OPEN_TO_CLOSE = {"(": ")", "[": "]", "{": "}"}
CONTROL_OP_RE = re.compile(r"\((try_begin|try_for_[A-Za-z0-9_]+|else_try|try_end)\b")
FIRST_OP_RE = re.compile(r"^\(([^,\)\s]+)")


def iter_default_files() -> list[Path]:
    if not DEFAULT_MODULE_DIR.exists():
        return []
    return sorted(DEFAULT_MODULE_DIR.glob("module_*.py"))


def iter_paths(raw_paths: Iterable[str]) -> list[Path]:
    paths: list[Path] = []
    for raw_path in raw_paths:
        path = Path(raw_path)
        if path.is_dir():
            paths.extend(sorted(path.glob("module_*.py")))
        else:
            paths.append(path)
    return paths or iter_default_files()


def bracket_delta(text: str) -> int:
    """Return net bracket nesting change, ignoring quoted strings and comments."""
    delta = 0
    i = 0
    quote = ""
    triple = False
    escape = False

    while i < len(text):
        char = text[i]
        nxt3 = text[i : i + 3]

        if quote:
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif triple and nxt3 == quote * 3:
                quote = ""
                triple = False
                i += 2
            elif not triple and char == quote:
                quote = ""
            i += 1
            continue

        if char == "#":
            break
        if nxt3 in ('"""', "'''"):
            quote = char
            triple = True
            i += 3
            continue
        if char in ('"', "'"):
            quote = char
            i += 1
            continue
        if char in OPENERS:
            delta += 1
        elif char in CLOSERS:
            delta -= 1
        i += 1

    return delta


def trim_trailing_and_normalize_leading_tabs(text: str) -> str:
    stripped_right = text.rstrip()
    leading_len = len(stripped_right) - len(stripped_right.lstrip(" \t"))
    leading = stripped_right[:leading_len].replace("\t", INDENT)
    return leading + stripped_right[leading_len:]


def normalize_leading_tabs(text: str, strip_trailing_whitespace: bool, normalize_tabs: bool) -> str:
    line = text.rstrip() if strip_trailing_whitespace else text
    if not normalize_tabs or not line.strip():
        return line
    leading_len = len(line) - len(line.lstrip(" \t"))
    leading = line[:leading_len].replace("\t", INDENT)
    return leading + line[leading_len:]


def format_text(text: str, strip_trailing_whitespace: bool = False, normalize_tabs: bool = False) -> str:
    lines = text.splitlines()
    has_final_newline = text.endswith("\n")
    formatted = [normalize_leading_tabs(line, strip_trailing_whitespace, normalize_tabs) for line in lines]
    output = "\n".join(formatted)
    if has_final_newline or text:
        output += "\n"
    return output


def strip_outer_record(record: str) -> tuple[str, str, str] | None:
    stripped = record.strip()
    suffix = ""
    if stripped.endswith(","):
        stripped = stripped[:-1].rstrip()
        suffix = ","
    if not stripped:
        return None
    opener = stripped[0]
    closer = OPEN_TO_CLOSE.get(opener)
    if closer is None or not stripped.endswith(closer):
        return None
    return opener, stripped[1:-1], closer + suffix


def split_top_level(text: str) -> list[str] | None:
    parts: list[str] = []
    start = 0
    level = 0
    i = 0
    quote = ""
    triple = False
    escape = False

    while i < len(text):
        char = text[i]
        nxt3 = text[i : i + 3]

        if quote:
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif triple and nxt3 == quote * 3:
                quote = ""
                triple = False
                i += 2
            elif not triple and char == quote:
                quote = ""
            i += 1
            continue

        if nxt3 in ('"""', "'''"):
            quote = char
            triple = True
            i += 3
            continue
        if char in ('"', "'"):
            quote = char
            i += 1
            continue
        if char in OPENERS:
            level += 1
        elif char in CLOSERS:
            level -= 1
            if level < 0:
                return None
        elif char == "," and level == 0:
            parts.append(text[start:i].strip())
            start = i + 1
        i += 1

    if quote or level != 0:
        return None
    tail = text[start:].strip()
    if tail:
        parts.append(tail)
    return parts


def format_inline_list(value: str, base_indent: str) -> list[str]:
    outer = strip_outer_record(value)
    if not outer:
        return [base_indent + value]

    opener, inner, closer = outer
    parts = split_top_level(inner)
    if parts is None:
        return [base_indent + value]

    lines = [base_indent + opener]
    item_indent = base_indent + INDENT
    for part in parts:
        lines.append(item_indent + part + ",")
    if len(lines) > 1:
        lines[-1] = lines[-1].rstrip(",")
    lines.append(base_indent + closer)
    return lines


def comma_join(parts: list[str]) -> str:
    return ",".join(parts)


def chunked(parts: list[str], size: int) -> Iterable[list[str]]:
    for index in range(0, len(parts), size):
        yield parts[index : index + size]


def format_troop_inventory(value: str, base_indent: str, items_per_line: int = 4) -> list[str]:
    outer = strip_outer_record(value)
    if not outer:
        return [base_indent + value]

    opener, inner, closer = outer
    parts = split_top_level(inner)
    if parts is None:
        return [base_indent + value]
    if not parts:
        return [base_indent + opener + closer]

    lines = [base_indent + opener]
    item_indent = base_indent + INDENT
    for row_index, row in enumerate(chunked(parts, items_per_line)):
        comma = "," if row_index < (len(parts) - 1) // items_per_line else ""
        lines.append(item_indent + comma_join(row) + comma)
    lines.append(base_indent + closer)
    return lines


def split_trailing_comment(text: str) -> tuple[str, str]:
    i = 0
    quote = ""
    triple = False
    escape = False

    while i < len(text):
        char = text[i]
        nxt3 = text[i : i + 3]

        if quote:
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif triple and nxt3 == quote * 3:
                quote = ""
                triple = False
                i += 2
            elif not triple and char == quote:
                quote = ""
            i += 1
            continue

        if nxt3 in ('"""', "'''"):
            quote = char
            triple = True
            i += 3
            continue
        if char in ('"', "'"):
            quote = char
            i += 1
            continue
        if char == "#":
            return text[:i].rstrip(), text[i:]
        i += 1

    return text.rstrip(), ""


def wrap_record_line(line: str, max_line_length: int) -> list[str]:
    if len(line) <= max_line_length:
        return [line]

    body, comment = split_trailing_comment(line)
    if comment:
        return [line]

    leading_len = len(body) - len(body.lstrip(" "))
    leading = body[:leading_len]
    stripped = body[leading_len:]
    outer = strip_outer_record(stripped)
    if not outer:
        return [line]

    opener, inner, closer = outer
    parts = split_top_level(inner)
    if parts is None or len(parts) < 2:
        return [line]

    lines = [leading + opener]
    item_indent = leading + INDENT
    for index, part in enumerate(parts):
        comma = "," if index < len(parts) - 1 else ""
        lines.append(item_indent + part + comma)
    lines.append(leading + closer)
    return lines


def wrap_long_lines(text: str, max_line_length: int) -> str:
    lines = text.splitlines()
    has_final_newline = text.endswith("\n")
    wrapped: list[str] = []

    for line in lines:
        wrapped.extend(wrap_record_line(line, max_line_length))

    output = "\n".join(wrapped)
    if has_final_newline or text:
        output += "\n"
    return output


def leading_spaces(line: str) -> str:
    return line[: len(line) - len(line.lstrip(" "))]


def leading_whitespace(line: str) -> str:
    return line[: len(line) - len(line.lstrip(" \t"))]


def first_operation_token(stripped: str) -> str:
    match = FIRST_OP_RE.match(stripped)
    return match.group(1) if match else ""


def operation_control_counts(stripped: str) -> tuple[int, int, bool]:
    body, _comment = split_trailing_comment(stripped)
    starts = 0
    ends = 0
    has_else = False

    for match in CONTROL_OP_RE.finditer(body):
        op = match.group(1)
        if op == "try_end":
            ends += 1
        elif op == "else_try":
            has_else = True
        else:
            starts += 1

    return starts, ends, has_else


def with_indent(line: str, indent: str) -> str:
    return indent + line.lstrip(" \t")


def fix_operation_indent(text: str) -> str:
    """Fix indentation inside Warband try blocks without reindenting whole files."""
    lines = text.splitlines()
    has_final_newline = text.endswith("\n")
    fixed: list[str] = []
    level = 0
    base_indent = ""
    list_operation_indent = ""
    dirty_depth = 0

    for line in lines:
        stripped = line.lstrip(" \t")
        if not stripped:
            fixed.append(line)
            continue
        if stripped.startswith(("])", "],")):
            fixed.append(line)
            level = 0
            base_indent = ""
            list_operation_indent = ""
            dirty_depth = 0
            continue

        raw_indent = leading_whitespace(line)
        normalized_indent = raw_indent.replace("\t", INDENT)
        has_tab_indent = "\t" in raw_indent
        token = first_operation_token(stripped)
        starts, ends, has_else = operation_control_counts(stripped)
        is_control_line = bool(starts or ends or has_else)
        is_operation_line = bool(token and not token.startswith(("'", '"')))
        if level == 0 and is_operation_line and not list_operation_indent:
            list_operation_indent = normalized_indent

        if level == 0 and is_control_line and (has_tab_indent or dirty_depth):
            base_indent = list_operation_indent or normalized_indent

        line_level = level
        if token == "try_end":
            line_level = max(level - 1, 0)
        elif token == "else_try":
            line_level = max(level - 1, 0)

        should_reindent = False
        if is_operation_line and (has_tab_indent or dirty_depth):
            should_reindent = True
        elif dirty_depth and stripped.startswith("#") and raw_indent:
            should_reindent = True

        if should_reindent:
            indent_base = base_indent or list_operation_indent or normalized_indent
            fixed.append(with_indent(line, indent_base + INDENT * line_level))
        elif level == 0 and is_operation_line and has_tab_indent and list_operation_indent:
            fixed.append(with_indent(line, list_operation_indent))
        else:
            fixed.append(line)

        if is_control_line:
            next_level = level + starts - ends
            if token == "else_try":
                next_level = max(level - 1, 0) + 1 + starts - ends
            if has_tab_indent or dirty_depth:
                dirty_depth = max(dirty_depth, next_level)
            level = max(next_level, 0)
            if level < dirty_depth:
                dirty_depth = level
            if level == 0:
                base_indent = ""
                dirty_depth = 0

    output = "\n".join(fixed)
    if has_final_newline or text:
        output += "\n"
    return output


def looks_like_troop_record(record: str) -> bool:
    stripped = record.lstrip()
    return stripped.startswith('["') or stripped.startswith("['")


def format_troop_record(record: str) -> str:
    outer = strip_outer_record(record)
    if not outer:
        return record

    opener, inner, closer = outer
    parts = split_top_level(inner)
    if parts is None or len(parts) < 11:
        return record
    if not (parts[0].startswith('"') or parts[0].startswith("'")):
        return record

    lines = ["  " + opener + comma_join(parts[:3]) + ","]
    field_indent = INDENT * 2
    lines.append(field_indent + comma_join(parts[3:7]) + ",")

    if parts[7].startswith("["):
        item_lines = format_troop_inventory(parts[7], field_indent)
        item_lines[-1] += ","
        lines.extend(item_lines)
    else:
        lines.append(field_indent + parts[7] + ",")

    if len(parts) >= 10:
        lines.append(field_indent + comma_join(parts[8:10]) + ",")
    if len(parts) >= 11:
        lines.append(field_indent + parts[10] + ",")

    remaining = parts[11:]
    for row_index, row in enumerate(chunked(remaining, 2)):
        comma = "," if row_index < (len(remaining) - 1) // 2 else ""
        lines.append(field_indent + comma_join(row) + comma)
    lines.append("  " + closer)
    return "\n".join(lines)


def format_troop_records(text: str) -> str:
    lines = text.splitlines()
    has_final_newline = text.endswith("\n")
    formatted: list[str] = []
    i = 0

    while i < len(lines):
        line = trim_trailing_and_normalize_leading_tabs(lines[i])
        if not looks_like_troop_record(line):
            formatted.append(line)
            i += 1
            continue

        record_lines = [line]
        level = bracket_delta(line)
        i += 1
        while level > 0 and i < len(lines):
            next_line = trim_trailing_and_normalize_leading_tabs(lines[i])
            record_lines.append(next_line)
            level += bracket_delta(next_line)
            i += 1

        record = "\n".join(record_lines)
        formatted.extend(format_troop_record(record).splitlines())

    output = "\n".join(formatted)
    if has_final_newline or text:
        output += "\n"
    return output


def process_file(
    path: Path,
    write: bool,
    show_diff: bool,
    troops: bool,
    fix_indent: bool,
    wrap_lines: bool,
    max_line_length: int,
    strip_trailing_whitespace: bool,
    normalize_tabs: bool,
) -> bool:
    old = path.read_text(encoding="utf-8", errors="surrogateescape")
    new = format_text(old, strip_trailing_whitespace=strip_trailing_whitespace, normalize_tabs=normalize_tabs)
    if fix_indent:
        new = fix_operation_indent(new)
    if wrap_lines:
        new = wrap_long_lines(new, max_line_length=max_line_length)
    if troops:
        new = format_troop_records(new)
    changed = old != new

    if changed and show_diff:
        print(
            "".join(
                difflib.unified_diff(
                    old.splitlines(keepends=True),
                    new.splitlines(keepends=True),
                    fromfile=str(path),
                    tofile=str(path),
                )
            ),
            end="",
        )

    if changed and write:
        path.write_text(new, encoding="utf-8", errors="surrogateescape")

    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Format Warband module-system scripts conservatively.")
    parser.add_argument("paths", nargs="*", help="Files or module directories. Defaults to Floris Expanded Module.")
    parser.add_argument("--normalize-leading-tabs", action="store_true", help="Convert leading tabs to spaces.")
    parser.add_argument("--strip-trailing-whitespace", action="store_true", help="Also remove trailing whitespace.")
    parser.add_argument("--fix-operation-indent", action="store_true", help="Fix nested try/else/try_end operation indentation.")
    parser.add_argument("--wrap-long-lines", action="store_true", help="Split safely parsed one-line tuple/list records.")
    parser.add_argument("--max-line-length", type=int, default=160, help="Line length used by --wrap-long-lines.")
    parser.add_argument("--troops", action="store_true", help="Legacy broad troop-table formatter; prefer --wrap-long-lines.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="Rewrite files in place.")
    mode.add_argument("--check", action="store_true", help="Exit non-zero if any file would change.")
    mode.add_argument("--diff", action="store_true", help="Print unified diff without writing.")
    args = parser.parse_args()

    paths = iter_paths(args.paths)
    if not paths:
        print("No module files found.")
        return 1

    changed_paths = []
    for path in paths:
        if not path.exists():
            print(f"Missing: {path}")
            return 1
        changed = process_file(
            path,
            write=args.write,
            show_diff=args.diff,
            troops=args.troops,
            fix_indent=args.fix_operation_indent,
            wrap_lines=args.wrap_long_lines,
            max_line_length=args.max_line_length,
            strip_trailing_whitespace=args.strip_trailing_whitespace,
            normalize_tabs=args.normalize_leading_tabs,
        )
        if changed:
            changed_paths.append(path)

    if args.write:
        for path in changed_paths:
            print(f"Formatted {path}")
    elif args.check and changed_paths:
        for path in changed_paths:
            print(f"Would format {path}")
        return 1
    elif not args.diff:
        if changed_paths:
            for path in changed_paths:
                print(f"Would format {path}")
            print("Run again with --write to update files or --diff to inspect changes.")
        else:
            print("All checked module files are already formatted.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

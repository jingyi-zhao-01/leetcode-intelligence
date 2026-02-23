"""
Code cleaning utilities for submissions.

Normalizes and cleans code for better embeddings and storage.
"""

import re


def _remove_leading_trailing_empty_lines(lines: list) -> list:
    """Remove empty lines from start and end."""
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return lines


def _normalize_indentation(lines: list) -> list:
    """Normalize indentation to 4 spaces."""
    normalized_lines = []
    for line in lines:
        if line.strip():
            leading_ws = len(line) - len(line.lstrip())
            normalized_leading = line[:leading_ws].replace("\t", "    ")
            normalized_leading = " " * (len(normalized_leading) // 4 * 4)
            normalized_lines.append(normalized_leading + line.lstrip())
        else:
            normalized_lines.append("")
    return normalized_lines


def _remove_multiple_empty_lines(lines: list) -> list:
    """Remove consecutive empty lines, keep max 1."""
    result_lines = []
    prev_empty = False
    for line in lines:
        if not line.strip():
            if not prev_empty:
                result_lines.append("")
            prev_empty = True
        else:
            result_lines.append(line)
            prev_empty = False
    return result_lines


def clean_python_code(code: str) -> str:
    """
    Clean and normalize Python code for embeddings.

    Args:
        code: Raw Python code string

    Returns:
        Cleaned and normalized code
    """
    if not code:
        return ""

    # Remove trailing whitespace from each line
    lines = [line.rstrip() for line in code.split("\n")]

    # Remove leading/trailing empty lines
    lines = _remove_leading_trailing_empty_lines(lines)

    # Normalize indentation
    lines = _normalize_indentation(lines)

    # Remove multiple consecutive empty lines
    lines = _remove_multiple_empty_lines(lines)

    return "\n".join(lines)


def _find_function_start(lines: list) -> int:
    """Find the line where function definition starts."""
    for i, line in enumerate(lines):
        if re.match(r"\s*def\s+", line):
            return i
    return -1


def _calculate_min_indent(lines: list, start_idx: int) -> int:
    """Calculate minimum indentation after function definition."""
    min_indent = float("inf")
    for line in lines[start_idx + 1 :]:
        if line.strip():
            indent = len(line) - len(line.lstrip())
            min_indent = min(min_indent, indent)
    return 0 if min_indent == float("inf") else min_indent


def _dedent_function(lines: list, start_idx: int, min_indent: int) -> str:
    """Remove class indentation from function."""
    result = [lines[start_idx].lstrip()]
    for line in lines[start_idx + 1 :]:
        if line.strip():
            result.append(line[min_indent:] if min_indent > 0 else line)
        else:
            result.append("")
    return "\n".join(result)


def extract_function_only(code: str) -> str:
    """
    Extract just the function definition from a class-wrapped solution.

    For LeetCode submissions that wrap functions in a Solution class,
    this extracts the inner function definition.
    """
    code = clean_python_code(code)

    # Check if code starts with class definition
    if "class Solution" not in code:
        return code

    lines = code.split("\n")
    start_idx = _find_function_start(lines)

    if start_idx == -1:
        return code

    min_indent = _calculate_min_indent(lines, start_idx)
    return _dedent_function(lines, start_idx, min_indent)


def extract_thought(code: str) -> str | None:
    """
    Extract @thought comments from code.

    Looks for @thought markers (typically in docstrings or comments)
    and extracts the thought content.

    Args:
        code: Raw code string

    Returns:
        Extracted thought text or None if no @thought found
    """
    # Look for @thought as a marker (followed by colon or space or special char)
    import re

    if not code or not re.search(r"@thought\s*:", code):
        return None

    lines = code.split("\n")
    thought_lines = []
    in_thought = False
    in_docstring = False
    docstring_delimiter = None

    for line in lines:
        stripped = line.strip()

        # Track docstring boundaries
        if '"""' in stripped or "'''" in stripped:
            # Find which delimiter is present
            if '"""' in stripped:
                delimiter = '"""'
            else:
                delimiter = "'''"

            # Count occurrences to determine if entering/exiting docstring
            count = stripped.count(delimiter)
            if count == 2:
                # Single line docstring, don't change state
                pass
            elif count == 1:
                if not in_docstring:
                    in_docstring = True
                    docstring_delimiter = delimiter
                elif delimiter == docstring_delimiter:
                    in_docstring = False
                    docstring_delimiter = None

        # Check if @thought marker exists (with colon)
        if re.search(r"@thought\s*:", line):
            in_thought = True
            # Extract text after @thought: marker
            thought_part = re.sub(r".*@thought\s*:\s*", "", line).strip()
            if thought_part:
                thought_lines.append(thought_part)
            continue

        # Collect lines after @thought until we exit docstring or hit actual code
        if in_thought:
            if not stripped or stripped.startswith("#"):
                # Empty line or comment
                if stripped.startswith("#"):
                    thought_lines.append(stripped[1:].strip())
            elif stripped.startswith('"""') or stripped.startswith("'''"):
                # Docstring boundary - stop collecting if exiting docstring
                if not in_docstring:
                    in_thought = False
            elif in_docstring:
                # We're in a docstring, so collect this line
                thought_lines.append(stripped)
            else:
                # Hit actual code outside docstring, stop collecting
                in_thought = False

    thought_text = " ".join(thought_lines).strip()
    return thought_text if thought_text else None


def normalize_for_embedding(code: str, extract_function: bool = True) -> str:
    """
    Fully normalize code for embedding.

    This is the main function to call for preparing code for embeddings.
    Comments are retained as they provide semantic meaning for embeddings.

    Args:
        code: Raw Python code
        extract_function: Whether to extract function from class wrapper

    Returns:
        Normalized code ready for embedding (with comments intact)
    """
    # Clean the code
    cleaned = clean_python_code(code)

    # Extract function if it's in a class wrapper
    if extract_function:
        cleaned = extract_function_only(cleaned)

    return cleaned

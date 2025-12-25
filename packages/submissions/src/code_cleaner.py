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

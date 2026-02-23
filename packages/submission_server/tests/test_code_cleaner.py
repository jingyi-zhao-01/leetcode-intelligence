"""Test cases for code cleaner utility."""

from src.submissions.code_cleaner import (
    clean_python_code,
    extract_function_only,
    normalize_for_embedding,
)


def test_clean_python_code():
    """Test basic code cleaning."""
    code = """
    
def foo(x):
    return x + 1
    
"""
    result = clean_python_code(code)
    assert "def foo" in result
    assert "return x + 1" in result
    assert result.count("\n\n") == 0  # No multiple empty lines


def test_extract_function_only():
    """Test function extraction from class."""
    code = """class Solution:
    def twoSum(self, nums, target):
        return []"""

    result = extract_function_only(code)
    assert result.startswith("def twoSum")
    assert "class" not in result


def test_normalize_for_embedding():
    """Test full normalization for embeddings."""
    code = """
    class Solution:
        def foo(x):
            # This comment should be retained
            return x + 1
    """
    result = normalize_for_embedding(code)
    assert "def foo" in result
    assert "# This comment should be retained" in result
    assert "class" not in result

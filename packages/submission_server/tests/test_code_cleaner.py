"""Test cases for code cleaner utility."""

from pathlib import Path
from code_cleaner import (
    clean_python_code,
    extract_function_only,
    extract_thought,
    normalize_for_embedding,
)


def load_sample_code() -> str:
    """Load sample.txt as benchmark code."""
    sample_path = Path(__file__).parent / "sample.txt"
    with open(sample_path, "r") as f:
        return f.read()


def test_sample_code_extract_thought():
    """Test @thought extraction from sample.txt."""
    sample = load_sample_code()
    thought = extract_thought(sample)

    assert thought is not None, "Should extract @thought from sample"
    assert "two pointer approach" in thought.lower(), "Should contain pointer approach"
    assert (
        "last non zero element" in thought.lower()
    ), "Should contain algorithm details"


def test_sample_code_normalize():
    """Test normalization preserves logic but removes class wrapper."""
    sample = load_sample_code()
    normalized = normalize_for_embedding(sample)

    assert "def moveZeroes" in normalized
    assert "p1" in normalized
    assert "class Solution" not in normalized
    # Comments should be retained
    assert "#" in normalized


def test_sample_code_extract_function():
    """Test function extraction from sample.txt."""
    sample = load_sample_code()
    extracted = extract_function_only(sample)

    assert "def moveZeroes" in extracted
    assert "class" not in extracted


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


def test_extract_thought_no_thought():
    """Test extract_thought returns None when no @thought marker."""
    code = """class Solution:
    def solve(self, nums):
        # Regular comment without @thought marker
        return 42
"""
    thought = extract_thought(code)
    assert thought is None

'''Test finding the longest palindromic substring'''

import pytest
from app import Palindrome

@pytest.fixture
def solver() -> Palindrome:
    return Palindrome()

@pytest.mark.parametrize("grid, expected, description", [
# Standard LeetCode cases
    ("babad", {"bab", "aba"}, "Standard odd-length palindrome"),
    ("cbbd", {"bb"}, "Standard even-length palindrome"),
    
    # Edge cases: empty, single char, all unique
    ("", {""}, "Empty string"),
    ("a", {"a"}, "Single character"),
    ("ac", {"a", "c"}, "Two unique characters"),
    ("abcdef", {"a", "b", "c", "d", "e", "f"}, "All unique characters"),
    
    # Full-string palindromes (fast-path check)
    ("racecar", {"racecar"}, "Full odd-length palindrome"),
    ("abba", {"abba"}, "Full even-length palindrome"),
    
    # Duplicate character collapsing
    ("aaaa", {"aaaa"}, "All identical characters"),
    ("caaaab", {"aaaa"}, "Identical characters in middle"),
    ("aaabaaaa", {"aaabaaa"}, "Slightly asymmetrical identical characters"),
    
    # Palindrome at start, middle, and end
    ("abacdfgdcaba", {"aba"}, "Multiple identical palindromes"),
    ("xyzracecar123", {"racecar"}, "Palindrome in the middle of junk characters"),
    ("12345noon", {"noon"}, "Palindrome at the end"),
    
    # Digits & mixed alphanumeric
    ("12321", {"12321"}, "Numeric palindrome"),
    ("a1b2b1c", {"1b2b1"}, "Mixed alphanumeric palindrome"),
    
    # Max constraint stress test (n = 1000)
    ("a" * 1000, {"a" * 1000}, "Maximum length identical characters"),
    ("b" + "a" * 999, {"a" * 999}, "Maximum length identical with different start char")
])
def test_longest_palindromic(solver, grid, expected, description):
    assert solver.longestPalindrome(grid) in expected, description

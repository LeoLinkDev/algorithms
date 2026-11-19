import pytest
from app import Solution


@pytest.fixture
def solver():
    return Solution()


@pytest.mark.parametrize(
    "s, expected",
    [
        # Standard LeetCode examples
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        # Edge cases
        ("", 0),
        ("a", 1),
        (" ", 1),
        ("  ", 1),
        ("au", 2),
        # All unique characters
        ("abcdefg", 7),
        # Tricky sliding window cases (e.g., duplicates outside current window)
        ("abba", 2),
        ("dvdf", 3),
        ("tmmzuxt", 5),
        ("anviaj", 5),
        # Duplicates at start / end
        ("aab", 2),
        ("abb", 2),
        ("abcda", 4),
        # Digits, symbols, and mixed case (ASCII)
        ("aA", 2),
        ("12345123", 5),
        ("!@#$%^&*()!", 10),
        ("a b c a", 3),
    ],
)
def test_length_of_longest_substring(solver, s, expected):
    assert solver.lengthOfLongestSubstring(s) == expected


def test_large_input(solver):
    # 95 printable ASCII characters repeated
    ascii_printable = "".join(chr(i) for i in range(32, 127))
    s = ascii_printable * 500
    assert solver.lengthOfLongestSubstring(s) == 95
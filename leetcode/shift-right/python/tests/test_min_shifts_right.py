'''Test min shifts right'''

import pytest
from typing import List
from app import ShiftRight

@pytest.fixture
def solver() -> ShiftRight:
    return ShiftRight()

@pytest.mark.parametrize("grid, expected, desc", [
    # 1. Standard rotation: Pivot is in the middle (drop_idx = 3)
    ([3, 4, 5, 1, 2], 2, "Standard rotation"),
    
    # 2. Already sorted: No drop point (drop_idx = -1)
    ([1, 3, 5], 0, "Already sorted"),
    
    # 3. Wrap-around failure: 1 drop (2 -> 1), but nums[-1] > nums[0] (4 > 2)
    ([2, 1, 4], -1, "Wrap-around failure"),
    
    # 4. Minimum length (n = 1): Single-element array is trivially sorted
    ([42], 0, "Minimum length (n = 1)"),
    
    # 5. Two elements rotated (n = 2): Smallest possible non-trivial valid shift
    ([10, 5], 1, "Two elements rotated (n = 2)"),
    
    # 6. Maximum shifts (n - 1): Drop occurs immediately at index 1
    ([5, 1, 2, 3, 4], 4, "Maximum shifts (n - 1)"),
    
    # 7. Single shift needed: Drop occurs at the very last index (n - 1)
    ([2, 3, 4, 5, 1], 1, "Single shift needed"),
    
    # 8. Strictly descending (n >= 3): Multiple drops; fails on second drop
    ([5, 4, 3, 2, 1], -1, "Strictly descending"),
    
    # 9. Sorted prefix, invalid suffix: 1 drop (5 -> 3), fails wrap-around (4 > 1)
    ([1, 2, 5, 3, 4], -1, "Sorted prefix, invalid suffix"),
    
    # 10. Late wrap-around trap: Valid pivot (28 < 29), last element fails (62 > 29)
    ([29, 30, 88, 28, 62], -1, "Late wrap-around trap"),
])
def test_min_shifts_right(solver, grid, expected, desc):
    assert solver.minimumRightShifts(grid) == expected, f"Failed on : {desc}"
'''Chebyshev tests'''

import pytest

from app import Solution

@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize("grid, expected", [
    # 3x4 all 0s: placing a 1 at (1, 1) or (1, 2) reaches all cells within Chebyshev distance 2
    ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 2),

    # 2x4 with 1s on the right edge: placing a 1 at col 1 covers cols 0..2 within distance 1
    ([[0, 0, 0, 1], [0, 0, 0, 1]], 1),

    # 2x2 all 1s: every cell is already a delivery center -> distance 0
    ([[1, 1], [1, 1]], 0),

    # 2x2 with a single 0: converting (1, 1) to 1 makes all cells 1s -> distance 0
    ([[1, 1], [1, 0]], 0),

    # 1x1 single 0: converting the only cell to 1 -> distance 0
    ([[0]], 0),

    # 1x1 single 1 (extra edge case): already a center -> distance 0
    ([[1]], 0),

    # 3x3 with one 1 at top-left: placing a 1 at center (1, 1) covers the whole 3x3 within distance 1
    ([[1, 0, 0], [0, 0, 0], [0, 0, 0]], 1),

    # 3x4 with opposite corners: placing a 1 in the middle (e.g., (1, 1) or (1, 2)) covers all within distance 1
    ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]], 2),

    # 5x5 all 0s: placing a 1 at center (2, 2) reaches the furthest corners in max(|2-0|, |2-0|) = 2
    ([[0] * 5 for _ in range(5)], 2),

    # 1x7 row of 0s: placing a 1 at the midpoint (index 3) reaches ends (0 and 6) in distance 3
    ([[0, 0, 0, 0, 0, 0, 0]], 3),

    # 1x7 row with 1 at left end: uncovered cells for k=2 are indices 3..6; placing 1 at index 4 covers them within 2
    ([[1, 0, 0, 0, 0, 0, 0]], 2),

    # 7x1 column of 0s (extra vertical 1D edge case): placing 1 at row 3 gives max distance 3
    ([[0], [0], [0], [0], [0], [0], [0]], 3),

    # 101x101 large empty grid (included from the standalone performance test): placing 1 at (50, 50) -> distance 50
    ([[0] * 101 for _ in range(101)], 50),
])
def test_get_min_inconvenience(solver, grid, expected):
    assert solver.getMinInconvenience(grid) == expected
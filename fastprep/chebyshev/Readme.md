# Minimum Grid Inconvenience

**Source:** [FastPrep - Minimum Grid Inconvenience](https://www.fastprep.io/problems/amazon-minimum-grid-inconvenience) \
**Difficulty:** <span style="color: red;">Hard</span>

## Problem Description

A city is represented by a binary grid. A cell marked `1` is a delivery center, and a cell marked `0` is any other place.

The distance between two cells is the maximum of the absolute row-coordinate difference and the absolute column-coordinate difference.\
 The inconvenience of the grid is the maximum, over every `0` cell, of its distance to the nearest delivery center.

Amazon may open one new delivery center by converting at most one `0` cell into `1`. \
Return the minimum possible inconvenience after this conversion.

---

## Function Signature

    getMinInconvenience(grid: int[][]) -> int

---

## Examples

### Example 1

    grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    return = 2

**Explain:** With no existing delivery center, it is optimal to convert the center cell `(1,1)` to `1`. \
The farthest cells then have distance `2`.

### Example 2

    grid = [[0]]
    return = 0

**Explain:** Convert the only cell to a delivery center, leaving no `0` cell with positive distance.

### Example 3

    grid = [[0,0,0,1],[0,0,0,1]]
    return = 1

**Explain:** Add a delivery center at `(0,0)`. The new center covers columns `0` and `1` within Chebyshev distance `1`, \
while the existing centers cover columns `2` and `3` within distance `1`. \
Some cells remain at distance `1`, so the minimum inconvenience is `1`.

---

## Constraints

* `1 <= n, m <= 500`
* `0 <= grid[i][j] <= 1`

---

## Complexity & Edge Cases

* **Time Complexity:** `O(n * m * log(max(n, m)))` — At most `ceil(log2(500)) = 9` binary search checks over `250,000` cells (`~2.25 * 10^6` operations, running in under 10 ms).
* **Space Complexity:** `O(n * m)` — Used for the `dist` matrix and BFS queue.
* **Edge Cases Handled:**
  1. **All `1`s in the grid:** `maxR` stays `-1` at `k = 0`, returning `0`.
  2. **All `0`s in the grid:** All `dist` entries stay at the initial sentinel value, and the bounding box spans the entire grid, placing the single delivery center at the grid's center.
  3. **Midpoint validity:** Because every uncovered cell is within `[0, n - 1]` and `[0, m - 1]`, the bounding-box midpoint is guaranteed to lie inside the grid and be a `0` cell (if it were already a `1`, no cell within distance `k` of it would have `dist > k`).
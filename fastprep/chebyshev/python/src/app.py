"""
File: app.py (AMAZON Coding Challenge)
Author: Leo Gurdian
Date: 2026-11-13

Problem: Minimum Grid Inconvenience (Amazon OA)
Source: https://www.fastprep.io/problems/amazon-minimum-grid-inconvenience

Description:
    A city is represented by a binary grid where 1 is a delivery center and 0
    is an ordinary location. Distance is measured using Chebyshev distance:
    max(|r1 - r2|, |c1 - c2|). The inconvenience of the grid is the maximum
    distance from any 0 cell to its nearest delivery center.

    Return the minimum possible inconvenience after converting at most one 0
    cell into a 1.

Constraints:
    - 1 <= n, m <= 500
    - 0 <= grid[i][j] <= 1

Approach:
    1. 8-Directional Multi-Source BFS from all existing 1s to compute each
       cell's initial distance to the nearest delivery center.
    2. Binary search on the target inconvenience k in [0, max(n, m) - 1],
       checking if the bounding box of all cells with dist > k spans at most
       2k in both rows and columns.

Complexity:
    - Time:  O(n * m * log(max(n, m)))
    - Space: O(n * m)
"""
from collections import deque
from typing import List

class Solution:
  def getMinInconvenience(self, grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    dist = [[999] * m for _ in range(n)]
    q = deque()

    #1. set distance of all existing centers (1's) to zero
    for r in range(n):
      for c in range(m):
        if grid[r][c]: # is it a 1 ? 
          dist[r][c] = 0
          q.append((r, c))

    #2. set unvisited neighbor rows and cols to 1, and append to queue
    while q:
      r, c = q.popleft()
      d = dist[r][c] + 1
      for nr in (r - 1, r, r + 1):
        for nc in (c - 1, c, c + 1):
          if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] > d: #unvisited?
            dist[nr][nc] = d
            q.append((nr, nc))
            
    #3. Binary search on the minimum inconvenience k (mid)
    # Can we get every cell within k steps of a delivery center?
    def can_achieve(k: int) -> bool:
      uncovered = [(r, c) for r in range(n) for c in range(m) if dist[r][c] > k]
      if not uncovered:
        return True
      rows, cols = zip(*uncovered)
      return max(rows) - min(rows) <= 2 * k and max(cols) - min(cols) <= 2 * k

    #4. compare achievables and return lowest
    lo, hi = 0, max(n, m) - 1
    while lo < hi:
      mid = (lo + hi) // 2
      if can_achieve(mid):
        hi = mid
      else:
        lo = mid + 1
    return lo

def main():
  solver = Solution()

if __name__ == "__main__":
  main()
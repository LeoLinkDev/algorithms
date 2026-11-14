using System;

namespace Algorithms;

partial class Chebyshev
{
    /* Minimum Grid Inconvenience
    * https://www.fastprep.io/problems/amazon-minimum-grid-inconvenience
    * 
    * Complexity & Edge Cases:
    *
    * - Time Complexity: O(n * m * log(max(n, m)))
    *   At most ceil(log2(500)) = 9 binary search checks over 250,000 cells
    *   (~2.25 * 10^6 operations, running in under 10 ms).
    *
    * - Space Complexity: O(n * m)
    *   Used for the `dist` matrix and BFS queue.
    *
    * - Edge Cases Handled:
    *   1. All 1s in the grid: `maxR` stays -1 at k = 0, returning 0.
    *   2. All 0s in the grid: All `dist` entries stay `int.MaxValue`, and the
    *      bounding box spans the entire grid, placing the single delivery
    *      center at the grid's center.
    *   3. Midpoint validity: Because every uncovered cell is within [0, n - 1]
    *      and [0, m - 1], the bounding-box midpoint is guaranteed to lie inside
    *      the grid and be a 0 cell (if it were already a 1, no cell within
    *      distance k of it would have `dist > k`).
    */   
    public static int getMinInconvenience(List<List<int>> grid)
    {
        int n = grid.Count;
        int m = grid[0].Count;

        int[,] dist = new int[n, m];
        var queue = new Queue<(int r, int c)>();

        // 1. Multi-source BFS from all existing delivery centers (1s)
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (grid[i][j] == 1)
                {
                    dist[i, j] = 0;
                    queue.Enqueue((i, j));
                }
                else
                {
                    dist[i, j] = int.MaxValue;
                }
            }
        }

        while (queue.Count > 0)
        {
            var (r, c) = queue.Dequeue();
            int nextDist = dist[r, c] + 1;

            for (int dr = -1; dr <= 1; dr++)
            {
                for (int dc = -1; dc <= 1; dc++)
                {
                    int nr = r + dr;
                    int nc = c + dc;
                    if (nr >= 0 && nr < n && nc >= 0 && nc < m && dist[nr, nc] > nextDist)
                    {
                        dist[nr, nc] = nextDist;
                        queue.Enqueue((nr, nc));
                    }
                }
            }
        }

        // 2. Binary search for the minimum achievable inconvenience
        int low = 0, high = Math.Max(n, m);
        while (low < high)
        {
            int mid = low + (high - low) / 2;
            if (CanAchieve(dist, n, m, mid))
                high = mid;
            else
                low = mid + 1;
        }

        return low;
    }

    private static bool CanAchieve(int[,] dist, int n, int m, int mid)
    {
        int minR = n;
        int minC = m;
        int maxR = -1;
        int maxC = -1;

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (dist[i, j] > mid)
                {
                    if (i < minR) minR = i;
                    if (i > maxR) maxR = i;
                    if (j < minC) minC = j;
                    if (j > maxC) maxC = j;
                }
            }
        }

        // All cells already have distance <= mid
        if (maxR == -1) return true;

        // A single square of radius k covers all uncovered cells iff width and height <= 2k
        return (maxR - minR <= 2 * mid) && (maxC - minC <= 2 * mid);
    }
}
"""
This problem is a variation of the standard Unique Paths problem, but now some cells are
blocked by obstacles. The robot starts at the top-left corner (0,0) and wants to reach the
bottom-right corner (m-1, n-1). The robot may only move right or down. Any cell marked 1
is an obstacle and cannot be stepped on.

We use Dynamic Programming to count the number of valid paths.

Key idea:
For each cell (i, j), the number of ways to reach it is:
    dp[i][j] = dp[i-1][j] + dp[i][j-1]
BUT only if the cell is not an obstacle.

If a cell contains an obstacle (value = 1), then:
    dp[i][j] = 0
because no path can go through that cell.

Steps:
1. If the starting cell (0,0) has an obstacle, return 0 immediately.
2. Initialize a 2D dp array of size m x n with 0s.
3. Set dp[0][0] = 1 (if it's not an obstacle).
4. Traverse each cell:
        - If obstacleGrid[i][j] == 1, set dp[i][j] = 0.
        - Otherwise:
            up = dp[i-1][j] if i > 0 else 0
            left = dp[i][j-1] if j > 0 else 0
            dp[i][j] = up + left
5. The answer is dp[m-1][n-1].

Why this works:
A path to any cell can only come from the cell above or the cell to the left, and we skip
blocked cells by assigning 0 ways to them.

Time Complexity:
    O(m * n), since we iterate through the grid once.

Space Complexity:
    O(m * n), due to the dp grid. (This can be optimized to O(n), but this version is simpler.)

Final Code:
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the starting point is an obstacle
        if obstacleGrid[0][0] == 1:
            return 0
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue

                if i == 0 and j == 0:
                    continue  # already set

                up = dp[i-1][j] if i > 0 else 0
                left = dp[i][j-1] if j > 0 else 0

                dp[i][j] = up + left

        return dp[m-1][n-1]
"""
This dynamic programming approach correctly counts all valid paths while avoiding obstacles.
"""

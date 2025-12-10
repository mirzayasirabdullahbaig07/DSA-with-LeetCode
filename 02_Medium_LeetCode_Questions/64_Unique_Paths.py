"""
This problem asks for the number of unique paths a robot can take to move from the top-left
corner of an m x n grid to the bottom-right corner. The robot may only move either right
or down at any point.

We solve this using Dynamic Programming with space optimization.

Idea:
For each cell (i, j) in the grid, the number of ways to reach that cell is the sum of:
    - ways to reach the cell above it (i-1, j)
    - ways to reach the cell to the left (i, j-1)

Thus:
    dp[i][j] = dp[i-1][j] + dp[i][j-1]

To reduce space usage, instead of keeping an entire 2D dp array, we maintain only two rows:
    - prev: represents dp for the previous row (i-1)
    - curr: represents dp for the current row (i)

Algorithm:
1. Initialize prev as a list of zeros of length n.
2. Loop through each row:
      - Create a new curr array of size n.
      - For each column j:
            - If (i, j) is the starting cell (0,0), dp = 1.
            - Otherwise:
                up = prev[j] if we’re not in the first row
                left = curr[j-1] if we’re not in the first column
                curr[j] = up + left
      - Update prev = curr.
3. The bottom-right cell value is in prev[-1].

Time Complexity:
    O(m * n), because we visit each cell once.

Space Complexity:
    O(n), storing only one row at a time instead of the full grid.

Final Code:
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize the previous row with 0s
        prev = [0] * n

        for i in range(m):
            # Initialize the current row
            curr = [0] * n
            for j in range(n):
                if i == 0 and j == 0:
                    curr[j] = 1  # Start position
                else:
                    up = prev[j] if i > 0 else 0
                    left = curr[j-1] if j > 0 else 0
                    curr[j] = up + left
            prev = curr  # Update previous row

        return prev[-1]
"""
This dynamic programming approach efficiently calculates the number of unique paths.
"""

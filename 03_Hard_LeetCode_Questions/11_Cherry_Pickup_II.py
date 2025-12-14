"""
        CHERRY PICKUP II – DYNAMIC PROGRAMMING EXPLANATION

        We are given a grid where each cell contains cherries.
        Two robots start at the top row:
        - Robot 1 starts at column 0
        - Robot 2 starts at column (cols - 1)

        At every step:
        - Both robots move down to the next row
        - Each robot can move left (-1), stay (0), or move right (+1)
        - Robots must stay within the grid
        - Both robots must reach the last row

        If both robots land on the same cell, cherries are counted only once.

        ------------------------------------------------------------
        DYNAMIC PROGRAMMING APPROACH
        ------------------------------------------------------------

        We use a 3D DP array:
        dp[row][col1][col2]

        Meaning:
        - row   -> current row index
        - col1  -> column of Robot 1
        - col2  -> column of Robot 2
        - value -> maximum cherries collected from this state to the bottom

        ------------------------------------------------------------
        BASE CASE
        ------------------------------------------------------------

        When we reach the last row:
        - If both robots are in the same column, take cherries once
        - Otherwise, take cherries from both positions

        ------------------------------------------------------------
        TRANSITION
        ------------------------------------------------------------

        From dp[row][col1][col2], both robots move to row + 1.
        Each robot has 3 choices: left, stay, or right.

        We try all 9 combinations of movements:
        (dc1, dc2) ∈ {-1, 0, 1} × {-1, 0, 1}

        For each valid move:
        - Ensure new positions stay inside the grid
        - Choose the maximum cherries from the next row

        ------------------------------------------------------------
        CURRENT CHERRIES
        ------------------------------------------------------------

        After selecting the best future state:
        - If col1 == col2 → add grid[row][col1] once
        - Else → add grid[row][col1] + grid[row][col2]

        ------------------------------------------------------------
        FINAL ANSWER
        ------------------------------------------------------------

        The result is stored at:
        dp[0][0][cols - 1]

        This represents:
        - Starting at row 0
        - Robot 1 at column 0
        - Robot 2 at column cols - 1

        ------------------------------------------------------------
        TIME AND SPACE COMPLEXITY
        ------------------------------------------------------------

        Time Complexity:
        O(rows × cols × cols × 9)

        Space Complexity:
        O(rows × cols × cols)

        This solution efficiently computes the maximum cherries
        both robots can collect.
"""

from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        dp = [[[-1] * cols for _ in range(cols)] for _ in range(rows)]

        for c1 in range(cols):
            for c2 in range(cols):
                if c1 == c2:
                    dp[rows - 1][c1][c2] = grid[rows - 1][c1]
                else:
                    dp[rows - 1][c1][c2] = grid[rows - 1][c1] + grid[rows - 1][c2]

        for r in range(rows - 2, -1, -1):
            for c1 in range(cols):
                for c2 in range(cols):
                    max_cherries = 0
                    for dc1 in (-1, 0, 1):
                        for dc2 in (-1, 0, 1):
                            nc1, nc2 = c1 + dc1, c2 + dc2
                            if 0 <= nc1 < cols and 0 <= nc2 < cols:
                                max_cherries = max(
                                    max_cherries,
                                    dp[r + 1][nc1][nc2]
                                )

                    if c1 == c2:
                        dp[r][c1][c2] = grid[r][c1] + max_cherries
                    else:
                        dp[r][c1][c2] = grid[r][c1] + grid[r][c2] + max_cherries

        return dp[0][0][cols - 1]

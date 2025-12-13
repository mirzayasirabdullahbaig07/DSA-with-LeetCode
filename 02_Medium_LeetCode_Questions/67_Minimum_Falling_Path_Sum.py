"""
        PROBLEM TYPE:
        - Dynamic Programming (2D DP)

        TECHNIQUE USED:
        - Bottom-Up Dynamic Programming
        - Space Optimization using Rolling Array

        IDEA:
        - Each cell in the matrix depends on three cells from the previous row:
          (i-1, j-1), (i-1, j), (i-1, j+1)
        - Instead of storing a full DP table, only the previous row is stored.

        DP STATE:
        - prev[j] represents the minimum falling path sum to reach column j
          in the previous row.

        TRANSITION:
        - curr[j] = matrix[i][j] + min(
                        prev[j-1],   # left diagonal
                        prev[j],     # directly above
                        prev[j+1]    # right diagonal
                    )

        BASE CASE:
        - For the first row, the minimum path sum is the value of the cell itself.

        FINAL ANSWER:
        - The minimum value in the last DP row.

        TIME COMPLEXITY:
        - O(n^2), where n is the number of rows (and columns).
        - Every cell is processed exactly once.

        SPACE COMPLEXITY:
        - O(n), due to two 1D arrays (prev and curr).
        - Optimized from O(n^2) of a full DP table.

        WHY DP WORKS:
        - Optimal substructure: minimum path to a cell depends on minimum paths above it.
        - Overlapping subproblems: same subpaths are reused.
        """

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:


        rows = len(matrix)
        cols = len(matrix[0])

        # Initialize DP for the first row
        prev = [matrix[0][j] for j in range(cols)]

        # Build the solution row by row
        for i in range(1, rows):
            curr = [0] * cols
            for j in range(cols):
                left = prev[j - 1] if j > 0 else float("inf")
                up = prev[j]
                right = prev[j + 1] if j < cols - 1 else float("inf")

                curr[j] = matrix[i][j] + min(left, up, right)

            # Move to the next row
            prev = curr

        # Return the minimum path sum from the last row
        return min(prev)

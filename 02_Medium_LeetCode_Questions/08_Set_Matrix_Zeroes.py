"""
        LEETCODE PROBLEM: 73. Set Matrix Zeroes
        ---------------------------------------

        QUESTION STATEMENT:
        -------------------
        Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
        You must do it in place.

        EXAMPLES:
        ---------
        Example 1:
        Input:  matrix = [[1,1,1],
                          [1,0,1],
                          [1,1,1]]
        Output: [[1,0,1],
                 [0,0,0],
                 [1,0,1]]

        Example 2:
        Input:  matrix = [[0,1,2,0],
                          [3,4,5,2],
                          [1,3,1,5]]
        Output: [[0,0,0,0],
                 [0,4,5,0],
                 [0,3,1,0]]

        CONSTRAINTS:
        ------------
        - m == matrix.length
        - n == matrix[0].length
        - 1 <= m, n <= 200
        - -2^31 <= matrix[i][j] <= 2^31 - 1

        FOLLOW UP:
        ----------
        - O(mn) extra space solution is trivial but not optimal.
        - O(m+n) space solution is better.
        - Best: O(1) extra space (reuse matrix itself as storage).

        APPROACH / TECHNIQUE:
        ---------------------
        We use the **"Marker in First Row & First Column"** technique:
        1. Check if the first row and first column need to be zeroed.
        2. Use first row and column as "flags":
           - If matrix[i][j] == 0 → mark row by setting matrix[i][0] = 0
                                   mark col by setting matrix[0][j] = 0
        3. Traverse again, zero out cells based on these markers.
        4. Finally, handle the first row and column separately.

        WHY THIS WORKS:
        ---------------
        - Instead of extra memory, we use the matrix’s first row/col as markers.
        - Preserves O(1) space while covering all cases.
        - Each element is touched only a constant number of times.

        TIME COMPLEXITY:
        ----------------
        - O(m * n), since we traverse the matrix twice.

        SPACE COMPLEXITY:
        -----------------
        - O(1) extra space (modifies matrix in place).

        DRY RUN:
        --------
        Input: [[1,1,1],
                [1,0,1],
                [1,1,1]]

        Step 1: first_row_zero = False, first_col_zero = False
        Step 2: Found matrix[1][1] = 0 → mark row & col
                matrix = [[1,0,1],
                          [0,0,1],
                          [1,1,1]]

        Step 3: Apply marks:
                Row 1 and Col 1 → set to 0
                matrix = [[1,0,1],
                          [0,0,0],
                          [1,0,1]]

        Step 4: Handle first row/col (no change here)

        Final Output = [[1,0,1],
                        [0,0,0],
                        [1,0,1]]
        """

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows, cols = len(matrix), len(matrix[0])

        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Step 1: Mark zeros in first row/col
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 2: Apply marks to set cells
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 3: Handle first row
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Step 4: Handle first col
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0

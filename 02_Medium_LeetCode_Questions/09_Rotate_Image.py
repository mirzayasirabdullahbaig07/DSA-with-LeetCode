"""
        LEETCODE PROBLEM: 48. Rotate Image
        ----------------------------------

        QUESTION STATEMENT:
        -------------------
        You are given an n x n 2D matrix representing an image. 
        Rotate the image by 90 degrees (clockwise), in-place.
        - You must modify the matrix directly.
        - Do NOT allocate another 2D matrix.

        EXAMPLES:
        ---------
        Example 1:
        Input:  matrix = [[1,2,3],
                          [4,5,6],
                          [7,8,9]]
        Output: [[7,4,1],
                 [8,5,2],
                 [9,6,3]]

        Example 2:
        Input:  matrix = [[5,1,9,11],
                          [2,4,8,10],
                          [13,3,6,7],
                          [15,14,12,16]]
        Output: [[15,13,2,5],
                 [14,3,4,1],
                 [12,6,8,9],
                 [16,7,10,11]]

        CONSTRAINTS:
        ------------
        - n == matrix.length == matrix[i].length
        - 1 <= n <= 20
        - -1000 <= matrix[i][j] <= 1000

        APPROACH / TECHNIQUE:
        ---------------------
        We use the **Transpose + Reverse Rows** technique:
        1. **Transpose the matrix** (swap elements across the diagonal).
           - After this, rows become columns.
        2. **Reverse each row** to complete the clockwise 90° rotation.

        WHY THIS WORKS:
        ---------------
        - Transpose rearranges elements into their rotated positions (but mirrored).
        - Reversing rows fixes the mirror effect, giving the correct clockwise rotation.
        - Everything is done in-place with only swaps.

        TIME COMPLEXITY:
        ----------------
        - Transposing: O(n^2)
        - Reversing rows: O(n^2)
        - Total = O(n^2)

        SPACE COMPLEXITY:
        -----------------
        - O(1) (in-place, no extra matrix allocated).

        DRY RUN:
        --------
        Input: [[1,2,3],
                [4,5,6],
                [7,8,9]]

        Step 1: Transpose
                [[1,4,7],
                 [2,5,8],
                 [3,6,9]]

        Step 2: Reverse each row
                [[7,4,1],
                 [8,5,2],
                 [9,6,3]]

        Final Output = [[7,4,1],
                        [8,5,2],
                        [9,6,3]]
        """

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)

        # Step 1: Transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()

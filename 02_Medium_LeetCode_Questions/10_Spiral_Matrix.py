"""
LEETCODE PROBLEM: 54. Spiral Matrix
-----------------------------------

STATEMENT:
----------
Given an m x n matrix, return all elements of the matrix in spiral order.

EXAMPLES:
---------
Example 1:
Input:  [[1,2,3],
         [4,5,6],
         [7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:  [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

CONSTRAINTS:
------------
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100


TECHNIQUE / APPROACH:
----------------------
We use the **Boundary Simulation Method**:
1. Maintain 4 pointers: top, bottom, left, right.
   - top = 0 (first row index)
   - bottom = last row index
   - left = 0 (first column index)
   - right = last column index
2. Traverse in 4 directions:
   a) Left → Right across the top row, then increment `top`.
   b) Top → Bottom down the right column, then decrement `right`.
   c) Right → Left across the bottom row (if rows remain), then decrement `bottom`.
   d) Bottom → Top up the left column (if columns remain), then increment `left`.
3. Repeat until top > bottom OR left > right.


DRY RUN:
--------
Input: [[1,2,3],
        [4,5,6],
        [7,8,9]]

Initial boundaries: top=0, bottom=2, left=0, right=2

Step 1: Left → Right → [1,2,3], top=1
Step 2: Top → Bottom → [6,9], right=1
Step 3: Right → Left → [8,7], bottom=1
Step 4: Bottom → Top → [4], left=1
Step 5: Left → Right → [5], top=2 (stop as top > bottom)

Final Output = [1,2,3,6,9,8,7,4,5]


TIME COMPLEXITY:
----------------
- O(m * n) → Each element is visited exactly once.

SPACE COMPLEXITY:
-----------------
- O(1) → No extra space used (apart from result list).
"""


from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res
        
        # Define the boundaries
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # Traverse from left → right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            
            # Traverse from top → bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            # Traverse from right → left (if row remains)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            
            # Traverse from bottom → top (if column remains)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        
        return res

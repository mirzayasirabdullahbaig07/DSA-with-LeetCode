"""
LeetCode 1901: Find a Peak Element II
-------------------------------------

Problem Recap:
-----------------
You are given a 2D matrix `mat` of dimensions m x n.

A peak element is defined as an element mat[i][j] such that:
    - It is strictly greater than its top neighbor
    - It is strictly greater than its bottom neighbor
    - It is strictly greater than its left neighbor
    - It is strictly greater than its right neighbor

You must return [i, j] for any one such peak element.

Goal:
------
Design an algorithm that runs in O(m log n) or O(n log m) time.
"""

# =====================================================================
# 1. Brute Force Solution
# =====================================================================

"""
IDEA:
--------
- Check every cell in the matrix.
- For each cell, compare it with its 4 neighbors (up, down, left, right).
- If it is greater than all, return its coordinates.

This approach is simple but inefficient for large matrices.
"""

from typing import List

class SolutionBruteForce:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])

        # Traverse each cell in the matrix
        for i in range(rows):
            for j in range(cols):
                curr = mat[i][j]

                # Handle boundary conditions by assigning -1 where neighbor doesn't exist
                top = mat[i - 1][j] if i > 0 else -1
                bottom = mat[i + 1][j] if i < rows - 1 else -1
                left = mat[i][j - 1] if j > 0 else -1
                right = mat[i][j + 1] if j < cols - 1 else -1

                # Check if current element is greater than all 4 neighbors
                if curr > top and curr > bottom and curr > left and curr > right:
                    return [i, j]


"""
DRY RUN:
------------
mat = [[1, 4],
       [3, 2]]

i   j   curr  top  bottom  left  right  Is Peak?
0   0   1     -1   3       -1    4      No
0   1   4     -1   2       1     -1     Yes → [0, 1]

Output → [0, 1]

Time Complexity: O(m × n)
Space Complexity: O(1)
"""

# =====================================================================
# 2. Better Solution (Row-wise Maximum)
# =====================================================================

"""
IDEA:
--------
- For each row:
    - Find the maximum element (potential candidate for peak).
    - Check if it’s greater than the element directly above and below it.
    - If yes → return as the peak.

This reduces neighbor checks but still scans all rows linearly.
"""

class SolutionBetter:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        
        for i in range(rows):
            # Find index of the maximum element in current row
            max_col = mat[i].index(max(mat[i]))
            
            # Compare with top and bottom neighbors in the same column
            top = mat[i - 1][max_col] if i > 0 else -1
            bottom = mat[i + 1][max_col] if i < rows - 1 else -1
            
            if mat[i][max_col] > top and mat[i][max_col] > bottom:
                return [i, max_col]


"""
DRY RUN:
------------
mat = [[1, 4],
       [3, 2]]

Row 0 → max = 4 at col = 1
top = -1, bottom = 2
4 > -1 and 4 > 2 → Peak found

Output → [0, 1]

Time Complexity: O(m × n)
Space Complexity: O(1)
"""

# =====================================================================
# 3. Optimal Solution (Binary Search on Columns)
# =====================================================================

"""
IDEA:
--------
We can optimize further using Binary Search on columns.

Key Intuition:
--------------
- In each iteration, pick the middle column.
- Find the maximum element in that column (row index = max_row).
- Compare it with its left and right neighbors.
    - If greater than both → it’s a peak.
    - If left neighbor is greater → move to left half.
    - If right neighbor is greater → move to right half.
- Continue until a peak is found.

This gives O(m log n) complexity.
"""

class SolutionOptimal:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        
        left, right = 0, cols - 1  # Binary search boundaries
        
        while left <= right:
            mid = (left + right) // 2  # Middle column
            
            # Find row index of the maximum element in the middle column
            max_row = 0
            for i in range(rows):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i
            
            # Fetch left and right neighbor values safely (boundary check)
            left_val = mat[max_row][mid - 1] if mid - 1 >= 0 else -1
            right_val = mat[max_row][mid + 1] if mid + 1 < cols else -1
            curr_val = mat[max_row][mid]
            
            # Check if current element is peak
            if curr_val > left_val and curr_val > right_val:
                return [max_row, mid]
            
            # Move towards the greater neighbor direction
            elif left_val > curr_val:
                right = mid - 1
            else:
                left = mid + 1


"""
DRY RUN:
------------
mat = [[10,20,15],
       [21,30,14],
       [7,16,32]]

Step 1:
left = 0, right = 2 → mid = 1
Column 1 = [20, 30, 16]
max_row = 1 (element = 30)
left_val = 21, right_val = 14
30 > 21 and 30 > 14 → Peak found

Output → [1, 1]

Time Complexity: O(m log n)
Space Complexity: O(1)
"""

# =====================================================================
# SUMMARY TABLE
# =====================================================================

"""
Approach            Time Complexity    Space Complexity     Explanation
-------------------------------------------------------------------------------
Brute Force         O(m × n)           O(1)                 Check all neighbors
Better              O(m × n)           O(1)                 Row-wise max comparison
Optimal             O(m log n)         O(1)                 Binary search on columns

Notes:
---------
- Brute Force → easiest to understand; good for small inputs.
- Better → fewer comparisons but still linear.
- Optimal → ideal for large matrices; uses binary search pattern.

Optional:
------------
You can also implement the O(n log m) variant (binary search on rows) — it’s symmetric logic.
"""

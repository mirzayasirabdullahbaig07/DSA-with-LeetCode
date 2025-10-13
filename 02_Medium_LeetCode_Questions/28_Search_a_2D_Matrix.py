"""
Problem: 74. Search a 2D Matrix
---------------------------------------
You are given an m x n matrix that follows two important properties:
1) Each row is sorted in ascending (non-decreasing) order.
2) The first element of each row is greater than the last element of the previous row.

Task:
Given an integer `target`, return True if `target` exists in the matrix, otherwise False.

---------------------------------------
Example:
---------------------------------------
Input:
matrix = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
]
target = 3

Output: True

Explanation:
Target 3 exists in the first row at position (0,1).

---------------------------------------
Intuition
---------------------------------------
Because the entire matrix is sorted in a special way (each row is sorted and the next row starts with a larger number),
we can treat the 2D matrix as a flattened sorted 1D array of size m * n.

Example:
matrix = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
]

Flattened view = [1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]

We can now apply binary search on this 1D sequence without physically flattening the matrix.

---------------------------------------
Approaches Overview
---------------------------------------
1) Brute Force: Scan every element → O(m * n)
2) Better: Binary search each row → O(m * log n)
3) Optimal: Treat as 1D sorted array → O(log(m * n))
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Optimal Binary Search Solution
        ---------------------------------------
        Uses binary search over the virtual 1D representation of the 2D matrix.
        """
        # Step 1: Handle empty matrix case
        if not matrix or not matrix[0]:
            return False

        # Step 2: Get matrix dimensions
        m, n = len(matrix), len(matrix[0])

        # Step 3: Set binary search boundaries
        left, right = 0, m * n - 1  # Treat entire matrix as a 1D array

        # Step 4: Binary search loop
        while left <= right:
            mid = (left + right) // 2

            # Convert 1D index → 2D coordinates
            row = mid // n
            col = mid % n
            mid_val = matrix[row][col]

            # Step 5: Check if mid value matches target
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        # Step 6: Target not found
        return False


"""
---------------------------------------
Dry Run Example
---------------------------------------
matrix = [
 [1, 3, 5, 7],
 [10, 11, 16, 20],
 [23, 30, 34, 60]
]
target = 16

m = 3, n = 4 → total elements = 12
left = 0, right = 11

Step | left | right | mid | mid_val | row | col | Action
-----|-------|--------|-----|---------|-----|-----|-----------------
 1   | 0     | 11     | 5   | 11      | 1   | 1   | 11 < 16 → move right
 2   | 6     | 11     | 8   | 23      | 2   | 0   | 23 > 16 → move left
 3   | 6     | 7      | 6   | 16      | 1   | 2   | Found target

Return True

---------------------------------------
Time and Space Complexity Analysis
---------------------------------------
We perform a single binary search across m * n elements.
Each step halves the search space.

Time Complexity:  O(log(m * n))
Space Complexity: O(1)  (no extra space used)

---------------------------------------
Edge Cases
---------------------------------------
1) Empty matrix → return False
2) Target smaller than smallest element → False
3) Target larger than largest element → False
4) Target exists in the first or last cell → True

---------------------------------------
Alternative Approaches
---------------------------------------

1) Brute Force: Linear Search
---------------------------------------
Check each element one by one.
Simple, but inefficient.

Code:
for row in matrix:
    for val in row:
        if val == target:
            return True
return False

Time:  O(m * n)
Space: O(1)

---------------------------------------

2) Better Approach: Row-wise Binary Search
---------------------------------------
Perform binary search in each row individually.
Stop early if target found.

Code:
for row in matrix:
    if row[0] <= target <= row[-1]:
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
return False

Time:  O(m * log n)
Space: O(1)

---------------------------------------

3) Optimal: Treat Matrix as Flattened Sorted Array
---------------------------------------
Time:  O(log(m * n))
Space: O(1)
Best for interview and production-level implementation.

---------------------------------------
Summary
---------------------------------------
Approach                 | Time         | Space | Notes
--------------------------|--------------|--------|----------------------------
Brute Force               | O(m * n)     | O(1)  | Simple but slow
Row-wise Binary Search    | O(m * log n) | O(1)  | Better if rows are sorted
Flattened Binary Search   | O(log(m*n))  | O(1)  | Optimal and elegant

---------------------------------------
Why It Works:
---------------------------------------
The “matrix ordering” ensures that elements are sorted globally.
Binary search can treat the entire 2D grid as a continuous 1D list.
The conversion from index → coordinates via (row = mid // n, col = mid % n)
ensures correct mapping without extra space.

---------------------------------------
Conclusion:
---------------------------------------
This approach demonstrates how to transform a 2D search problem into
a 1D binary search using mathematical mapping, achieving optimal efficiency.
"""

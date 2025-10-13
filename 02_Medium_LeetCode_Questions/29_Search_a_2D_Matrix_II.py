"""
Problem: 240. Search a 2D Matrix II
---------------------------------------
You are given an m x n integer matrix `matrix` with the following properties:

1) Each row is sorted in ascending order (left to right).
2) Each column is sorted in ascending order (top to bottom).

Task:
Given an integer `target`, return True if `target` exists in the matrix, otherwise False.

---------------------------------------
Example:
---------------------------------------
Input:
matrix = [
  [1, 4, 7, 11, 15],
  [2, 5, 8, 12, 19],
  [3, 6, 9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5

Output: True

Explanation:
5 exists at position (1,1).

---------------------------------------
Intuition:
---------------------------------------
The matrix is sorted both row-wise and column-wise.
If we start searching from the top-right corner:

- If the current element is greater than the target, we move LEFT (because all elements below are larger).
- If the current element is smaller than the target, we move DOWN (because all elements to the left are smaller).

This allows us to eliminate one row or one column in every step efficiently.

---------------------------------------
Approaches Overview:
---------------------------------------
1) Brute Force → O(m * n)
2) Better (Row-wise Binary Search) → O(m * log n)
3) Optimal (Start from top-right corner) → O(m + n)
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Optimal Solution
        ---------------------------------------
        Uses the "Top-Right Corner Elimination" approach.
        Eliminates one row or column in every step.
        """
        # Step 1: Get matrix dimensions
        rows = len(matrix)
        cols = len(matrix[0])

        # Step 2: Start from top-right corner
        row = 0
        col = cols - 1

        # Step 3: Traverse matrix until out of bounds
        while row < rows and col >= 0:
            current = matrix[row][col]

            if current == target:
                return True  # Target found
            elif current > target:
                col -= 1  # Move left (eliminate one column)
            else:
                row += 1  # Move down (eliminate one row)

        # Step 4: Target not found
        return False


"""
---------------------------------------
Dry Run Example
---------------------------------------
matrix = [
 [1, 4, 7, 11, 15],
 [2, 5, 8, 12, 19],
 [3, 6, 9, 16, 22],
 [10, 13, 14, 17, 24],
 [18, 21, 23, 26, 30]
]
target = 16

rows = 5, cols = 5
Start: row = 0, col = 4 → current = 15

Step | row | col | current | Action
-----|------|------|----------|--------------------------
 1   | 0    | 4    | 15       | 15 < 16 → move down
 2   | 1    | 4    | 19       | 19 > 16 → move left
 3   | 1    | 3    | 12       | 12 < 16 → move down
 4   | 2    | 3    | 16       | Found target ✅

Return True

---------------------------------------
Time and Space Complexity
---------------------------------------
- In each iteration, we move either one step left or one step down.
- We can take at most (m + n) steps before going out of bounds.

Time Complexity:  O(m + n)
Space Complexity: O(1)

---------------------------------------
Edge Cases
---------------------------------------
1) Empty matrix → return False
2) Single row or column → handled naturally
3) Target smaller than smallest element → False
4) Target larger than largest element → False
5) Target at corner positions → Works correctly

---------------------------------------
Alternative Approaches
---------------------------------------

1) Brute Force: Linear Search
---------------------------------------
Check every element one by one.

Code:
for row in matrix:
    for val in row:
        if val == target:
            return True
return False

Time:  O(m * n)
Space: O(1)

---------------------------------------

2) Better: Row-wise Binary Search
---------------------------------------
Each row is sorted → perform binary search per row.

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

3) Optimal: Top-Right Corner Search
---------------------------------------
Start from top-right corner:
- Move left if current > target
- Move down if current < target

This eliminates one row or one column in each step.

Time:  O(m + n)
Space: O(1)
Best for large matrices (m, n up to 300)

---------------------------------------
Summary:
---------------------------------------
Approach                 | Time         | Space | Notes
--------------------------|--------------|--------|----------------------------
Brute Force               | O(m * n)     | O(1)  | Simple but inefficient
Row-wise Binary Search    | O(m * log n) | O(1)  | Faster if rows are sorted
Top-Right Search (Optimal)| O(m + n)     | O(1)  | Elegant and efficient

---------------------------------------
Why It Works:
---------------------------------------
Because each row and column are sorted:
- Moving left decreases values
- Moving down increases values
Thus, we can discard one full row or column each step,
leading to an efficient O(m + n) search.

---------------------------------------
Conclusion:
---------------------------------------
This problem demonstrates how understanding data structure patterns
(such as sorted rows and columns) allows us to reduce complexity from
O(m * n) to O(m + n) using a logical elimination strategy.
"""

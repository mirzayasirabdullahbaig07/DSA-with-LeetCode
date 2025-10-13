"""
🧠 Problem:
---------
Given an m x n binary matrix `mat`, find the row that contains the **maximum count of ones**.
Return an array containing two values:
    [index_of_row_with_max_ones, number_of_ones_in_that_row]

If multiple rows have the same maximum number of ones,
return the one with the smallest index.

---------------------------------------
📘 Example:
---------------------------------------
Input:  mat = [[0,1],
               [1,0]]

Output: [0, 1]
Explanation:
- Row 0 has 1 one → count = 1
- Row 1 has 1 one → count = 1
→ Both rows tie, so choose smaller index → 0

---------------------------------------
💡 Brute Force Approach (Your Code)
---------------------------------------
- For each row:
    → Count number of ones using `sum(row)`
    → Track the row with maximum ones
- If two rows have the same number of ones, keep the smaller index.

---------------------------------------
⚙️ Code Implementation
---------------------------------------
"""

from typing import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = -1
        row_index = -1
        
        # Step 1: Iterate through each row
        for i, row in enumerate(mat):
            ones_count = sum(row)  # Step 2: Count ones using Python’s sum()
            
            # Step 3: Update max if current row has more ones
            if ones_count > max_ones:
                max_ones = ones_count
                row_index = i
        
        # Step 4: Return the row index and number of ones
        return [row_index, max_ones]

"""
---------------------------------------
🧩 Dry Run Example
---------------------------------------
Input: mat = [[0,0,0],
              [0,1,1]]

Initial:
max_ones = -1
row_index = -1

Iteration 1 → i = 0, row = [0,0,0]
→ ones_count = sum([0,0,0]) = 0
→ 0 > -1 → update max_ones = 0, row_index = 0

Iteration 2 → i = 1, row = [0,1,1]
→ ones_count = sum([0,1,1]) = 2
→ 2 > 0 → update max_ones = 2, row_index = 1

End:
Return [1, 2]
✅ Output = [1, 2]

---------------------------------------
⏱️ Time Complexity:
---------------------------------------
For each row (m rows):
→ Counting ones using sum(row) takes O(n)
So total = O(m × n)

Space Complexity: O(1)
→ We only use a few extra variables.

---------------------------------------
⚡ Better Approach (Using Binary Search)
---------------------------------------
If each row is sorted (0s then 1s), we can find the first 1 using binary search.

Steps:
1. For each row, apply binary search to find index of first 1.
2. Number of ones = total_columns - first_one_index
3. Keep track of max.

Code:
"""

class SolutionBinarySearch:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = -1
        row_index = -1
        n = len(mat[0])

        for i, row in enumerate(mat):
            left, right = 0, n - 1
            first_one_index = n  # Default: assume no 1 found

            # Binary search for first 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == 1:
                    first_one_index = mid
                    right = mid - 1
                else:
                    left = mid + 1

            count_ones = n - first_one_index

            if count_ones > max_ones:
                max_ones = count_ones
                row_index = i

        return [row_index, max_ones]

"""
⏱️ Time Complexity: O(m × log n)
Space Complexity: O(1)

---------------------------------------
🚀 Optimal Approach (Top-Right Corner Method)
---------------------------------------
Intuition:
Since each row is sorted (0s → 1s),
we can start from the top-right corner of the matrix and move:
- Left if we see 1 (to count more 1s)
- Down if we see 0 (go to next row)

This way we only traverse m + n cells in total.

Code:
"""

class SolutionOptimal:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        row = 0
        col = n - 1
        max_row = -1
        max_ones = 0

        while row < m and col >= 0:
            if mat[row][col] == 1:
                max_row = row
                max_ones = n - col
                col -= 1  # move left
            else:
                row += 1  # move down

        return [max_row if max_row != -1 else 0, max_ones]

"""
---------------------------------------
⏱️ Time Complexity: O(m + n)
Space Complexity: O(1)

---------------------------------------
✅ Summary
---------------------------------------
Approach            | Time       | Space | Notes
--------------------|------------|--------|---------------------------
Brute Force (sum)   | O(m × n)   | O(1)  | Easy and clean
Binary Search       | O(m × log n) | O(1) | Works if rows sorted
Top-right Pointer   | O(m + n)   | O(1)  | Fastest, optimal

---------------------------------------
🧠 Intuition Recap:
---------------------------------------
- Brute force counts 1s directly → simplest
- Binary search leverages sorting to find 1s faster
- Top-right corner traversal leverages matrix structure fully
→ making it optimal for sorted binary matrices
"""

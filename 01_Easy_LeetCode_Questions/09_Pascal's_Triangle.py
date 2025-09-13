"""
LEETCODE PROBLEM: 118. Pascal's Triangle
----------------------------------------

STATEMENT:
----------
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle:
- Each number is the sum of the two numbers directly above it.
- The first and last number of each row is always 1.

EXAMPLES:
---------
Example 1:
Input:  numRows = 5
Output: [[1],
         [1,1],
         [1,2,1],
         [1,3,3,1],
         [1,4,6,4,1]]

Example 2:
Input:  numRows = 1
Output: [[1]]

CONSTRAINTS:
------------
- 1 <= numRows <= 30


TECHNIQUE / APPROACH:
----------------------
We use **Dynamic Programming (DP) construction**:
1. Start with the first row as [1].
2. Each row begins and ends with 1.
3. For the inner elements: 
   - row[j] = prev_row[j-1] + prev_row[j]
4. Append each row to the triangle until numRows is built.


DRY RUN:
--------
numRows = 5

Row 1: [1]
Row 2: [1,1]
Row 3: [1, (1+1)=2, 1] → [1,2,1]
Row 4: [1, (1+2)=3, (2+1)=3, 1] → [1,3,3,1]
Row 5: [1, (1+3)=4, (3+3)=6, (3+1)=4, 1] → [1,4,6,4,1]

Final Output:
[[1],
 [1,1],
 [1,2,1],
 [1,3,3,1],
 [1,4,6,4,1]]


TIME COMPLEXITY:
----------------
- O(numRows^2) → Each row builds using previous row’s elements.

SPACE COMPLEXITY:
-----------------
- O(numRows^2) → Result list storing all rows.
"""


from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            # Start each row with 1s
            row = [1] * (i + 1)
            
            # Fill inner values using previous row
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            
            triangle.append(row)
        
        return triangle

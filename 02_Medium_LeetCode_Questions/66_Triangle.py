"""
PROBLEM SUMMARY:
We are given a triangle (list of lists), where each row has one more element 
than the previous. Starting at the top, we must move to the bottom by choosing 
adjacent numbers in the next row (i.e., from index j we can move to j or j+1). 
We must find the minimum possible sum of such a path.

----------------------------------------------------
EXPLANATION (BOTTOM-UP DYNAMIC PROGRAMMING, O(n) SPACE):
----------------------------------------------------

1. The idea: 
   Instead of computing from top → bottom (which causes overlapping subproblems), 
   we compute from bottom → top. For every cell, the minimum path from that cell 
   downward is:
   
       triangle[i][j] + min(down, down-right)
   
   Where:
       down       = dp[j]
       down-right = dp[j+1]

2. dp array:
   We use a 1-D dp array that initially equals the last row of the triangle.
   Why? Because the last row already represents the minimum path sums 
   if you start at that row.

3. Transition:
   For each row above the last, update dp[j] as:

       dp[j] = triangle[i][j] + min(dp[j], dp[j+1])

   After processing the entire row, dp will represent the minimum path values 
   starting from that row.

4. Final answer:
   After we reach the top row, dp[0] will contain the minimum path sum 
   from the top of the triangle to the bottom.

----------------------------------------------------
TIME COMPLEXITY:
    O(n^2) — because we visit each cell once.
SPACE COMPLEXITY:
    O(n)   — using a single list the size of the bottom row.
----------------------------------------------------
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        # dp initially is the last row
        dp = triangle[-1].copy()
        
        # Build from second last row upward
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        
        return dp[0]

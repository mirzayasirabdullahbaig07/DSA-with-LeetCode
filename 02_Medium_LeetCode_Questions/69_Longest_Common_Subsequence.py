"""
LeetCode 1143: Longest Common Subsequence (LCS)
----------------------------------------------

Problem Summary:
Given two strings `text1` and `text2`, return the length of their
longest common subsequence (LCS).
A subsequence is formed by deleting characters without changing
the relative order of the remaining characters.

Key Idea:
- If two characters match, they can be part of the LCS.
- If they do not match, we must decide which character to ignore
  to maximize the LCS length.

Dynamic Programming Approach:

We define a DP table where:
    dp[i][j] = length of the longest common subsequence between
               text1[:i] and text2[:j]

DP Table Dimensions:
- (n + 1) x (m + 1), where:
    n = len(text1)
    m = len(text2)
- Extra row and column represent empty prefixes.

Base Case:
- dp[0][j] = 0 for all j (empty text1)
- dp[i][0] = 0 for all i (empty text2)
- An empty string has LCS length 0 with any string.

State Transition:
- If the current characters match:
      text1[i - 1] == text2[j - 1]
  then we extend the LCS by 1:
      dp[i][j] = 1 + dp[i - 1][j - 1]

- If the characters do not match:
  we take the maximum LCS length obtained by:
      - ignoring the current character from text1
      - ignoring the current character from text2
  hence:
      dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

Iteration Order:
- Fill the table row by row, from top-left to bottom-right.
- This ensures all required subproblems are already solved.

Final Answer:
- dp[n][m] contains the length of the longest common subsequence
  between the full strings text1 and text2.

Time Complexity:
- O(n * m), where n and m are the lengths of the two strings.

Space Complexity:
- O(n * m) due to the DP table.

Why This Works:
- The problem exhibits optimal substructure:
  the LCS of two strings depends on the LCS of their prefixes.
- Overlapping subproblems make dynamic programming the optimal choice.

Key Technique Used:
- Dynamic Programming (2D DP table)
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        
        # dp[i][j] = LCS length of text1[:i] and text2[:j]
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[n][m]

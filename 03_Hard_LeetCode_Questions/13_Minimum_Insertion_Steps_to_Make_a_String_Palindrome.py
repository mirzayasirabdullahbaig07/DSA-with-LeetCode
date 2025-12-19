"""
Problem:
--------
We are given a string `s`. In one step, we can insert any character at any index.
Our goal is to find the minimum number of insertions required to make the string
a palindrome (a string that reads the same forward and backward).

Key Insight:
------------
Instead of directly simulating insertions, we observe that:
- If we keep the longest part of the string that is already palindromic,
  we only need to insert characters for the remaining part.
- The Longest Palindromic Subsequence (LPS) tells us the maximum number of
  characters that can stay in place without breaking the palindrome.

Important Trick:
----------------
The Longest Palindromic Subsequence (LPS) of a string is equal to the
Longest Common Subsequence (LCS) between the string and its reverse.

So:
Minimum Insertions = len(s) - LPS

Technique Used:
---------------
Dynamic Programming (DP)
- We use DP to compute the Longest Common Subsequence (LCS).
- dp[i][j] represents the LCS length between the first i characters of `text1`
  and the first j characters of `text2`.

Algorithm Steps:
----------------
1. Reverse the given string `s`.
2. Compute LCS between `s` and its reversed string using DP.
3. Subtract the LCS length from the original string length.
4. The result is the minimum number of insertions needed.

Time Complexity:
----------------
O(n^2)
- We fill a DP table of size (n + 1) x (n + 1).

Space Complexity:
-----------------
O(n^2)
- We store the DP table for LCS computation.

Where:
------
n = length of the string `s`
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]

    def minInsertions(self, s: str) -> int:
        rev = s[::-1]
        lps = self.longestCommonSubsequence(s, rev)
        return len(s) - lps

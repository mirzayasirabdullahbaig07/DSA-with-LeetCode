"""
PROBLEM:
---------
Given a string `s`, find the length of the Longest Palindromic Subsequence (LPS).

A subsequence is formed by deleting some (or no) characters from the string
without changing the order of the remaining characters.

A palindrome is a string that reads the same forward and backward.

Example:
Input:  "bbbab"
Output: 4
Explanation: "bbbb" is a valid palindromic subsequence.


TECHNIQUE USED:
----------------
Dynamic Programming using Longest Common Subsequence (LCS)

Key Insight:
A palindrome remains the same when reversed.
So, the Longest Palindromic Subsequence of a string `s`
is equal to the Longest Common Subsequence between:
    - the original string `s`
    - the reversed string `s[::-1]`

Therefore:
LPS(s) = LCS(s, reverse(s))


APPROACH:
----------
1. Reverse the input string.
2. Compute the Longest Common Subsequence (LCS) between the original
   string and the reversed string using Dynamic Programming.
3. The final LCS length is the answer.


TIME COMPLEXITY:
-----------------
Let n be the length of the string.

- We fill an n x n DP table
- Time Complexity: O(n²)


SPACE COMPLEXITY:
------------------
- DP table of size (n+1) x (n+1)
- Space Complexity: O(n²)


CODE:
------
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        # DP table where dp[i][j] stores LCS length
        # for text1[0..i-1] and text2[0..j-1]
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]

    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestCommonSubsequence(s, s[::-1])

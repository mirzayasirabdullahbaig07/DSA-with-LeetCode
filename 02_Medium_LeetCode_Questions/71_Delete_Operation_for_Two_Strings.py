"""
Problem: 583. Delete Operation for Two Strings
------------------------------------------------

Given two strings word1 and word2, the goal is to determine the
minimum number of delete operations required to make both strings
exactly the same.

In one operation, we can delete exactly one character from either
string.


Core Idea
---------
The optimal way to make both strings equal is to keep their
Longest Common Subsequence (LCS) and delete all other characters.

The LCS is the longest sequence of characters that appears in both
strings in the same relative order (not necessarily contiguous).

Any character that is not part of the LCS must be deleted.


Why LCS Works
-------------
If LCS length is L:
- word1 has (len(word1) - L) extra characters to delete
- word2 has (len(word2) - L) extra characters to delete

So, the total minimum deletions required are:
    (len(word1) - L) + (len(word2) - L)


Technique Used
--------------
Dynamic Programming (DP)

This problem has:
- Overlapping subproblems
- Optimal substructure

Hence, DP is the most efficient approach.


Algorithm Used
--------------
Algorithm: Longest Common Subsequence (LCS)

We define a DP table:
    dp[i][j] = length of LCS between
               word1[0 ... i-1] and word2[0 ... j-1]

Transition rules:
1. If characters match:
       dp[i][j] = dp[i-1][j-1] + 1
2. If characters do not match:
       dp[i][j] = max(dp[i-1][j], dp[i][j-1])

The value dp[n][m] gives the length of the LCS.


Time and Space Complexity
-------------------------
Let:
    n = length of word1
    m = length of word2

Time Complexity:
    O(n * m)

Space Complexity:
    O(n * m)


Final Result
------------
After computing the LCS, the minimum number of delete operations
required to make both strings the same is:

    (n - LCS) + (m - LCS)
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        lcs = dp[n][m]
        return (n - lcs) + (m - lcs)

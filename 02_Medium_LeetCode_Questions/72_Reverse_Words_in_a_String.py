"""
LeetCode 151: Reverse Words in a String

Problem Statement:
------------------
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.

The returned string should:
- Contain words in reverse order
- Have only a single space between words
- Not contain leading or trailing spaces

Example 1:
----------
Input:  s = "the sky is blue"
Output: "blue is sky the"

Example 2:
----------
Input:  s = "  hello world  "
Output: "world hello"

Example 3:
----------
Input:  s = "a good   example"
Output: "example good a"

Constraints:
------------
1 <= s.length <= 10^4
s contains English letters, digits, and spaces
There is at least one word in s

Approach Used:
--------------
1. Split the string using `split()`, which automatically removes:
   - Leading spaces
   - Trailing spaces
   - Extra spaces between words
2. Reverse the list of words
3. Join the words back together using a single space
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Split the string by whitespace (handles extra spaces)
        words = s.split()
        
        # Step 2: Reverse the list of words
        words.reverse()
        
        # Step 3: Join the words with a single space
        return " ".join(words)

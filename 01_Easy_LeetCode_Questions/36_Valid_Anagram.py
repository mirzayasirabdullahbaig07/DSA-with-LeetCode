"""
LeetCode 242. Valid Anagram

QUESTION EXPLANATION:
---------------------
You are given two strings `s` and `t`.

Your task is to return True if `t` is an anagram of `s`,
otherwise return False.

An anagram means:
- Both strings must contain the same characters
- Each character must appear the same number of times
- Order of characters does NOT matter

Examples:
----------
s = "anagram", t = "nagaram"  -> True
s = "rat", t = "car"          -> False

Constraints:
------------
- Length of s and t can be up to 50,000
- Only lowercase English letters are used
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        APPROACH:
        ---------
        1. If the lengths of the two strings are different,
           they cannot be anagrams.
        2. Count how many times each character appears in `s`
           using a dictionary.
        3. Go through each character in `t` and reduce the count.
        4. If a character does not exist or count goes below zero,
           return False.
        5. If all checks pass, return True.
        """

        # Step 1: If lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False

        # Step 2: Dictionary to store character counts from string s
        chars = {}

        # Count each character in s
        for ch in s:
            chars[ch] = chars.get(ch, 0) + 1

        # Step 3: Check characters in t
        for ch in t:
            # If character not found in dictionary, not an anagram
            if ch not in chars:
                return False
            else:
                # If count is already zero, extra character exists
                if chars[ch] == 0:
                    return False
                # Decrease count for matched character
                chars[ch] -= 1

        # Step 4: If all characters matched correctly
        return True

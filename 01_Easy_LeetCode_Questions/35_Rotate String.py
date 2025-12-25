"""
LeetCode 796: Rotate String

Problem Statement:
------------------
Given two strings s and goal, return True if and only if s can become goal
after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost
position.

Example:
---------
Input:  s = "abcde", goal = "cdeab"
Output: True

Input:  s = "abcde", goal = "abced"
Output: False

Constraints:
------------
1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.


Approach / Technique Used:
--------------------------
String Rotation using Concatenation + Substring Search

This approach is based on the observation that:
If a string 'goal' is a rotation of string 's', then 'goal' must appear as a
substring within 's + s'.

Example:
---------
s = "abcde"
s + s = "abcdeabcde"

All possible rotations of "abcde" appear as substrings in "abcdeabcde":
"abcde", "bcdea", "cdeab", "deabc", "eabcd"

So, checking whether 'goal' exists inside 's + s' confirms rotation.


Algorithm Steps:
----------------
1. Check if lengths of s and goal are equal.
   - If not equal, rotation is impossible → return False.

2. Concatenate s with itself.
   - This creates a string containing all possible rotations of s.

3. Check if goal is a substring of the concatenated string.
   - If yes → return True
   - Otherwise → return False


Why This Works:
---------------
A rotation does not change the length or characters of a string,
only their order.

By duplicating the string (s + s), every possible left-rotation of s
appears exactly once as a continuous substring.

This avoids manually rotating the string multiple times and is
more efficient and cleaner.


Time Complexity:
----------------
Let n = length of string s

1. Length comparison → O(1)
2. String concatenation (s + s) → O(n)
3. Substring check (goal in double_s) → O(n)

Overall Time Complexity:
------------------------
O(n)

This is optimal for this problem.


Space Complexity:
-----------------
1. Extra space for concatenated string (s + s) → O(n)

Overall Space Complexity:
-------------------------
O(n)


Key Concepts Used:
-----------------
- String manipulation
- String concatenation
- Substring search
- Pattern matching logic

No advanced algorithms (like KMP) are required here because Python's
substring search is already optimized.


Interview Tip:
--------------
This solution is preferred in interviews because:
- It is simple
- It is optimal
- It avoids unnecessary loops
- It demonstrates strong string intuition
"""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Step 1: If lengths are not equal, rotation is impossible
        if len(s) != len(goal):
            return False
        
        # Step 2: Concatenate the string with itself
        double_s = s + s
        
        # Step 3: Check if goal is a substring of double_s
        return goal in double_s

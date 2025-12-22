"""
Problem: 1021. Remove Outermost Parentheses

Explanation:
-------------
We are given a valid parentheses string `s` made of '(' and ')'.
The string consists of one or more primitive parentheses strings.

A primitive parentheses string:
- Is non-empty
- Cannot be split into two smaller valid parentheses strings

Goal:
-----
For each primitive substring, remove its outermost '(' and ')',
then concatenate the remaining parts and return the result.

Approach:
---------
We use a counter to track the current depth of parentheses.

- When we see '(':
    - If depth > 0, it is NOT an outermost '(' → keep it
    - Increase depth

- When we see ')':
    - Decrease depth first
    - If depth > 0, it is NOT an outermost ')' → keep it

This works because:
- Outermost '(' appears when depth == 0
- Outermost ')' appears when depth becomes 0 after decrement

We skip those outermost parentheses and keep all inner ones.

Data Structures Used:
---------------------
- List `result` to efficiently build the output string
- Integer `count` to track parentheses depth

Time Complexity:
----------------
O(n) — each character in the string is processed once

Space Complexity:
-----------------
O(n) — extra space used to store the resulting characters
"""

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []   # Stores the final characters
        count = 0     # Tracks the current depth of parentheses

        for ch in s:
            if ch == '(':
                # If depth > 0, this '(' is not outermost
                if count > 0:
                    result.append(ch)
                count += 1
            else:  # ch == ')'
                count -= 1
                # If depth > 0 after decrement, this ')' is not outermost
                if count > 0:
                    result.append(ch)

        return "".join(result)

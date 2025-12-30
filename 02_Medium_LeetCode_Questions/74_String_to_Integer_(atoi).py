"""
LeetCode 8: String to Integer (atoi)

PROBLEM STATEMENT:
------------------
Implement the function myAtoi(string s), which converts a string into
a 32-bit signed integer.

The conversion follows these rules:

1. WHITESPACE:
   Ignore any leading whitespace characters (' ').

2. SIGN:
   Check if the next character is '+' or '-'.
   - '+' means positive
   - '-' means negative
   If neither is present, assume the number is positive.

3. CONVERSION:
   Read characters while they are digits (0–9).
   - Ignore leading zeros
   - Stop reading when a non-digit character appears
   - If no digits are read, return 0

4. ROUNDING (CLAMPING):
   The integer must stay within the 32-bit signed integer range:
       INT_MIN = -2^31
       INT_MAX =  2^31 - 1
   - If the number is smaller than INT_MIN → return INT_MIN
   - If the number is larger than INT_MAX → return INT_MAX

EXAMPLES:
---------
Input: "42"           → Output: 42
Input: " -042"        → Output: -42
Input: "1337c0d3"     → Output: 1337
Input: "0-1"          → Output: 0
Input: "words and 987"→ Output: 0

APPROACH:
---------
1. Use an index to traverse the string.
2. Skip all leading spaces.
3. Detect sign (+ or -).
4. Convert digit characters into an integer.
5. Handle overflow while building the number.
6. Return the final value multiplied by the sign.

WHY THIS WORKS:
---------------
- We process the string only once → O(n) time
- No extra memory used → O(1) space
- Overflow is handled immediately during conversion

TIME & SPACE COMPLEXITY:
------------------------
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        n = len(s)
        index = 0
        sign = 1
        result = 0

        # 1. Skip leading whitespace
        while index < n and s[index] == ' ':
            index += 1

        # 2. Handle optional sign
        if index < n:
            if s[index] == '+':
                index += 1
            elif s[index] == '-':
                sign = -1
                index += 1

        # 3. Convert digits to integer
        while index < n and s[index].isdigit():
            digit = ord(s[index]) - ord('0')
            result = result * 10 + digit

            # 4. Handle overflow
            if sign == 1 and result > INT_MAX:
                return INT_MAX
            if sign == -1 and result > -INT_MIN:
                return INT_MIN

            index += 1

        return sign * result

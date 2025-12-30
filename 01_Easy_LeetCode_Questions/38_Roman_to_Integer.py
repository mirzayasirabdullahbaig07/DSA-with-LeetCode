"""
LeetCode 13: Roman to Integer

PROBLEM EXPLANATION:
--------------------
Roman numerals are represented using seven symbols:

I  = 1
V  = 5
X  = 10
L  = 50
C  = 100
D  = 500
M  = 1000

Normally, Roman numerals are written from left to right in decreasing order.
Example:
    "XII" = 10 + 1 + 1 = 12

SPECIAL RULE (SUBTRACTION CASE):
--------------------------------
If a smaller value appears before a larger value, we subtract it.

Valid subtraction pairs:
I before V or X   → 4, 9
X before L or C   → 40, 90
C before D or M   → 400, 900

Example:
    "IV"  = 5 - 1 = 4
    "IX"  = 10 - 1 = 9
    "MCMXCIV" = 1000 + (1000 - 100) + (100 - 10) + (5 - 1) = 1994

APPROACH:
---------
1. Store Roman symbol values in a dictionary.
2. Traverse the string from left to right.
3. Compare the current symbol with the next symbol:
   - If current < next → subtract current value.
   - Else → add current value.
4. Return the final result.

WHY THIS WORKS:
---------------
Roman numerals only allow subtraction in specific cases.
By checking the next character, we correctly decide whether
to add or subtract the current value.

TIME & SPACE COMPLEXITY:
------------------------
Time Complexity: O(n)
Space Complexity: O(1)
(where n is the length of the Roman numeral string)
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        n = len(s)

        for i in range(n):
            # If the current symbol is smaller than the next one,
            # subtract its value
            if i < n - 1 and values[s[i]] < values[s[i + 1]]:
                result -= values[s[i]]
            else:
                result += values[s[i]]


        return result

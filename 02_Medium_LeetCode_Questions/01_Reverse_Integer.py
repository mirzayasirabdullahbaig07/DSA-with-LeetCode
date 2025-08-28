"""
Problem:
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer
range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers.

Examples:
Input: x = 123       → Output: 321
Input: x = -123      → Output: -321
Input: x = 120       → Output: 21

Constraints:
-2^31 <= x <= 2^31 - 1
"""

class Solution:
    def reverse(self, x: int) -> int:
        """
        Step-by-step solution:
        1. Define the 32-bit integer range (INT_MIN, INT_MAX).
        2. Extract the sign (negative or positive).
        3. Work with absolute value of x for simplicity.
        4. Reverse the digits mathematically (no string conversion).
        5. Reapply the original sign.
        6. Check if the result is within 32-bit range; else return 0.
        7. Return the reversed integer.
        """

        # Step 1: Define the range of 32-bit signed integer
        INT_MIN, INT_MAX = -2**31, 2**31 - 1  

        # Step 2: Extract sign
        sign = -1 if x < 0 else 1  

        # Step 3: Use absolute value for reversal
        x = abs(x)

        # Step 4: Initialize reversed number
        rev = 0  

        # Step 5: Reverse the number digit by digit
        while x != 0:
            digit = x % 10          # Extract last digit
            x //= 10                # Remove last digit
            rev = rev * 10 + digit  # Build reversed number

        # Step 6: Reapply the original sign
        rev *= sign  

        # Step 7: Check for overflow
        if rev < INT_MIN or rev > INT_MAX:
            return 0

        # Step 8: Return result
        return rev


"""
--- Dry Run Example ---
Input: x = -123

Step 1: INT_MIN = -2147483648, INT_MAX = 2147483647
Step 2: sign = -1 (since x < 0)
Step 3: x = abs(-123) = 123, rev = 0

Loop Iterations:
1st Iteration:
    digit = 123 % 10 = 3
    x = 123 // 10 = 12
    rev = 0 * 10 + 3 = 3

2nd Iteration:
    digit = 12 % 10 = 2
    x = 12 // 10 = 1
    rev = 3 * 10 + 2 = 32

3rd Iteration:
    digit = 1 % 10 = 1
    x = 1 // 10 = 0
    rev = 32 * 10 + 1 = 321

Loop ends since x = 0
Step 6: Apply sign → rev = 321 * -1 = -321
Step 7: Check range → valid
Output: -321
"""

"""
--- Time Complexity ---
O(log |x|), because we process each digit once. 
(Number of digits in x is proportional to log10(x)).

--- Space Complexity ---
O(1), since only a few integer variables are used (constant space).
"""

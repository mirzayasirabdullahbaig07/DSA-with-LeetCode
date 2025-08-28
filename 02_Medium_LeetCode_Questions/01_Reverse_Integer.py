# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21

# Constraints:
# -231 <= x <= 231 - 1

class Solution:
    def reverse(self, x: int) -> int:
        # Define the range of 32-bit signed integer
        INT_MIN, INT_MAX = -2**31, 2**31 - 1  

        # Step 1: Handle the sign of the number
        # If x is negative, sign = -1 else sign = 1
        sign = -1 if x < 0 else 1  

        # Work with absolute value (ignore sign for now)
        x = abs(x)

        # Step 2: Initialize reversed number
        rev = 0  

        # Step 3: Reverse the digits using math
        while x != 0:
            digit = x % 10      # Extract the last digit
            x //= 10            # Remove the last digit from x
            rev = rev * 10 + digit  # Build the reversed number

        # Step 4: Reapply the original sign
        rev *= sign  

        # Step 5: Check for overflow (must fit in 32-bit signed integer)
        if rev < INT_MIN or rev > INT_MAX:
            return 0

        # Step 6: Return the reversed integer
        return rev

# 🛠 Example Run (step by step in your head)
# Input: x = -123
# sign = -1, x = 123, rev = 0

# Loop:
# digit = 123 % 10 = 3, x = 12, rev = 0*10 + 3 = 3
# digit = 12 % 10 = 2, x = 1, rev = 3*10 + 2 = 32
# digit = 1 % 10 = 1, x = 0, rev = 32*10 + 1 = 321

# Apply sign: rev = 321 * -1 = -321
# Check range (safe)

# Return -321

# Time Complexity: O(log |x|) → proportional to the number of digits in x.

# Space Complexity: O(1) → only constant extra memory used.
"""
Problem:
Given an integer x, return True if x is a palindrome, and False otherwise.

Example 1:
Input: x = 121
Output: True
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: False
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.

Example 3:
Input: x = 10
Output: False
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-2^31 <= x <= 2^31 - 1

Follow-up: Could you solve it without converting the integer to a string?
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Approach:
        - Negative numbers are never palindrome because of the minus sign.
        - Reverse the integer mathematically (without using string conversion).
        - Compare the original number with the reversed number.
        """

        # Step 1: Check if number is negative
        if x < 0:
            return False

        # Step 2: Store original number for comparison later
        original = x
        rev = 0

        # Step 3: Reverse the number mathematically
        while x != 0:
            digit = x % 10             # Get last digit
            x //= 10                   # Remove last digit
            rev = rev * 10 + digit     # Append digit to reversed number

        # Step 4: Check if reversed == original
        return original == rev


"""
--- Dry Run Example ---
Input: x = 121

Step 1: x = 121, original = 121, rev = 0
Step 2: digit = 121 % 10 = 1 → rev = 0*10 + 1 = 1, x = 121 // 10 = 12
Step 3: digit = 12 % 10 = 2 → rev = 1*10 + 2 = 12, x = 12 // 10 = 1
Step 4: digit = 1 % 10 = 1 → rev = 12*10 + 1 = 121, x = 1 // 10 = 0
Now x = 0 → loop ends.

Compare: original = 121, rev = 121 → Equal → Return True
Output: True

--- Another Example ---
Input: x = -121
Step 1: Negative check → return False
Output: False

--- Another Example ---
Input: x = 10
Step 1: x = 10, original = 10, rev = 0
digit = 0 → rev = 0, x = 1
digit = 1 → rev = 1, x = 0
Compare: original = 10, rev = 1 → Not equal → Return False
Output: False
"""

"""
--- Time and Space Complexity ---
Let n = number of digits in x

- Time Complexity: O(n)
    We process each digit once while reversing.
- Space Complexity: O(1)
    We only use a few integer variables (rev, digit, original).
"""
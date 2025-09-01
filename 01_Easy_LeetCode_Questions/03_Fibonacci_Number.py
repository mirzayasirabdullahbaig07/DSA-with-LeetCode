"""
Problem:
The Fibonacci numbers, commonly denoted F(n), form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:
0 <= n <= 30
"""

class Solution:
    def fib(self, n: int) -> int:
        """
        Approach:
        - Iterative (Bottom-Up Dynamic Programming with Two Variables)
        - Start with base values F(0) = 0, F(1) = 1
        - Update two variables in a loop to compute F(n)

        Time Complexity: O(n)  -> Loop runs n times
        Space Complexity: O(1) -> Only two variables used
        """
        if n < 2:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


# -------- Dry Run Example --------
# Input: n = 4
# Step 1: Initialize a=0, b=1
# Step 2: Loop from 2 to 4
#   i=2 -> a=1, b=1   (F(2)=1)
#   i=3 -> a=1, b=2   (F(3)=2)
#   i=4 -> a=2, b=3   (F(4)=3)
# Output: 3
# ---------------------------------


if __name__ == "__main__":
    sol = Solution()
    # Test Cases
    print(sol.fib(2))  # Expected output: 1
    print(sol.fib(3))  # Expected output: 2
    print(sol.fib(4))  # Expected output: 3

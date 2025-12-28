"""
LeetCode 1614 - Maximum Nesting Depth of the Parentheses

PROBLEM SUMMARY:
----------------
You are given a valid parentheses string (VPS).
Your task is to find the maximum nesting depth of parentheses.

Nesting depth means:
- How many '(' are open at the same time at the deepest point.

Example:
---------
Input: "(1+(2*3)+((8)/4))+1"
Output: 3

Explanation:
- The number 8 is inside 3 nested parentheses: ((8))

APPROACH:
---------
We iterate through each character in the string and:
1. Increase a counter when we see '('
2. Decrease the counter when we see ')'
3. Track the maximum value of the counter at any point

This works because:
- '(' means we go one level deeper
- ')' means we exit one level
- The highest level reached is the answer

TIME & SPACE COMPLEXITY:
------------------------
Time Complexity:  O(n)  -> We scan the string once
Space Complexity: O(1)  -> Only two integer variables are used
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        """
        This function returns the maximum nesting depth of parentheses.

        Parameters:
        s (str): A valid parentheses string containing digits and operators

        Returns:
        int: Maximum nesting depth
        """

        # Tracks the current number of open parentheses
        curr_depth = 0

        # Stores the maximum depth reached at any point
        max_depth = 0

        # Loop through every character in the string
        for ch in s:

            # If we encounter an opening parenthesis
            if ch == '(':
                # Increase current depth
                curr_depth += 1

                # Update maximum depth if current is greater
                max_depth = max(max_depth, curr_depth)

            # If we encounter a closing parenthesis
            elif ch == ')':
                # Decrease current depth since we exit a level
                curr_depth -= 1

        # Return the maximum depth found
        return max_depth

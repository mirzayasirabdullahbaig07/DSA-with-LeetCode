"""
LeetCode 1903: Largest Odd Number in String
------------------------------------------

Problem Explanation:
--------------------
You are given a string `num` that represents a very large integer.
Your task is to find the largest-valued odd number that can be formed
as a non-empty substring of this string.

A substring means a continuous part of the string.
If no odd number can be formed, return an empty string "".

Important Observations:
-----------------------
1. A number is considered odd if its last digit is odd.
   Odd digits are: 1, 3, 5, 7, 9.
2. To get the largest possible odd number, we want the longest substring
   starting from the left and ending at an odd digit.
3. Checking all substrings would be inefficient, so we need an optimized approach.

Optimized Approach:
-------------------
1. Start scanning the string from the rightmost digit.
2. Find the first digit that is odd.
3. Once found, return the substring from index 0 up to that digit.
4. If no odd digit is found after scanning the entire string, return "".

Why This Works:
---------------
- Any substring ending earlier would be smaller in value.
- The rightmost odd digit gives the maximum possible length.
- This avoids unnecessary substring checks.

Example Walkthrough:
--------------------
Input:  "35427"
Last digit '7' is odd → whole string is odd
Output: "35427"

Input:  "4206"
No odd digits found
Output: ""

Time Complexity:
----------------
O(n), where n is the length of the string.

Space Complexity:
-----------------
O(1), no extra space used.
"""


class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)

        # Traverse the string from right to left
        for i in range(n - 1, -1, -1):
            # Check if the digit is odd
            if int(num[i]) % 2 == 1:
                # Return the substring up to this index
                return num[:i + 1]

        # If no odd digit is found
        return ""

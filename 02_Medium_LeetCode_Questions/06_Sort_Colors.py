"""
LEETCODE PROBLEM: 75. Sort Colors
---------------------------------
QUESTION STATEMENT:
-------------------
Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers:
- 0 → red
- 1 → white
- 2 → blue

You must solve this problem WITHOUT using the library's sort function.


EXAMPLES:
---------
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]


CONSTRAINTS:
------------
- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2


FOLLOW UP:
----------
Could you come up with a one-pass algorithm using only constant extra space?


APPROACH / TECHNIQUE:
---------------------
We use the **Dutch National Flag Algorithm** with three pointers:
- low   → boundary for 0s
- mid   → current index being checked
- high  → boundary for 2s

Algorithm:
1. Start with low = 0, mid = 0, high = len(nums) - 1
2. While mid <= high:
   - If nums[mid] == 0:
        Swap nums[low] and nums[mid]
        Move low++, mid++
   - If nums[mid] == 1:
        Just move mid++
   - If nums[mid] == 2:
        Swap nums[mid] and nums[high]
        Move high-- (don’t move mid yet, because swapped value may need recheck)

Why this works:
- Ensures left zone contains all 0s
- Middle zone contains 1s
- Right zone contains 2s
- Entire array sorted in one traversal.


TIME COMPLEXITY:
----------------
- O(n) → one pass through the array.

SPACE COMPLEXITY:
-----------------
- O(1) → only three pointers used.


DRY RUN:
--------
nums = [2,0,2,1,1,0]

Step 1: low=0, mid=0, high=5
nums[mid]=2 → swap with high
nums = [0,0,2,1,1,2], high=4

Step 2: mid=0 → nums[mid]=0 → swap with low
nums = [0,0,2,1,1,2], low=1, mid=1

Step 3: mid=1 → nums[mid]=0 → swap with low
nums = [0,0,2,1,1,2], low=2, mid=2

Step 4: mid=2 → nums[mid]=2 → swap with high
nums = [0,0,1,1,2,2], high=3

Step 5: mid=2 → nums[mid]=1 → mid=3
Step 6: mid=3 → nums[mid]=1 → mid=4

Loop ends (mid > high).
Final nums = [0,0,1,1,2,2]
"""

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

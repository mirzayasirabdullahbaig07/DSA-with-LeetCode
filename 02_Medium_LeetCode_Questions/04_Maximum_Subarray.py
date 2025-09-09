"""
LEETCODE PROBLEM: 53. Maximum Subarray
--------------------------------------

QUESTION STATEMENT:
-------------------
Given an integer array nums, find the subarray with the largest sum, 
and return its sum.

A subarray is a contiguous part of the array.

EXAMPLES:
---------
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation:
- The subarray [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation:
- Only one element → largest sum = 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation:
- The subarray [5,4,-1,7,8] has the largest sum = 23.


CONSTRAINTS:
------------
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4


APPROACH / TECHNIQUE:
---------------------
We use **Kadane’s Algorithm (Dynamic Programming idea)**:
1. Traverse the array while keeping track of:
   - current_sum = max sum of subarray ending at the current index
   - max_sum = global maximum so far
2. At each number `num`:
   - Decide whether to:
     a) start a new subarray from `num` (if current_sum + num < num), or
     b) extend the previous subarray (if current_sum + num >= num).
   - Update max_sum accordingly.

WHY THIS WORKS:
---------------
- It ensures we always track the best "ending here" sum while also 
  updating the global maximum.
- Efficiently finds the largest subarray sum in one pass.

TIME COMPLEXITY:
----------------
- Single pass through nums → O(n)

SPACE COMPLEXITY:
-----------------
- Only two variables (current_sum, max_sum) → O(1)


DRY RUN:
--------
nums = [-2,1,-3,4,-1,2,1,-5,4]

Start:
current_sum = max_sum = -2

Step 1: num=1
current_sum = max(1, -2+1) = 1
max_sum = max(-2, 1) = 1

Step 2: num=-3
current_sum = max(-3, 1-3) = -2
max_sum = max(1, -2) = 1

Step 3: num=4
current_sum = max(4, -2+4) = 4
max_sum = max(1, 4) = 4

Step 4: num=-1
current_sum = max(-1, 4-1) = 3
max_sum = max(4, 3) = 4

Step 5: num=2
current_sum = max(2, 3+2) = 5
max_sum = max(4, 5) = 5

Step 6: num=1
current_sum = max(1, 5+1) = 6
max_sum = max(5, 6) = 6

Step 7: num=-5
current_sum = max(-5, 6-5) = 1
max_sum = max(6, 1) = 6

Step 8: num=4
current_sum = max(4, 1+4) = 5
max_sum = max(6, 5) = 6

Final Answer = 6
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]

        for num in nums[1:]:
            # either start fresh at num, or extend the previous subarray
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum

"""
Problem: Search Insert Position (LeetCode 35)
---------------------------------------------
You are given a sorted array of distinct integers and a target value.  
Return the index if the target is found.  
If not, return the index where it would be if inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Examples:
---------
1. Input: nums = [1,3,5,6], target = 5
   Output: 2
   Explanation: target 5 is found at index 2.

2. Input: nums = [1,3,5,6], target = 2
   Output: 1
   Explanation: target 2 is not found. It would be inserted before 3, at index 1.

3. Input: nums = [1,3,5,6], target = 7
   Output: 4
   Explanation: target 7 is not found. It would be inserted at the end, index 4.

-----------------------------------------------------
Techniques Used:
1. Binary Search:
   - Since nums is sorted, we can use binary search instead of linear scan.
   - Keep track of a variable `ans` initialized to n (end position).
   - If nums[mid] >= target, update ans = mid and search left.
   - If nums[mid] < target, search right.
   - At the end, `ans` will store the correct insertion index.

-----------------------------------------------------
Time Complexity:
- O(log n), where n = length of nums (binary search).
Space Complexity:
- O(1), only a few variables are used.
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n - 1
        ans = n  # default insertion position = end of array

        while low <= high:
            mid = (low + high) // 2  # midpoint of current search window

            if nums[mid] >= target:
                ans = mid            # candidate insertion position
                high = mid - 1       # continue searching left
            else:
                low = mid + 1        # search right half

        return ans  # final insertion index

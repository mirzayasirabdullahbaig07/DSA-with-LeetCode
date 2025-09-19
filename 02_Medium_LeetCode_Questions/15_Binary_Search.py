"""
Problem: Binary Search (LeetCode 704)
-------------------------------------
You are given a sorted array of integers nums (in ascending order) 
and an integer target. The task is to find the index of target in nums. 
If target does not exist in nums, return -1.

You must write an algorithm with O(log n) runtime complexity.

Examples:
---------
1. Input: nums = [-1,0,3,5,9,12], target = 9
   Output: 4
   Explanation: 9 exists in nums and its index is 4.

2. Input: nums = [-1,0,3,5,9,12], target = 2
   Output: -1
   Explanation: 2 does not exist in nums, so return -1.

-----------------------------------------------------
Techniques Used:
1. Binary Search:
   - Since nums is sorted, we can use binary search to reduce search space.
   - Repeatedly check the middle element:
        - If nums[mid] == target → return index.
        - If nums[mid] < target → search in right half.
        - If nums[mid] > target → search in left half.

2. Iterative Approach:
   - Use two pointers (low, high) to track search boundaries.
   - Loop until low <= high.

-----------------------------------------------------
Time Complexity:
- Each step halves the search space.
- O(log n), where n = length of nums.

Space Complexity:
- O(1), since only a few variables are used.
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1

        # Standard binary search loop
        while low <= high:
            mid = (low + high) // 2  # Find middle index

            if nums[mid] == target:
                return mid  # Target found, return index
            elif nums[mid] < target:
                low = mid + 1  # Search right half
            else:
                high = mid - 1  # Search left half

        return -1  # Target not found

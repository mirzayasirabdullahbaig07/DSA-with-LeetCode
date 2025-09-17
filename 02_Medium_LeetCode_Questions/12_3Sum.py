"""
Problem: 3Sum
-------------
Given an integer array nums, return all the unique triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

The solution set must not contain duplicate triplets.

Example:
--------
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]

-----------------------------------------------------
Techniques Used:
1. Sorting:
   - The array is first sorted to apply the two-pointer strategy efficiently 
     and also to handle duplicates more easily.

2. Two-pointer approach:
   - For each number nums[i], we try to find two numbers (nums[left], nums[right])
     such that nums[i] + nums[left] + nums[right] == 0.
   - If sum is too small, move left pointer.
   - If sum is too large, move right pointer.
   - If sum matches, store triplet and skip duplicates.

3. Duplicate Handling:
   - Skip duplicate values for the first number (nums[i]) and also for 
     second/third numbers while moving pointers.

-----------------------------------------------------
Time Complexity:
- Sorting the array: O(n log n)
- For each element, applying two-pointer search: O(n^2) in the worst case
- Overall: O(n^2)

Space Complexity:
- O(1) extra space (ignoring the result list).
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Step 1: Sort the array for two-pointer strategy

        for i in range(len(nums)):
            # Step 2: Skip duplicate "first" elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]  # Step 3: We want nums[left] + nums[right] = -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    # Found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Step 4: Skip duplicate "second" and "third" elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif s < target:
                    left += 1  # Need a larger sum
                else:
                    right -= 1  # Need a smaller sum

        return res

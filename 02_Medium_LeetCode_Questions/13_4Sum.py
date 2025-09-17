"""
Problem: 4Sum
-------------
Given an array nums of n integers, return all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
    - 0 <= a, b, c, d < n
    - a, b, c, and d are distinct
    - nums[a] + nums[b] + nums[c] + nums[d] == target

The solution set must not contain duplicate quadruplets.

Example 1:
----------
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]

Example 2:
----------
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

-----------------------------------------------------
Techniques Used:
1. Sorting:
   - Sort the array to make duplicate handling easier and to apply the two-pointer approach.

2. Two nested loops + Two-pointer:
   - First fix two numbers (nums[i], nums[j]).
   - Use two pointers (left, right) to find pairs such that
     nums[i] + nums[j] + nums[left] + nums[right] == target.

3. Duplicate Handling:
   - Skip duplicates for i, j, left, and right to ensure unique quadruplets.

-----------------------------------------------------
Time Complexity:
- Sorting the array: O(n log n)
- Two nested loops for i and j: O(n^2)
- Two-pointer scan for each pair (i, j): O(n)
- Overall: O(n^3)

Space Complexity:
- O(1) extra space (ignoring the result list).
"""

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        res = []
        n = len(nums)

        # Step 2: Fix first element nums[i]
        for i in range(n - 3):
            # Skip duplicate nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Step 3: Fix second element nums[j]
            for j in range(i + 1, n - 2):
                # Skip duplicate nums[j]
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Step 4: Use two-pointer for the remaining two numbers
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicate nums[left]
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicate nums[right]
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1  # Need larger sum
                    else:
                        right -= 1  # Need smaller sum

        return res

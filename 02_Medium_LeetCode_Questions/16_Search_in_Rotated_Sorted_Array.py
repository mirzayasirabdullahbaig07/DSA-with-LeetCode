"""
Problem: Search in Rotated Sorted Array (LeetCode #33)

You are given an integer array 'nums' that was originally sorted in ascending order,
but it may have been rotated at an unknown pivot index k.

- The array contains distinct integers.
- Task: Search for the target value in nums.
- If found, return its index.
- Otherwise, return -1.

Requirement: Must solve with O(log n) runtime complexity.

-------------------------------------------------------
Example 1:
nums   = [4,5,6,7,0,1,2], target = 0
Output = 4   (since nums[4] = 0)

Example 2:
nums   = [4,5,6,7,0,1,2], target = 3
Output = -1  (3 does not exist in nums)

Example 3:
nums   = [1], target = 0
Output = -1

-------------------------------------------------------
Technique Used:
1. **Modified Binary Search** (on rotated sorted array)
   - Normally, binary search works on fully sorted arrays.
   - But here, the array might be rotated, so one half of the array
     is always sorted at any point.
   - At each step, we:
       a) Check if nums[mid] == target → return mid.
       b) Determine which half (left or right) is sorted.
       c) Check if target lies inside the sorted half.
          - If yes → adjust boundaries to that half.
          - If no  → search in the other half.
   - Continue until low > high.

-------------------------------------------------------
Time Complexity:
- O(log n) → Because binary search halves the search space at each step.
- Space Complexity: O(1) → Only constant extra variables are used.
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n         = len(nums)
        low, high = 0, n - 1
        
        while low <= high:
            mid = (low + high) // 2          # middle index
            
            if nums[mid] == target:          # target found
                return mid
            
            # ----- identify the sorted half -----
            if nums[low] <= nums[mid]:       # left half is sorted
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1           # search in left half
                else:
                    low  = mid + 1           # search in right half
            else:                            # right half is sorted
                if nums[mid] <= target <= nums[high]:
                    low  = mid + 1           # search in right half
                else:
                    high = mid - 1           # search in left half
        
        return -1                            # target not found


# Example test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.search([4,5,6,7,0,1,2], 0))  # Output: 4
    print(sol.search([4,5,6,7,0,1,2], 3))  # Output: -1
    print(sol.search([1], 0))              # Output: -1
    print(sol.search([5,6,7,1,2,3,4], 2))  # Output: 4

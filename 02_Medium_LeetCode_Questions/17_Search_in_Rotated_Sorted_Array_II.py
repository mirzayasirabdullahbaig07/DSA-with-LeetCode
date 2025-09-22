"""
Problem: Search in Rotated Sorted Array II (LeetCode #81)

You are given an integer array `nums` that was originally sorted in non-decreasing order
(but may contain duplicates). It may have been rotated at an unknown pivot.

- Task: Return True if the target exists in nums, otherwise False.
- The array can contain duplicates, unlike problem #33.

-------------------------------------------------------
Example 1:
nums   = [2,5,6,0,0,1,2], target = 0
Output = True   (0 exists in nums)

Example 2:
nums   = [2,5,6,0,0,1,2], target = 3
Output = False  (3 does not exist in nums)

-------------------------------------------------------
Key Differences from Problem #33:
1. Duplicates are allowed here.
2. When duplicates occur at both ends (nums[low] == nums[mid] == nums[high]),
   we cannot determine which half is sorted → in this case, just shrink the window
   by moving low += 1 and high -= 1.

-------------------------------------------------------
Technique Used:
- Modified Binary Search
- At each step:
    a) Check if nums[mid] == target → return True.
    b) If duplicates make it ambiguous (nums[low] == nums[mid] == nums[high]),
       shrink boundaries (low++, high--).
    c) Otherwise, determine which half is sorted (left or right).
    d) Decide if target lies in that half, adjust search boundaries accordingly.

-------------------------------------------------------
Time Complexity:
- Best / Average case: O(log n) → like standard binary search.
- Worst case (when many duplicates are present): O(n),
  because shrinking boundaries one by one may degrade performance.

Space Complexity:
- O(1) → only constant extra variables used.
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2              # Find the middle index

            if nums[mid] == target:              # If middle element is target, return True
                return True

            # Handle duplicates: cannot decide sorted half
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            # If left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1               # Search in left half
                else:
                    low = mid + 1                # Search in right half
            # Else, right half is sorted
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1                # Search in right half
                else:
                    high = mid - 1               # Search in left half

        return False                             # Target not found


# Example test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.search([2,5,6,0,0,1,2], 0))   # Output: True
    print(sol.search([2,5,6,0,0,1,2], 3))   # Output: False
    print(sol.search([1,0,1,1,1], 0))       # Output: True
    print(sol.search([1,1,1,1,1], 2))       # Output: False

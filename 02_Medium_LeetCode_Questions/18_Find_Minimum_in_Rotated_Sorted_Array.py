"""
Problem: 153. Find Minimum in Rotated Sorted Array

We are given a sorted array that has been rotated between 1 and n times.
Our task: return the minimum element in O(log n) time.

-------------------------------------------------------
Example 1:
nums   = [3,4,5,1,2]
Output = 1
Explanation: Original = [1,2,3,4,5] rotated 3 times

Example 2:
nums   = [4,5,6,7,0,1,2]
Output = 0
Explanation: Original = [0,1,2,4,5,6,7] rotated 4 times

Example 3:
nums   = [11,13,15,17]
Output = 11
Explanation: Already sorted, rotated 4 times (or not rotated).

-------------------------------------------------------
Technique Used:
- Modified Binary Search
- At each step:
    1. If the left half is sorted → the minimum must lie either in this half's first element
       OR in the right half.
    2. If the right half is sorted → the minimum may lie in mid or left half.
    3. Update the `minimum` during the search.

-------------------------------------------------------
Time Complexity:
- O(log n) → Because binary search is applied to halve the search space each time.
- Worst case: O(log n), since there are no duplicates.

Space Complexity:
- O(1) → Only constant extra variables used.

-------------------------------------------------------
Constraints:
- 1 <= n <= 5000
- Elements are unique, array is rotated sorted.
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n - 1
        minimum = float("inf")  # Initialize with +infinity

        while low <= high:
            mid = (low + high) // 2  # Find the middle index

            # If left half is sorted
            if nums[low] <= nums[mid]:
                minimum = min(minimum, nums[low])  # Minimum could be nums[low]
                low = mid + 1                      # Move search to right half
            else:
                # Right half is sorted
                minimum = min(minimum, nums[mid])  # Minimum could be nums[mid]
                high = mid - 1                     # Move search to left half

        return minimum  # Return the smallest element


# Example test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMin([3,4,5,1,2]))        # Output: 1
    print(sol.findMin([4,5,6,7,0,1,2]))    # Output: 0
    print(sol.findMin([11,13,15,17]))      # Output: 11

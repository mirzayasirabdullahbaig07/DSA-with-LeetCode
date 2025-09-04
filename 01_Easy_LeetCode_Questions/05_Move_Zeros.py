"""
Problem: Move Zeroes (LeetCode 283)
-------------------------------------
Given an integer array nums, move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
------------
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1

Requirement: 
- Do this in-place (modify nums directly)
- Do NOT make a copy of the array
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Approach: Two Pointer Method
        -------------------------------
        - Use a pointer `pos` to track the position where the next non-zero 
          element should go.
        - Iterate over the array:
            - If nums[i] is non-zero, place it at nums[pos] and increment pos.
        - After processing all elements, fill the rest with zeroes.

        Example Dry Run:
        ----------------
        nums = [0,1,0,3,12]

        Step 1: pos = 0
        Step 2: i=0 → nums[0]=0 → skip
        Step 3: i=1 → nums[1]=1 → place at nums[0] → [1,1,0,3,12], pos=1
        Step 4: i=2 → nums[2]=0 → skip
        Step 5: i=3 → nums[3]=3 → place at nums[1] → [1,3,0,3,12], pos=2
        Step 6: i=4 → nums[4]=12 → place at nums[2] → [1,3,12,3,12], pos=3
        Step 7: Fill remaining indices with 0 → [1,3,12,0,0]

        Final Answer: [1,3,12,0,0]
        """

        pos = 0  # pointer for next non-zero placement

        # Step 1: Move all non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1

        # Step 2: Fill the rest with zeroes
        while pos < len(nums):
            nums[pos] = 0
            pos += 1


"""
Complexity Analysis:
-----------------------
Time Complexity: O(n)
    - We scan the array once to move non-zeros.
    - Another pass (at most n) to fill zeroes.
    - Total O(n).

Space Complexity: O(1)
    - Only uses pointer variables, no extra array.

This is the most efficient in-place solution.
"""

# ------------------ TEST CASES ------------------
if __name__ == "__main__":
    s = Solution()

    """ Test case 1 """
    arr1 = [0,1,0,3,12]
    s.moveZeroes(arr1)
    print("After moving zeroes:", arr1)  
    # Expected: [1,3,12,0,0]

    """ Test case 2 """
    arr2 = [0]
    s.moveZeroes(arr2)
    print("After moving zeroes:", arr2)  
    # Expected: [0]

    """ Test case 3 """
    arr3 = [4,2,4,0,0,3,0,5,1,0]
    s.moveZeroes(arr3)
    print("After moving zeroes:", arr3)  
    # Expected: [4,2,4,3,5,1,0,0,0,0]

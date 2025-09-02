"""
Problem 26: Remove Duplicates from Sorted Array
Given an integer array nums sorted in non-decreasing order, remove the 
duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return 
the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, 
you need to do the following things:

1. Change the array nums such that the first k elements of nums contain 
   the unique elements in the order they were present in nums initially.
2. The remaining elements of nums are not important as well as the size 
   of nums.
3. Return k.

Custom Judge:
--------------
The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length

    int k = removeDuplicates(nums); // Calls your implementation

    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }

If all assertions pass, then your solution will be accepted.

Examples:
----------
Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two 
elements of nums being 1 and 2 respectively. It does not matter what you 
leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five 
elements of nums being 0, 1, 2, 3, and 4 respectively.

Constraints:
-------------
1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Approach:
        ----------
        - Since nums is sorted, duplicates are always next to each other.
        - Use Two Pointers:
            - i = slow pointer → tracks the index of the last unique element.
            - j = fast pointer → scans through the array.
        - Whenever nums[j] != nums[i], it means nums[j] is a new unique 
          element. Move i forward and assign nums[i] = nums[j].
        - At the end, i + 1 is the total count of unique elements.

        Time Complexity:
        -----------------
        O(n) → We traverse the array once.

        Space Complexity:
        -----------------
        O(1) → In-place modification, no extra space used.

        Returns:
        ----------
        k (int) → the number of unique elements in nums
        """
        if not nums:
            return 0
        
        i = 0  # slow pointer
        for j in range(1, len(nums)):  # fast pointer
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1


# ----------------------------------------------------------
# Dry Run Example
# ----------------------------------------------------------
"""
Input: nums = [0,0,1,1,1,2,2,3,3,4]

Step-by-step execution:

Start: i=0, nums=[0,0,1,1,1,2,2,3,3,4]

j=1 → nums[1]=0, nums[0]=0 → same → skip
j=2 → nums[2]=1, nums[0]=0 → different → i=1, nums[1]=1 → [0,1,1,1,1,2,2,3,3,4]
j=3 → nums[3]=1, nums[1]=1 → same → skip
j=4 → nums[4]=1, nums[1]=1 → same → skip
j=5 → nums[5]=2, nums[1]=1 → different → i=2, nums[2]=2 → [0,1,2,1,1,2,2,3,3,4]
j=6 → nums[6]=2, nums[2]=2 → same → skip
j=7 → nums[7]=3, nums[2]=2 → different → i=3, nums[3]=3 → [0,1,2,3,1,2,2,3,3,4]
j=8 → nums[8]=3, nums[3]=3 → same → skip
j=9 → nums[9]=4, nums[3]=3 → different → i=4, nums[4]=4 → [0,1,2,3,4,2,2,3,3,4]

End:
- Unique count = i + 1 = 5
- Modified nums = [0,1,2,3,4,_,_,_,_,_]
"""

# ----------------------------------------------------------
# Test Cases
# ----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    nums1 = [1,1,2]
    k1 = sol.removeDuplicates(nums1)
    print("Output:", k1, "Array:", nums1[:k1])  
    # Expected: 2, [1,2]

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    k2 = sol.removeDuplicates(nums2)
    print("Output:", k2, "Array:", nums2[:k2])  
    # Expected: 5, [0,1,2,3,4]

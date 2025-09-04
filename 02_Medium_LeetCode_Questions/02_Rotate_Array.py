"""
Problem: Rotate Array (LeetCode 189)
---------------------------------------
Given an integer array nums, rotate the array to the right by k steps, 
where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]

Constraints:
------------
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5

Follow-up: 
- Can you solve this in-place with O(1) extra space?
- There are at least 3 ways to solve this problem.
"""

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Approach: Array Reversal Trick
        --------------------------------
        1. Reverse the entire array
        2. Reverse the first k elements
        3. Reverse the last n-k elements

        Why does this work?
        -------------------
        Reversing changes the order of elements. 
        By carefully applying 3 reversals, we can "simulate" rotation without extra space.

        Example Dry Run:
        ----------------
        nums = [1,2,3,4,5,6,7], k = 3

        Step 1: reverse whole array 
        → [7,6,5,4,3,2,1]

        Step 2: reverse first k=3 
        → [5,6,7,4,3,2,1]

        Step 3: reverse rest 
        → [5,6,7,1,2,3,4] final rotated array
        """

        n = len(nums)

        """
        If k >= n, rotating more than n times is same as rotating (k % n) times.
        Example: rotating 7 elements by 10 steps → same as rotating by 3 steps.
        """
        k = k % n

        def reverse(start: int, end: int) -> None:
            """
            Helper function to reverse part of the array.
            Works by swapping left and right elements.
            """
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        """ Step 1: Reverse the entire array """
        reverse(0, n - 1)

        """ Step 2: Reverse the first k elements """
        reverse(0, k - 1)

        """ Step 3: Reverse the remaining n-k elements """
        reverse(k, n - 1)

        """ Done! Array rotated in-place with O(1) space """


"""
Complexity Analysis:
-----------------------
⏱ Time Complexity: O(n)
    - We reverse the array 3 times.
    - Each reversal takes O(n).
    - Total = O(n)

Space Complexity: O(1)
    - We only use variables for indices.
    - No extra array is created.

This is the most efficient in-place solution.
"""

# ------------------ TEST CASES ------------------
if __name__ == "__main__":
    s = Solution()

    """ Test case 1 """
    arr1 = [1,2,3,4,5,6,7]
    s.rotate(arr1, 3)
    print("After rotating by 3:", arr1)  
    # Expected: [5,6,7,1,2,3,4]

    """ Test case 2 """
    arr2 = [-1,-100,3,99]
    s.rotate(arr2, 2)
    print("After rotating by 2:", arr2)  
    # Expected: [3,99,-1,-100]

    """ Test case 3: k larger than n """
    arr3 = [1,2,3]
    s.rotate(arr3, 10)  
    print("After rotating by 10:", arr3)  
    # Expected: [2,3,1]

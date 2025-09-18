"""
Problem: Reverse Pairs (LeetCode 493)
-------------------------------------
Given an integer array nums, return the number of reverse pairs in the array.

Definition of Reverse Pair:
A pair (i, j) is considered a reverse pair if:
    - 0 <= i < j < len(nums), and
    - nums[i] > 2 * nums[j].

Examples:
---------
1. Input: nums = [1,3,2,3,1]
   Output: 2
   Explanation: The reverse pairs are:
   (1, 4) → nums[1] = 3, nums[4] = 1 → 3 > 2*1
   (3, 4) → nums[3] = 3, nums[4] = 1 → 3 > 2*1

2. Input: nums = [2,4,3,5,1]
   Output: 3
   Explanation: The reverse pairs are:
   (1, 4) → 4 > 2*1
   (2, 4) → 3 > 2*1
   (3, 4) → 5 > 2*1

-----------------------------------------------------
Techniques Used:
1. Modified Merge Sort (Divide & Conquer):
   - Normal brute force O(n^2) check for all pairs is too slow for n up to 10^5.
   - Instead, use merge sort to divide the array into halves and count reverse pairs 
     while merging.
   - During merging, we count how many elements in the right half satisfy:
     nums[i] > 2 * nums[j].

2. Merge Process:
   - First count reverse pairs between two sorted halves.
   - Then merge the halves into a sorted array (standard merge sort step).

-----------------------------------------------------
Time Complexity:
- Each merge step takes O(n) for counting + O(n) for merging.
- Recurrence relation: T(n) = 2T(n/2) + O(n)
- Overall: O(n log n)

Space Complexity:
- O(n) for temporary arrays used during merging.
"""

from typing import List, Tuple

class Solution:
    def mergeList(self, arr1: List[int], arr2: List[int]) -> Tuple[List[int], int]:
        """
        Merges two sorted arrays (arr1 and arr2).
        Also counts reverse pairs where element from arr1 > 2 * element from arr2.
        """
        n, m = len(arr1), len(arr2)
        count = 0
        result = []
        j = 0

        # Step 1: Count reverse pairs
        for i in range(n):
            while j < m and arr1[i] > 2 * arr2[j]:
                j += 1
            count += j

        # Step 2: Merge two sorted arrays
        i, j = 0, 0
        while i < n and j < m:
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1

        # Append remaining elements
        while i < n:
            result.append(arr1[i])
            i += 1
        while j < m:
            result.append(arr2[j])
            j += 1

        return result, count

    def mergeSort(self, lst: List[int]) -> Tuple[List[int], int]:
        """
        Recursively apply merge sort and count reverse pairs.
        """
        if len(lst) <= 1:
            return lst, 0

        mid = len(lst) // 2
        left_half, right_half = lst[:mid], lst[mid:]

        sorted_left, count_left = self.mergeSort(left_half)
        sorted_right, count_right = self.mergeSort(right_half)

        merged, cross_count = self.mergeList(sorted_left, sorted_right)

        return merged, count_left + count_right + cross_count

    def reversePairs(self, nums: List[int]) -> int:
        """
        Returns the total number of reverse pairs in nums.
        """
        _, count = self.mergeSort(nums)
        return count

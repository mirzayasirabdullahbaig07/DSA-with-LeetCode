"""
LeetCode 540. Single Element in a Sorted Array

Problem:
---------
You are given a sorted array consisting of only integers where every element 
appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:
----------
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
----------
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:
------------
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5

------------------------------------------------------------
Brute Force Solution (Linear Scan):
------------------------------------------------------------
- Iterate through the array.
- Check if the current element is different from its neighbors.
- Return that element.

Time Complexity: O(n)   # may check all elements
Space Complexity: O(1)  # no extra space

------------------------------------------------------------
Optimal Solution (Binary Search):
------------------------------------------------------------
Observation:
- Array is sorted.
- Elements come in pairs (x,x), except for one single element.
- For pairs:
    - First element of a pair is at even index.
    - Second element of a pair is at odd index.
- If this "pairing pattern" breaks, the single element is nearby.

Algorithm:
1. Use binary search (low=0, high=n-1).
2. Compute mid = (low+high)//2.
3. If nums[mid] is unique (not equal to neighbors), return nums[mid].
4. If nums[mid] == nums[mid-1]:
    - If mid is odd → unique is on the right.
    - If mid is even → unique is on the left.
5. If nums[mid] == nums[mid+1]:
    - If mid is even → unique is on the right.
    - If mid is odd → unique is on the left.
6. Continue until low == high → that’s the single element.

Time Complexity: O(log n)   # binary search halves search space
Space Complexity: O(1)      # only pointers

------------------------------------------------------------
Code Implementation:
------------------------------------------------------------
"""

from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            # Ensure mid is even (so pairs align correctly)
            if mid % 2 == 1:
                mid -= 1  

            # If nums[mid] == nums[mid+1], unique is on the right half
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                # Otherwise, unique is on the left half
                high = mid

        return nums[low]


"""
------------------------------------------------------------
Dry Run Example:
------------------------------------------------------------
Input: nums = [1,1,2,3,3,4,4,8,8]

low = 0, high = 8
mid = 4 (even index), nums[mid]=3, nums[mid+1]=3 → pair exists → search right
low = 6, high = 8
mid = 7 → make even → mid=6, nums[6]=4, nums[7]=8 → not equal → search left
high = 6
low = 6, high = 6 → stop → nums[6] = 2 is the answer

Output: 2
------------------------------------------------------------

Final Notes:
- Brute Force: simple but O(n).
- Optimal: binary search with O(log n).
- This is a classic interview question to test binary search variation.
"""

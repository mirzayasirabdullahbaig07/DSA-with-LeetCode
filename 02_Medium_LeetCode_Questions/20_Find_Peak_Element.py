"""
LeetCode: Find Peak Element

Problem:
---------
You are given a 0-indexed integer array `nums`. A peak element is an element 
that is strictly greater than its neighbors.

Task:
-----
Find a peak element and return its index. If the array contains multiple peaks, 
return the index of any peak.

Notes:
-----
- You may imagine nums[-1] = nums[n] = -∞ (negative infinity)
- Must run in O(log n) time for optimal solution.

Example 1:
----------
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element at index 2

Example 2:
----------
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Peaks can be at index 1 (2) or index 5 (6)

Constraints:
------------
1 <= nums.length <= 1000
-2^31 <= nums[i] <= 2^31 - 1
nums[i] != nums[i + 1] for all valid i

------------------------------------------------------------
Brute Force Solution (Linear Scan)
------------------------------------------------------------
Intuition:
----------
1. Check edge cases:
    - Array has only one element → it's a peak
    - First element > second → first is peak
    - Last element > second last → last is peak
2. Iterate through the array:
    - For each element (except first and last), check if it is greater than neighbors
    - Return index if true

Time Complexity: O(n)
Space Complexity: O(1)
------------------------------------------------------------
Code Implementation (Brute Force):
------------------------------------------------------------
"""

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Edge case: only one element
        if n == 1:
            return 0
        
        # Check first element
        if nums[0] > nums[1]:
            return 0
        
        # Check last element
        if nums[n - 1] > nums[n - 2]:
            return n - 1
        
        # Check middle elements
        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i

"""
------------------------------------------------------------
Dry Run (Brute Force):
------------------------------------------------------------
Input: nums = [1,2,3,1]
n = 4
i = 1 -> nums[1]=2, neighbors=1 & 3 -> not peak
i = 2 -> nums[2]=3, neighbors=2 & 1 -> peak found -> return 2
Output: 2
------------------------------------------------------------
Conclusion:
- Simple and easy to implement
- Works for small arrays
- Not optimal for large inputs
"""

"""
------------------------------------------------------------
Optimal Solution (Binary Search)
------------------------------------------------------------
Intuition:
----------
- Use binary search because array allows O(log n) search
- If mid element < right neighbor → peak is on right
- Else → peak is on left
- Always move towards greater neighbor
- Edge cases: check first and last elements separately

Time Complexity: O(log n)
Space Complexity: O(1)
------------------------------------------------------------
Code Implementation (Binary Search):
------------------------------------------------------------
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Edge cases
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return n - 1
        
        # Binary search
        low, high = 1, n - 2
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check if mid is peak
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            
            # Move left or right depending on slope
            if nums[mid] > nums[mid + 1]:
                high = mid - 1
            else:
                low = mid + 1

"""
------------------------------------------------------------
Dry Run (Binary Search):
------------------------------------------------------------
Input: nums = [1,2,3,1]
low=1, high=2
mid=(1+2)//2=1 -> nums[1]=2, nums[2]=3 -> nums[mid]<nums[mid+1] -> move right
low=2, high=2 -> mid=2 -> nums[2]=3, nums[1]=2, nums[3]=1 -> peak found -> return 2
Output: 2
------------------------------------------------------------
Conclusion:
- Efficient for large arrays
- Classic example of binary search on unsorted array using neighbor comparison
"""

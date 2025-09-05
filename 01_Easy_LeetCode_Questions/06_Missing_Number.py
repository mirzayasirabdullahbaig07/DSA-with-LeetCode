"""
Problem: Missing Number (LeetCode 268)
---------------------------------------
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Examples:
---------
Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: 
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
2 is the missing number.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: 
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
2 is the missing number.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation:
n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
8 is the missing number.
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Approach: Sum Formula Method
        ----------------------------
        - The numbers should form the sequence 0, 1, 2, …, n.
        - Formula for sum of first n natural numbers: n * (n + 1) // 2
        - Find expected_sum using the formula.
        - Find actual_sum from the array.
        - The missing number = expected_sum - actual_sum

        Example Dry Run:
        ----------------
        nums = [3,0,1]
        n = 3
        expected_sum = 3 * (3+1) // 2 = 6
        actual_sum   = sum([3,0,1]) = 4
        missing = 6 - 4 = 2
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


"""
Complexity Analysis:
---------------------
Time Complexity: O(n)
    - We compute sum(nums) which requires scanning all elements once.
    - Rest are O(1) operations.

Space Complexity: O(1)
    - Uses only a few variables, no extra data structures.
"""

# ------------------ TEST CASES ------------------
if __name__ == "__main__":
    s = Solution()

    # Test case 1
    arr1 = [3,0,1]
    print("Input:", arr1, "→ Missing number:", s.missingNumber(arr1))  
    # Expected: 2

    # Test case 2
    arr2 = [0,1]
    print("Input:", arr2, "→ Missing number:", s.missingNumber(arr2))  
    # Expected: 2

    # Test case 3
    arr3 = [9,6,4,2,3,5,7,0,1]
    print("Input:", arr3, "→ Missing number:", s.missingNumber(arr3))  
    # Expected: 8

"""
LeetCode Problem: 485. Max Consecutive Ones

STATEMENT:
-----------
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. 
The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:
-------------
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        METHOD:
        --------
        - Initialize two variables:
            count = to count current streak of 1's
            max_count = to store the maximum streak found
        - Traverse the array:
            If num == 1 → increment count, update max_count
            If num == 0 → reset count to 0
        - Return max_count at the end
        """
        count = 0
        max_count = 0
        
        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        
        return max_count


"""
DRY RUN:
---------
Example: nums = [1, 1, 0, 1, 1, 1]

Step 1: Start with count=0, max_count=0
Step 2: num=1 → count=1, max_count=1
Step 3: num=1 → count=2, max_count=2
Step 4: num=0 → count=0 (reset)
Step 5: num=1 → count=1, max_count=2
Step 6: num=1 → count=2, max_count=2
Step 7: num=1 → count=3, max_count=3

Final Answer = 3
"""

"""
TIME & SPACE COMPLEXITY:
------------------------
- Time Complexity: O(n) → We scan the array once
- Space Complexity: O(1) → Only two variables used (count, max_count)
"""

# ---------------------------
# TEST CASES
# ---------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))  # Output: 3
    print(sol.findMaxConsecutiveOnes([1,0,1,1,0,1]))  # Output: 2
    print(sol.findMaxConsecutiveOnes([0,0,0]))        # Output: 0
    print(sol.findMaxConsecutiveOnes([1,1,1,1]))      # Output: 4

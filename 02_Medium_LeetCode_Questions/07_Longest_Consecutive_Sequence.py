"""
LEETCODE PROBLEM: 128. Longest Consecutive Sequence
---------------------------------------------------

QUESTION STATEMENT:
-------------------
Given an unsorted array of integers nums, return the length of the longest 
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


EXAMPLES:
---------
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation:
The longest consecutive sequence is [1,2,3,4]. Hence length = 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation:
The longest consecutive sequence is [0,1,2,3,4,5,6,7,8]. Hence length = 9.

Example 3:
Input: nums = [1,0,1,2]
Output: 3
Explanation:
The longest consecutive sequence is [0,1,2]. Hence length = 3.


CONSTRAINTS:
------------
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9


APPROACH / TECHNIQUE:
---------------------
We use the "Set + Sequence Expansion" technique:
1. Convert nums into a set for O(1) lookups and uniqueness.
2. Iterate over each number in the set.
3. If (num - 1) is not in the set → num could be the start of a sequence.
4. Expand forward (num + 1, num + 2, …) while elements exist in the set.
5. Track the streak length and update the maximum.

WHY THIS WORKS:
---------------
- We only start counting when we find the smallest number in a sequence.
- Each number is visited at most once in expansion.
- This ensures overall O(n) complexity.


TIME COMPLEXITY:
----------------
- Creating the set = O(n)
- Iterating and expanding = O(n) overall
Total = O(n)

SPACE COMPLEXITY:
-----------------
- The set stores up to n elements → O(n)


DRY RUN:
--------
nums = [100,4,200,1,3,2]

Step 1: num_set = {1,2,3,4,100,200}
Step 2: Iterate:
    - num=1 → (0 not in set) → start sequence
      streak = [1,2,3,4] → length=4 → longest=4
    - num=2 → (1 in set) → skip
    - num=3 → (2 in set) → skip
    - num=4 → (3 in set) → skip
    - num=100 → (99 not in set) → streak=[100] → length=1
    - num=200 → (199 not in set) → streak=[200] → length=1
Step 3: Max streak length = 4

Final Output = 4
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)  # O(n) space
        longest = 0

        for num in num_set:
            # Check if it's the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Expand the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest

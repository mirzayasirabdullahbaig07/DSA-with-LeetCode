"""
LEETCODE PROBLEM: 229. Majority Element II
------------------------------------------

STATEMENT:
----------
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

EXAMPLES:
---------
Example 1:
Input:  nums = [3,2,3]
Output: [3]

Example 2:
Input:  nums = [1]
Output: [1]

Example 3:
Input:  nums = [1,2]
Output: [1,2]

CONSTRAINTS:
------------
- 1 <= nums.length <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9

FOLLOW-UP:
----------
- Solve the problem in O(n) time and O(1) space.


TECHNIQUE / APPROACH:
----------------------
We use the **Boyer-Moore Voting Algorithm (Extended)**:
1. Since at most 2 elements can appear more than ⌊n/3⌋ times, we track two candidates (cand1, cand2).
2. First pass:
   - Count votes for candidates.
   - If count becomes zero, replace with new candidate.
3. Second pass:
   - Verify the candidates by checking actual occurrences.
4. Return all verified candidates.


DRY RUN:
--------
nums = [3,2,3]

First pass (finding candidates):
- cand1 = 3, count1 = 1
- cand2 = 2, count2 = 1
- Next 3 → cand1 matches → count1 = 2

Second pass (verify counts):
- count(3) = 2 > 3//3 → include [3]

Output: [3]


TIME COMPLEXITY:
----------------
- O(n) → One pass to choose candidates, one pass to verify.

SPACE COMPLEXITY:
-----------------
- O(1) → Only variables for two candidates and counters.
"""


from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Step 1: Find potential candidates
        cand1 = cand2 = None
        count1 = count2 = 0
        
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 2: Verify candidates
        result = []
        n = len(nums)
        for cand in [cand1, cand2]:
            if cand is not None and nums.count(cand) > n // 3:
                result.append(cand)
        
        return result

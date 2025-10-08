"""
LEETCODE PROBLEM: 169. Majority Element
---------------------------------------

QUESTION STATEMENT:
-------------------
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

EXAMPLES:
---------
Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2


CONSTRAINTS:
------------
- n == nums.length
- 1 <= n <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9
- The majority element always exists.


APPROACH / TECHNIQUE:
---------------------
We use the **Boyer-Moore Voting Algorithm**:
1. Maintain a `count` and a candidate `element`.
2. Traverse the array:
   - If `count == 0`, set current element as the new candidate.
   - If current element == candidate → increment count.
   - Else → decrement count.
3. The candidate at the end is guaranteed to be the majority element 
   (since it always exists by problem constraint).

WHY THIS WORKS:
---------------
- Majority element appears more than ⌊n/2⌋ times.
- All other elements combined cannot "cancel it out" fully, 
  so it remains as the candidate after one pass.


TIME COMPLEXITY:
----------------
- O(n) → one pass through the array.

SPACE COMPLEXITY:
-----------------
- O(1) → only two variables used.


DRY RUN:
--------
nums = [2,2,1,1,1,2,2]

Start:
count = 0, element = None

Step 1: num=2
count==0 → element=2, count=1

Step 2: num=2
num == element → count=2

Step 3: num=1
num != element → count=1

Step 4: num=1
num != element → count=0

Step 5: num=1
count==0 → element=1, count=1

Step 6: num=2
num != element → count=0

Step 7: num=2
count==0 → element=2, count=1

Final Answer = 2 (majority element)
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = None

        for i in range(len(nums)):
            if count == 0:
                element = nums[i]
                count = 1
            elif nums[i] == element:
                count += 1
            else:
                count -= 1

        return element

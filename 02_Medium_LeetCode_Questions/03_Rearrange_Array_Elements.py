"""
LEETCODE PROBLEM: 2149. Rearrange Array Elements by Sign
--------------------------------------------------------

QUESTION STATEMENT:
-------------------
You are given a 0-indexed integer array nums of even length consisting of an equal number of 
positive and negative integers.

You should return the array of nums such that the array follows the given conditions:
1. Every consecutive pair of integers have opposite signs.
2. For all integers with the same sign, the order in which they were present in nums is preserved.
3. The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the aforementioned conditions.


EXAMPLES:
---------
Example 1:
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
- Positive integers in nums: [3,1,2]
- Negative integers in nums: [-2,-5,-4]
- Merging them alternately → [3,-2,1,-5,2,-4]

Example 2:
Input: nums = [-1,1]
Output: [1,-1]
Explanation:
- Positive = [1], Negative = [-1]
- Rearranged → [1,-1]


CONSTRAINTS:
------------
- 2 <= nums.length <= 2 * 10^5
- nums.length is even
- 1 <= |nums[i]| <= 10^5
- nums consists of equal number of positive and negative integers


APPROACH / TECHNIQUE:
---------------------
We use the "Two Array Splitting + Alternating Merge" technique:
1. Traverse nums → collect positives into 'pos', negatives into 'neg'.
2. Iterate through both lists in parallel.
3. Append one positive, then one negative into the result.
4. Return the result.

WHY THIS WORKS:
---------------
- Ensures alternating signs (because we add pos[i] then neg[i]).
- Preserves the relative order of positives and negatives.
- Always starts with a positive (since we begin merging with pos[0]).

TIME COMPLEXITY:
----------------
- Extract positives = O(n)
- Extract negatives = O(n)
- Merge lists = O(n)
Total = O(n)

SPACE COMPLEXITY:
-----------------
- Storing positives = O(n/2)
- Storing negatives = O(n/2)
- Final result = O(n)
Total = O(n)

DRY RUN:
--------
nums = [3,1,-2,-5,2,-4]
pos = [3,1,2]
neg = [-2,-5,-4]
result = []

Step 1: Add pos[0]=3, neg[0]=-2 → [3,-2]
Step 2: Add pos[1]=1, neg[1]=-5 → [3,-2,1,-5]
Step 3: Add pos[2]=2, neg[2]=-4 → [3,-2,1,-5,2,-4]

Final Output = [3,-2,1,-5,2,-4]
"""

from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if x > 0]   # extract positives
        neg = [x for x in nums if x < 0]   # extract negatives
        
        result = []
        # merge them alternately
        for i in range(len(pos)):
            result.append(pos[i])   # add positive
            result.append(neg[i])   # add negative
        
        return result

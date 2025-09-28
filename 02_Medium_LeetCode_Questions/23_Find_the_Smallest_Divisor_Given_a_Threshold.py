"""
LeetCode 1283. Find the Smallest Divisor Given a Threshold

------------------------------------------------------------
Problem:
------------------------------------------------------------
Given an array of integers nums and an integer threshold, we will 
choose a positive integer divisor. For each element in nums, divide 
it by the divisor and round up (ceiling). Then, sum all results.

Return the smallest divisor such that the sum is less than 
or equal to threshold.

------------------------------------------------------------
Example 1:
------------------------------------------------------------
Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation:
- divisor = 1 → sum = 17 (too high)
- divisor = 4 → sum = 7 (too high)
- divisor = 5 → sum = 5 (valid ✅)

------------------------------------------------------------
Example 2:
------------------------------------------------------------
Input: nums = [44,22,33,11,1], threshold = 5
Output: 44

------------------------------------------------------------
Constraints:
------------------------------------------------------------
1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^6
nums.length <= threshold <= 10^6

------------------------------------------------------------
Brute Force Solution (Try Every Possible Divisor):
------------------------------------------------------------
Intuition:
- Try every divisor from 1 up to max(nums).
- For each divisor, compute sum of ceil(num/divisor).
- Return the first divisor that keeps sum <= threshold.

Time Complexity: O(max(nums) * n)
Space Complexity: O(1)

------------------------------------------------------------
Code Implementation (Brute Force):
------------------------------------------------------------
"""

import math
from typing import List

class Solution:
    def getThreshold(self, divisor, nums, threshold):
        total = 0
        for num in nums:
            total += math.ceil(num / divisor)  # Divide and round up
        return total <= threshold

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        max_num = max(nums)
        for divisor in range(1, max_num + 1):
            if self.getThreshold(divisor, nums, threshold):
                return divisor
        return max_num


"""
------------------------------------------------------------
Dry Run (Brute Force):
------------------------------------------------------------
Input: nums = [1,2,5,9], threshold = 6

divisor = 1 → sum = 17 ❌
divisor = 2 → sum = 10 ❌
divisor = 3 → sum = 7  ❌
divisor = 4 → sum = 7  ❌
divisor = 5 → sum = 5 ✅ return 5

Answer = 5

------------------------------------------------------------
Optimal Solution (Binary Search on Answer):
------------------------------------------------------------
Observation:
- As divisor increases → sum decreases (monotonic behavior).
- Search space = [1, max(nums)].
- Binary search to find the smallest divisor that satisfies threshold.

Algorithm:
1. low = 1, high = max(nums).
2. While low <= high:
   - mid = (low+high)//2
   - If sum(mid) <= threshold → store answer, move left (high = mid-1).
   - Else → move right (low = mid+1).
3. Return stored answer.

Time Complexity: O(n * log(max(nums)))
Space Complexity: O(1)

------------------------------------------------------------
Code Implementation (Binary Search):
------------------------------------------------------------
"""

import math
from typing import List

class Solution:
    def calTotal(self, nums, divisor):
        total = 0
        for num in nums:
            total += math.ceil(num / divisor)
        return total

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            total = self.calTotal(nums, mid)

            if total <= threshold:
                ans = mid          # valid, try smaller
                high = mid - 1
            else:
                low = mid + 1      # invalid, try larger
        return ans


"""
------------------------------------------------------------
Dry Run (Binary Search):
------------------------------------------------------------
Input: nums = [1,2,5,9], threshold = 6

low = 1, high = 9
mid = 5 → total = 5 ✅ valid → ans=5, high=4
(mid loop ends)

Answer = 5

------------------------------------------------------------
Final Notes:
------------------------------------------------------------
- Brute Force: easy but O(max(nums)*n) → too slow for large inputs.
- Optimal: binary search O(n log(max(nums))) → efficient and 
  works well in practice.
- Key Trick: Search space is not indices but "possible divisors".

👉 Classic binary search variation: search on answer space.
"""

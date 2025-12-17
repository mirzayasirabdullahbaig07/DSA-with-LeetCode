"""
LeetCode 416: Partition Equal Subset Sum
---------------------------------------

Problem Summary:
Given an integer array `nums`, determine whether it can be partitioned
into two subsets such that the sum of elements in both subsets is equal.

Key Observations:
1. If the total sum of the array is odd, it is impossible to divide it
   into two subsets with equal sum.
2. If the total sum is even, the problem reduces to checking whether
   there exists a subset whose sum is equal to (total_sum // 2).

Approach (Dynamic Programming – 0/1 Knapsack):
- This problem is a variation of the classic 0/1 Knapsack problem.
- We use a boolean DP array where:
    dp[i] = True  → A subset with sum `i` can be formed using the numbers seen so far.
    dp[i] = False → Otherwise.

Initialization:
- dp[0] = True because a subset sum of 0 is always possible (empty subset).
- All other dp values are initialized to False.

Transition:
- For each number `num` in the array:
    - Iterate backwards from `target` down to `num`
    - Update dp[i] as:
        dp[i] = dp[i] OR dp[i - num]
    - Backward iteration ensures each number is used at most once
      (0/1 knapsack behavior).

Final Answer:
- If dp[target] is True, we can partition the array into two subsets
  with equal sum.
- Otherwise, it is not possible.

Time Complexity:
- O(n * target), where n is the number of elements
  and target = total_sum // 2.

Space Complexity:
- O(target), using a 1D DP array for optimization.

Why This Works:
- We only need to check half of the total sum because if one subset
  has sum = total_sum // 2, the remaining elements automatically form
  the other subset with the same sum.
"""

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # If total sum is odd, it's impossible to split into two equal subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        n = len(nums)
        
        # dp[i] will be True if a subset sum of i is possible
        dp = [False] * (target + 1)
        dp[0] = True  # Zero sum is always possible
        
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]

# Example usage
sol = Solution()
print(sol.canPartition([1, 5, 11, 5]))  # True
print(sol.canPartition([1, 2, 3, 5]))   # False

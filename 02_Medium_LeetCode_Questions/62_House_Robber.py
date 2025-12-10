"""
This problem is about choosing the maximum money you can rob from a list of houses
where robbing two adjacent houses is not allowed. Each house has an amount of money
given in the array nums.

To solve this, we use Dynamic Programming with an optimized space approach.

The idea is:
- At each house index i, you have two choices:
  1. Pick the current house: then you must add nums[i] to the solution of i-2 
     (because adjacent houses cannot be robbed).
  2. Skip the current house: then the result is simply the best solution at i-1.

The recurrence relation is:
    dp[i] = max(nums[i] + dp[i-2], dp[i-1])

But instead of storing the entire dp array, we only keep two variables:
- prev2 = dp[i-2]
- prev1 = dp[i-1]

We iterate from index 2 to n-1, updating these values.

Step-by-step logic:
1. If there is only one house, return nums[0].
2. prev2 starts as nums[0].
3. prev1 is the best choice between the first two houses: max(nums[0], nums[1]).
4. For every next house:
       pick = nums[i] + prev2
       not_pick = prev1
       curr = max(pick, not_pick)
   Then shift the window:
       prev2 = prev1
       prev1 = curr
5. At the end, prev1 contains the maximum amount we can rob.

Time Complexity:
    O(n), because we loop through the array once.

Space Complexity:
    O(1), because we only use two variables.

Final Code:
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        prev2 = nums[0]      # dp[i-2]
        prev1 = max(nums[0], nums[1])   # dp[i-1]

        for i in range(2, n):
            pick = nums[i] + prev2
            not_pick = prev1
            curr = max(pick, not_pick)

            prev2 = prev1
            prev1 = curr

        return prev1
"""
This gives the maximum money the robber can collect without alerting the police.
"""

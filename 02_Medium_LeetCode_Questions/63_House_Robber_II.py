"""
This problem is a variation of the original House Robber problem, but with one key difference:
the houses are arranged in a circle. This means the first house and the last house are adjacent.
Because adjacent houses cannot both be robbed, we cannot rob both house 0 and house n-1 in the
same plan.

To solve this, we break the problem into two independent linear robber problems:

Case 1:
    Rob houses from index 0 to index n-2 (exclude the last house).
Case 2:
    Rob houses from index 1 to index n-1 (exclude the first house).

We compute the maximum money for both cases using the same logic as House Robber I,
and the final result is the maximum of these two results.

We use a helper function rob_line(arr) that solves the normal (linear) House Robber problem.

Inside rob_line:
- prev represents dp[i-1] (best up to previous house)
- prev2 represents dp[i-2] (best up to the house before previous)
- For each house:
        pick = arr[i] + prev2        # rob this house + best from i-2
        not_pick = prev              # skip this house (best from i-1)
        curr = max(pick, not_pick)
  Then shift the sliding window:
        prev2 = prev
        prev = curr

At the end, prev contains the best possible amount for this linear arrangement.

Steps:
1. If there is only one house, return its value.
2. Compute case1 = rob houses from index 0 to n-2.
3. Compute case2 = rob houses from index 1 to n-1.
4. Return max(case1, case2).

Time Complexity:
    O(n), because we process each house once.

Space Complexity:
    O(1), due to using only constant extra variables.

Final Code Reference:
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        def rob_line(arr):
            prev = arr[0]
            prev2 = 0
            
            for i in range(1, len(arr)):
                pick = arr[i] + prev2
                not_pick = prev
                curr = max(pick, not_pick)
                
                prev2 = prev
                prev = curr
            
            return prev
        
        case1 = rob_line(nums[:-1])
        case2 = rob_line(nums[1:])
        
        return max(case1, case2)
"""
This solution correctly handles the circular arrangement and ensures maximum money can be robbed
without triggering security alarms.
"""

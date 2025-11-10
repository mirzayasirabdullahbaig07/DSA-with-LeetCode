"""
 LeetCode 55 — Jump Game | All Python Solutions Explained
-----------------------------------------------------------

 Problem Statement:
You are given an integer array 'nums' where each element 'nums[i]' represents 
the maximum jump length you can move forward from that index.

Starting at index 0, determine whether you can reach the last index.

 Example 1:
Input: nums = [2,3,1,1,4]
Output: True
Explanation:
- Start at index 0 → you can jump at most 2 steps ahead.
- Jump to index 1 → nums[1] = 3 allows you to reach even further.
- From index 1, you can directly reach index 4 (the last index).
Hence, the output is True.

 Example 2:
Input: nums = [3,2,1,0,4]
Output: False
Explanation:
- Start at index 0 → maximum reach is index 3.
- But when you arrive at index 3, nums[3] = 0, so you cannot move further.
Thus, you can never reach the last index.

-------------------------------------------------------
 Intuition Behind the Problem:
The challenge is to determine whether the **last index** can be reached 
based on the jumps defined by the elements in the array.

There are multiple ways to solve this — from brute force to optimal greedy.

Let’s explore all of them step by step.

-------------------------------------------------------
1 Brute Force (Recursive DFS)
-------------------------------------------------------
 Idea:
Try all possible jumps recursively until reaching the end. 
At each index, you explore all possible jump lengths and recursively check if the end is reachable.

 Code:
"""
class Solution:
    def canJump(self, nums):
        def dfs(i):
            if i >= len(nums) - 1:
                return True
            for jump in range(1, nums[i] + 1):
                if dfs(i + jump):
                    return True
            return False
        return dfs(0)
"""
 Example: nums = [2,3,1,1,4]
- Start at i=0 → possible jumps: 1 or 2.
- Try i=1 → possible jumps: up to 3 → can reach i=4.
- Return True.

Example: nums = [3,2,1,0,4]
- Start at i=0 → jumps: 1,2,3.
- From i=3 → nums[3] = 0 → stuck .
- Return False.

 Complexity:
- Time: O(2ⁿ)
- Space: O(n)
 Too slow for large inputs.

-------------------------------------------------------
2 Dynamic Programming (Top-Down Memoization)
-------------------------------------------------------
 Idea:
Same recursive logic, but use memoization to remember results of subproblems 
(avoid re-exploring the same index).

 Code:
"""
class Solution:
    def canJump(self, nums):
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(nums) - 1:
                return True
            for jump in range(1, nums[i] + 1):
                if dfs(i + jump):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return dfs(0)
"""
 Example: nums = [2,3,1,1,4]
- dfs(0): explore jumps → dfs(1) → dfs(4) 
- Store results in memo for reuse.
- Return True.

Example: nums = [3,2,1,0,4]
- dfs(0) → dfs(1), dfs(2), dfs(3) → stuck.
- Memo stores False → no repeated work.

 Complexity:
- Time: O(n²)
- Space: O(n)
 Faster but not yet optimal.

-------------------------------------------------------
3 Dynamic Programming (Bottom-Up)
-------------------------------------------------------
 Idea:
Start from the end and mark positions that can reach the goal. 
Move backward through the array, checking if each position can reach a "good" position.

 Code:
"""
class Solution:
    def canJump(self, nums):
        n = len(nums)
        dp = [False] * n
        dp[-1] = True  # last index is always reachable from itself

        for i in range(n - 2, -1, -1):
            furthest_jump = min(i + nums[i], n - 1)
            for j in range(i + 1, furthest_jump + 1):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]
"""
 Example: nums = [2,3,1,1,4]
- Start from end:
  dp[4] = True
  i=3 → can reach dp[4] → dp[3]=True
  i=2 → can reach dp[3] → dp[2]=True
  i=1 → can reach dp[4] → dp[1]=True
  i=0 → can reach dp[1] → dp[0]=True 
- Result: True

Example: nums = [3,2,1,0,4]
  dp[4]=True
  i=3 → no valid jump → dp[3]=False
  i=2 → can reach only dp[3]=False → dp[2]=False
  i=1 → same → dp[1]=False
  i=0 → max reach 3, but dp[3]=False → dp[0]=False 
- Result: False

 Complexity:
- Time: O(n²)
- Space: O(n)
 Easier to visualize, still not optimal.

-------------------------------------------------------
4 Greedy Approach (Optimal)
-------------------------------------------------------
 Intuition:
Track the **farthest index** reachable while moving forward. 
If the current index is ever greater than this farthest index, you’re stuck.

 Code:
"""
class Solution:
    def canJump(self, nums):
        max_index = 0
        for i in range(len(nums)):
            if i > max_index:
                return False
            max_index = max(max_index, i + nums[i])
        return True
"""
 Step-by-Step Dry Run:

Example: nums = [2,3,1,1,4]
i = 0 → max_index = max(0,0+2)=2
i = 1 → max_index = max(2,1+3)=4 
i = 2 → max_index = 4
i = 3 → max_index = 4
i = 4 → reached end 
Output: True

Example: nums = [3,2,1,0,4]
i = 0 → max_index = 3
i = 1 → max_index = 3
i = 2 → max_index = 3
i = 3 → max_index = 3
i = 4 → i(4)>max_index(3) stuck
Output: False

 Complexity:
- Time: O(n)
- Space: O(1)
 Most efficient, clean, and ideal for interviews.

-------------------------------------------------------
 Comparison Table:

| Approach               | Time  | Space | Description             |
|------------------------|--------|--------|--------------------------|
| Brute Force (DFS)      | O(2ⁿ)  | O(n)   | Tries all possibilities  |
| DP (Top-Down)          | O(n²)  | O(n)   | Uses memoization         |
| DP (Bottom-Up)         | O(n²)  | O(n)   | Iterative improvement    |
| Greedy (Optimal)       | O(n)   | O(1)   | Tracks farthest reach    |

-------------------------------------------------------
 Key Takeaways:
- **Brute Force** builds the foundation by exploring all paths.
- **Dynamic Programming** improves efficiency by reusing results.
- **Greedy** simplifies the problem into a one-pass range check.
- Jump Game demonstrates how **optimization evolves** from recursion to DP to Greedy.

 The Greedy approach is the most optimal and is widely used in interviews.
 Clean, fast, and intuitive — O(n) time and O(1) space.
"""



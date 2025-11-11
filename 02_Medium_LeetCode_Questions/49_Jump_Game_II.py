"""
 Problem: Jump Game II (LeetCode #45)
Level: Medium
Topic: Greedy / Dynamic Programming
Companies: Amazon, Google, Microsoft, Facebook

---

 Problem Statement:
You are given a 0-indexed array `nums` where each element `nums[i]` represents 
the maximum length of a forward jump you can make from that index.

You start at index 0 and need to reach the last index in the **minimum number of jumps**.
You can assume that you can always reach the last index.

---

 Example 1:
Input: nums = [2,3,1,1,4]
Output: 2

Explanation:
 From index 0, nums[0] = 2 → You can jump to index 1 or 2.
Choose index 1 (because nums[1]=3 allows you to go farthest).
 From index 1, jump directly to the last index (index 4).
 Minimum jumps required = 2.

---

 Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Explanation:
 Start at index 0, nums[0]=2 → You can go to 1 or 2.
 From index 1, nums[1]=3 → Jump to the last index (4).
 Total jumps = 2.

---

 Goal:
Return the minimum number of jumps required to reach the last index.

---

 Approach 1: Recursive (Brute Force)
Idea:
Try all possible jumps from the current index and take the minimum among them.
This is a direct search of all paths — simple but very slow.

Steps:
1 From current index, you can jump from 1 → nums[i] steps ahead.
2 Recursively find the minimum jumps from those future indices.
3 Return the minimum value + 1 (for current jump).

Base Case:
- If `index >= last index`: return number of jumps taken so far.

---

 Recursive Code:
"""
class Solution:
    def solve(self, index, jump, lastIndex, nums):
        if index >= lastIndex:
            return jump
        minJump = float("inf")
        for i in range(1, nums[index] + 1):
            minJump = min(minJump, self.solve(index + i, jump + 1, lastIndex, nums))
        return minJump

    def jump(self, nums: List[int]) -> int:
        return self.solve(0, 0, len(nums) - 1, nums)
"""
---

 Recursive Explanation (Example 1: [2,3,1,1,4]):

- Start at index 0 → nums[0]=2 → can jump to index 1 or 2.
- Jump to index 1:
    - nums[1]=3 → can jump to 2, 3, or 4.
    - Jump to index 4 (goal) → jumps = 2 
- Jump to index 2:
    - nums[2]=1 → jump to 3
    - nums[3]=1 → jump to 4 → jumps = 3 
 Minimum = 2 jumps.

 Time Complexity: Exponential (O(2^n))
 Space Complexity: O(n) (due to recursion stack)

 Disadvantage:
Recomputes many subproblems, extremely slow for large inputs.

---

 Approach 2: Greedy (Optimal)
Idea:
Use a **greedy level-based strategy** (like BFS but in array form).
We track how far we can go with the current jump and when to increase jump count.

Steps:
1 Initialize variables:
   - `jumps = 0`
   - `left = 0`, `right = 0` (the current range we can reach)
2 While we haven’t reached the end:
   - Find the farthest index reachable in current window [left, right].
   - Move to the next window (right + 1 → farthest).
   - Increment jump count.
3 Stop when right >= last index.

---

 Greedy Code:
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        left = 0
        right = 0

        while right < n - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            jumps += 1

        return jumps
"""
---

 Greedy Explanation (Example 1: [2,3,1,1,4]):

Iteration 1:
- left = 0, right = 0 → current range [0]
- i = 0 → farthest = max(0, 0+2) = 2
 Move window → left = 1, right = 2
 jumps = 1

Iteration 2:
- Range [1,2]
- i=1 → farthest = max(0, 1+3) = 4
- i=2 → farthest = max(4, 2+1) = 4
 Move window → left = 3, right = 4
 jumps = 2
 right (4) >= n-1 (4) → stop

 Minimum jumps = 2.

---

 Greedy Explanation (Example 2: [2,3,0,1,4]):

Iteration 1:
- left=0, right=0 → i=0 → farthest = 2
 left=1, right=2 → jumps=1

Iteration 2:
- Range [1,2]
- i=1 → farthest = 4 (1+3)
- i=2 → farthest = 4 (no change)
 left=3, right=4 → jumps=2
 right >= last index → stop

 Minimum jumps = 2.

---

 Time and Space Complexity:
 Time: O(n) → each index visited once.
 Space: O(1) → only a few variables used.

---

 Summary:

| Approach | Idea | Time | Space | Feasible for Large Inputs |
|-----------|------|------|--------|-----------------------------|
| Recursive | Try all paths | Exponential | O(n) |  No |
| Greedy | Expand farthest reachable range | O(n) | O(1) |  Yes |

---

 Final Takeaway:
- Brute force recursion is conceptually simple but inefficient.
- The Greedy “level expansion” approach is optimal and elegant.
- Always think in terms of *reachability levels* in such array jump problems.

---
"""

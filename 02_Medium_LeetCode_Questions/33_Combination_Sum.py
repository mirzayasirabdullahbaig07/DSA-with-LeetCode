"""
# Problem: Combination Sum
# =========================

# Problem Statement:
# Given an array of distinct integers `candidates` and a target integer `target`,
# return all **unique combinations** of `candidates` where the chosen numbers sum to `target`.
# You may return the combinations in any order.
#
# The same number may be chosen from `candidates` an unlimited number of times.
# Two combinations are unique if the frequency of at least one number differs.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]

# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:
# Input: candidates = [2], target = 1
# Output: []

# Constraints:
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# 1 <= target <= 40
# All elements in candidates are distinct.

# ----------------------------------------------------------------------

# Intuition:
# This problem is similar to the **coin change problem**.
# Think of each number in `candidates` as a type of coin.
# You can pick the same number (coin) multiple times to reach the target sum.
#
# At each step, you have two choices:
# 1. **Include** the current number (stay on the same index — since reuse is allowed)
# 2. **Exclude** the current number (move to the next index)
#
# Using backtracking, we explore both choices recursively until we reach a valid sum.

# ----------------------------------------------------------------------

# Technique Used: Backtracking (DFS Tree Exploration)
# -------------------------------------------------------
# - Explore all possible paths by including or excluding candidates.
# - Prune (cut off) paths early when the current total exceeds the target.
# - Use the same index for reuse, and increment the index only when skipping.
# - When total == target → store a copy of the current combination.

# ----------------------------------------------------------------------

# Step-by-Step Problem Logic:
# 1. Start recursion with index = 0, total = 0, and an empty list (subset).
# 2. If total == target → add subset copy to results.
# 3. If total > target or index == len(candidates) → stop exploring (invalid path).
# 4. Two recursive choices:
#     (a) Include candidates[index] → call recursion with same index (reuse allowed)
#     (b) Exclude candidates[index] → move to next index
# 5. Backtrack (remove last added number) after exploring each path.

# ----------------------------------------------------------------------

# Python Code Implementation:
"""

from typing import List

class Solution:
    def solve(self, index: int, total: int, subset: List[int],
              nums: List[int], target: int, result: List[List[int]]):
        # Base Case 1: If total equals target → found a valid combination
        if total == target:
            result.append(subset.copy())  # append copy to avoid reference issues
            return

        # Base Case 2: If total exceeds target or reached end of array → invalid path
        if total > target or index >= len(nums):
            return

        # ------------------------------------------------------------------
        # Choice 1 → Include nums[index] (reuse allowed, so index stays same)
        subset.append(nums[index])       # take the number
        self.solve(index, total + nums[index], subset, nums, target, result)
        subset.pop()                     # backtrack (remove last added number)
        # ------------------------------------------------------------------

        # Choice 2 → Skip nums[index] (move to next number)
        self.solve(index + 1, total, subset, nums, target, result)

    # Main function
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(0, 0, [], candidates, target, result)
        return result

# ----------------------------------------------------------------------
"""
# Code Explanation:
# --------------------
# - The helper function `solve()` recursively builds combinations.
# - We include or skip each candidate, forming a decision tree.
# - The backtrack (subset.pop()) ensures we remove the last added element before
#   exploring other options (to restore previous state).
# - Using `.copy()` ensures that each valid subset stored in results is independent.

# ----------------------------------------------------------------------

# Example Dry Run:
# -------------------
# Input: candidates = [2, 3, 6, 7], target = 7

# Start: index=0, total=0, subset=[]
#
# ➤ Include 2 → [2], total=2
# ➤ Include 2 → [2,2], total=4
# ➤ Include 2 → [2,2,2], total=6
# ➤ Include 2 → [2,2,2,2], total=8  (exceeds target, backtrack)
# ➤ Skip 2 → [2,2,3], total=7  (add to result)
# ➤ Backtrack and try skipping 2
# ➤ Include 7 → [7], total=7  (add to result)
#
# Result = [[2,2,3], [7]]

# ----------------------------------------------------------------------

# Time Complexity:
# --------------------
# O(N^(T/M)) where:
# - N = number of candidates
# - T = target
# - M = minimum value in candidates
#
# Because at most, we can take T/M numbers to reach target.
# Each choice generates a branch, leading to exponential growth.

# Space Complexity:
# ---------------------
# O(T/M)
# - Depth of recursion tree proportional to maximum number of elements
#   needed to reach target (T / smallest candidate).
# - Subset list grows linearly with recursion depth.

# ----------------------------------------------------------------------

# Real-world Analogy:
# -----------------------
# Imagine you’re making exact change using different coin denominations.
# You can use each coin as many times as needed.
# You try every possible combination of coins until you reach the target amount.
# If you exceed the amount, you stop that path — just like pruning invalid branches.

# ----------------------------------------------------------------------

# Example Run:
solution = Solution()
candidates = [2, 3, 6, 7]
target = 7
print("All unique combinations that sum to target:")
print(solution.combinationSum(candidates, target))

# Output:
# All unique combinations that sum to target:
# [[2, 2, 3], [7]]

# ----------------------------------------------------------------------

# Key Takeaways:
# -------------------
# - Classic **Backtracking** problem with **repetition allowed**.
# - Important to stay at same index when including element (reuse allowed).
# - Prune branches early when total > target.
# - Builds strong foundation for advanced recursion problems like:
#   ➤ Combination Sum II (no repetition)
#   ➤ Subset Sum
#   ➤ Partition Equal Subset Sum
#   ➤ Coin Change Variants
"""

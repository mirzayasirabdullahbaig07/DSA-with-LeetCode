"""
Problem: Combination Sum II (LeetCode #40)

Definition:
Given a list of candidate numbers and a target, find all unique combinations where
the numbers sum to the target. Each number may be used only once.

You must return combinations without duplicates.

Example:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
 [1,1,6],
 [1,2,5],
 [1,7],
 [2,6]
]

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

====================================================================
INTUITION:
This is a *backtracking problem* where we explore all possible subsets of numbers 
that can sum to the target. However, because candidates may contain duplicates, 
we need to ensure that each unique combination appears only once.

We solve this using recursion + pruning + duplicate handling.

====================================================================
SOLUTION 1: BRUTE FORCE (Using Set to Remove Duplicates)

Idea:
- Generate all possible subsets using recursion.
- Whenever a combination’s sum == target → add it to a result set.
- Use a set of tuples to automatically handle duplicate combinations.
- Sort candidates first to ensure combinations are generated in sorted order.

Algorithm:
1. Sort the input list.
2. Use recursion (include/exclude) to explore all possible combinations.
3. If target == 0 → store the combination as a tuple in a set.
4. If target < 0 → stop exploring that path.
5. Return the list of all unique combinations from the set.

Code:
"""
class Solution:
    def backtrack(self, subset, index, target, result, candidates):
        if target == 0:
            result.add(tuple(subset.copy()))
            return
        elif target < 0 or index >= len(candidates):
            return

        # Include current element
        subset.append(candidates[index])
        self.backtrack(subset, index + 1, target - candidates[index], result, candidates)

        # Exclude current element (backtrack)
        subset.pop()
        self.backtrack(subset, index + 1, target, result, candidates)

    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = set()
        self.backtrack([], 0, target, result, candidates)
        return list(result)
"""
 Techniques Used:
- Backtracking
- Recursion
- Set for duplicate removal

 Time Complexity: O(2^n)
(We explore all subsets and rely on the set for deduplication.)
 Space Complexity: O(k)
(k = number of valid combinations + recursion depth)

====================================================================
SOLUTION 2: OPTIMAL (Smart Duplicate Avoidance)

Idea:
Instead of generating duplicates and removing them later,
we can *avoid generating them in the first place.*

After sorting:
- If candidates[i] == candidates[i-1] and i > index → skip it.
  (This ensures we only pick the first occurrence at a given recursion level.)
- If candidates[i] > target → break early (since array is sorted).

 Algorithm:
1. Sort the array.
2. Use for-loop in recursion to pick elements.
3. Skip duplicates using: if i > index and candidates[i] == candidates[i-1]: continue
4. Stop when candidates[i] > target.
5. When target == 0 → add subset to result.
"""
# Code:
class Solution:
    def backtrack(self, subset, index, target, result, candidates):
        if target == 0:
            result.append(subset.copy())
            return

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break

            subset.append(candidates[i])
            self.backtrack(subset, i + 1, target - candidates[i], result, candidates)
            subset.pop()

    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        self.backtrack([], 0, target, result, candidates)
        return result
"""
 Techniques Used:
- Backtracking
- Pruning (early stop when candidates[i] > target)
- Duplicate skipping via sorted array
- Recursion with depth-first search (DFS)

 Time Complexity: O(2^n)
(Same worst-case complexity, but much faster in practice due to pruning.)
 Space Complexity: O(k)
(k = number of valid combinations + recursion stack)

====================================================================
Summary:
Approach                | Handles Duplicates | Efficiency | Best Use
------------------------|-------------------|-------------|------------------------
Brute Force (Set)       | After generation  | Moderate    | Easy understanding
Optimal (Skip Duplicates)| During generation | High        | Efficient production code

====================================================================
Key Takeaways:
- Always sort the input before recursive generation.
- Handle duplicates smartly to prevent redundant work.
- This backtracking + pruning technique is reusable in:
  - Subsets II
  - Permutations II
  - Combination Sum Variants
====================================================================
"""

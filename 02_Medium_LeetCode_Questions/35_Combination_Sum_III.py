"""
Problem: Combination Sum III (LeetCode #216)

Definition:
Find all possible combinations of `k` numbers that sum up to `n` using only numbers 1 to 9.
Each number can be used at most once.

Return all unique combinations.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

Example 3:
Input: k = 4, n = 1
Output: []

Constraints:
2 <= k <= 9
1 <= n <= 60

====================================================================
INTUITION:
We need to select exactly `k` distinct numbers from 1–9 that sum to `n`.
This is a *classic backtracking problem*:
- We make a choice (pick a number)
- Move forward (next number)
- Backtrack (remove it)
- Avoid invalid paths early (if sum exceeds n or count exceeds k)

====================================================================
BRUTE FORCE APPROACH:
Try all subsets of numbers 1–9 and check which ones:
- Have exactly `k` numbers.
- Sum equals `n`.

Steps:
1. Generate all subsets (2^9 = 512 total).
2. Check each subset’s length and sum.
3. Keep valid ones only.

Code:
"""
class Solution:
    def combinationSum3(self, k, n):
        from itertools import combinations
        result = []
        for combo in combinations(range(1, 10), k):
            if sum(combo) == n:
                result.append(list(combo))
        return result
"""
 Algorithm Used:
- Generate combinations using itertools
- Filtering based on conditions

 Time Complexity: O(C(9, k)) × O(k)
(checking sum for each combination)
 Space Complexity: O(k)
(for storing current combinations)

Easy but not efficient — it checks all subsets even if they exceed the sum.

====================================================================
OPTIMAL APPROACH: Smart Backtracking + Pruning

Idea:
Be smart — instead of generating all combinations, prune impossible paths early.
Keep track of:
- Current sum
- Current combination
- Last number used (to maintain ascending order)

Algorithm:
1. Start from number 1 → 9.
2. Add the current number to the combination.
3. Recurse with updated sum and next starting number.
4. Stop (prune) when:
   - Sum > n → invalid path
   - len(combination) > k → invalid path
5. If sum == n and len == k → valid combination found.

Code:
"""
class Solution:
    def func(self, n, Sum, last, nums, k, ans):
        # Base case: Found a valid combination
        if Sum == n and len(nums) == k:
            ans.append(list(nums))
            return
        
        # Pruning invalid paths
        if Sum > n or len(nums) > k:
            return

        # Try numbers from current 'last' to 9
        for i in range(last, 10):
            nums.append(i)
            self.func(n, Sum + i, i + 1, nums, k, ans)
            nums.pop()  # backtrack

    def combinationSum3(self, k, n):
        ans = []
        self.func(n, 0, 1, [], k, ans)
        return ans
"""
====================================================================
CODE EXPLANATION:
- `Sum` tracks running total to avoid recomputing sum(nums).
- `last` ensures increasing order, preventing duplicates.
- Pruning avoids exploring impossible paths (Sum > n or len > k).
- Backtracking ensures exploration of all valid possibilities efficiently.

====================================================================
DRY RUN EXAMPLE:
Input: k=3, n=7

Start with Sum=0, nums=[]
→ Try 1 → Sum=1 → Try 2 → Sum=3 → Try 4 → Sum=7 Found [1,2,4]
→ Backtrack and explore others
→ All others pruned (Sum > 7 or len > 3)

Output: [[1,2,4]]

====================================================================
⏱TIME & SPACE COMPLEXITY:
- Time: O(C(9, k)) ≈ O(2^9) in worst case, but reduced drastically by pruning.
- Space: O(k)
  (due to recursion stack and combination storage)

====================================================================
TECHNIQUES USED:
- Backtracking
- Pruning (Early stopping)
- Recursion
- Depth-First Search (DFS)
- Combination generation

====================================================================
SUMMARY:

Approach                | Description                      | Time     | Space | Duplication Handling
------------------------|----------------------------------|----------|--------|-----------------------
Brute Force (Combinations) | Try all subsets and filter     | O(2^9)   | O(k)  | Handled by combinations()
Optimal (Backtracking)     | Smart pruning + DFS recursion | O(C(9,k))| O(k)  | Natural via order

====================================================================
KEY TAKEAWAYS:
✔ Use backtracking when exploring combinations or subsets.  
✔ Always apply pruning to cut unnecessary exploration.  
✔ Keep track of constraints (sum > n, len > k) to save time.  
✔ Ascending order avoids duplicates naturally.  
✔ Running sum optimization saves recomputation time.

====================================================================
"""

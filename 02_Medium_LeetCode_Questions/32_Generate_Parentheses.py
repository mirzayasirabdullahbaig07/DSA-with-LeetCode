"""
# Problem: Generate All Well-Formed Parentheses
# ==============================================

# Problem Statement:
# Given `n` pairs of parentheses, generate all possible combinations
# of well-formed (balanced) parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]

# Constraints:
# 1 <= n <= 8

# ----------------------------------------------------------------------

# Intuition:
# Think of building a valid sequence of parentheses step by step.
# You must ensure:
# - You never add more closing ')' than opening '('.
# - You can only add '(' if you still have some left to place.
#
# Example:
# For n = 3, you have 3 '(' and 3 ')' to place.
# You must always form a valid sequence like:
# (()()), not something like ())(.

# ----------------------------------------------------------------------

# Technique Used: Backtracking
# --------------------------------
# Backtracking is used to explore all possible sequences of '(' and ')'
# while **pruning invalid ones early**.
#
# At each step, you decide:
# 1. If you can add an '(' (only if open < n)
# 2. If you can add a ')' (only if close < open)
#
# This ensures that at no point do we have invalid parentheses order.

# ----------------------------------------------------------------------

# Problem Logic (Step-by-Step):
# 1. Start with an empty string.
# 2. Maintain two counters:
#    - `open_count`: number of '(' used so far.
#    - `close_count`: number of ')' used so far.
# 3. Base Case:
#    - When length of current string == 2 * n → all parentheses used.
#    - Add the string to results.
# 4. Recursive Choices:
#    - If open_count < n → we can still add '('.
#    - If close_count < open_count → we can still add ')'.
# 5. Backtrack:
#    - Explore both possibilities and return when complete.

# ----------------------------------------------------------------------

# Python Code Implementation:
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []  # List to store all valid parentheses combinations

        # Helper function for backtracking
        def backtrack(current: str, open_count: int, close_count: int):
            # Base case: if the current string is complete (length == 2 * n)
            if len(current) == 2 * n:
                result.append(current)
                return

            # Choice 1: Add '(' if we still have some left to use
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Choice 2: Add ')' if we have more '(' used than ')'
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        # Start recursion with empty string and zero counts
        backtrack("", 0, 0)
        return result

# ----------------------------------------------------------------------
"""
# Code Explanation:
# --------------------
# - The function `backtrack` builds valid strings recursively.
# - It adds '(' or ')' only when allowed by the balance condition.
# - It ensures that we never exceed the available number of '(' or ')'.
# - Once we reach length == 2*n, we store that combination.
# - The recursion automatically explores all valid possibilities.

# ----------------------------------------------------------------------

# Example Dry Run:
# --------------------
# Input: n = 2
# Expected Output: ["(())", "()()"]

# Step 1: start with "" (open=0, close=0)
# → add '(' → "(" (open=1, close=0)
# → add '(' → "((" (open=2, close=0)
# → add ')' → "(()" (open=2, close=1)
# → add ')' → "(())"  valid
#
# Backtrack:
# From "(" → try adding ')'
# → "()" (open=1, close=1)
# → add '(' → "()(" (open=2, close=1)
# → add ')' → "()()"  valid
#
# Final Output: ["(())", "()()"]

# ----------------------------------------------------------------------

# Time Complexity:
# --------------------
# O(4^n / √n)
# - This is the **nth Catalan number**, which represents the number
#   of valid combinations of parentheses.
# - At each step, we explore two choices (open or close), but pruning
#   prevents invalid paths.

# Space Complexity:
# ---------------------
# O(n)
# - Maximum recursion depth is `2n` (length of each combination).
# - The auxiliary space for recursion is proportional to n.

# ----------------------------------------------------------------------

# Real-world Analogy:
# -----------------------
# Imagine stacking and unstacking boxes:
# - "(" represents stacking a box.
# - ")" represents unstacking a box.
# You can’t unstack unless there’s something to unstack.
# A valid parentheses sequence is like a proper sequence of stacking
# and unstacking boxes — balanced and ordered.

# ----------------------------------------------------------------------

# Example Run:
solution = Solution()
print("All valid parentheses combinations for n=3:")
print(solution.generateParenthesis(3))

# Output:
# All valid parentheses combinations for n=3:
# ['((()))', '(()())', '(())()', '()(())', '()()()']

# ----------------------------------------------------------------------

# Key Takeaways:
# -------------------
# - Uses **Backtracking** to generate valid combinations efficiently.
# - Pruning avoids invalid states early → improves performance.
# - Number of valid parentheses combinations = Catalan number Cn.
# - Very common **interview question** for recursion and backtracking mastery.
# - Foundation for solving similar pattern problems like:
#   ➤ Balanced Strings
#   ➤ Binary Tree Generation
#   ➤ N-Queens, Sudoku Solver, etc.
"""

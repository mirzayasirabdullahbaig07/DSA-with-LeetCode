"""
# Problem: Generate All Subsets (Power Set) using Bit Manipulation
# ================================================================

# Problem Statement:
# Given an integer array `nums` of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[], [0]]

# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All numbers in nums are unique.

# ----------------------------------------------------------------------

# Technique Used: Bit Manipulation (Bitmasking)
# ------------------------------------------------
# Every subset can be represented as a **binary number (bitmask)** of length `n` (number of elements).
#
# Example: nums = [a, b, c]
# We can represent subsets as binary digits:
# 000 → []           (none included)
# 001 → [c]          (include only c)
# 010 → [b]          (include only b)
# 011 → [b, c]       (include b and c)
# 100 → [a]          (include only a)
# 101 → [a, c]
# 110 → [a, b]
# 111 → [a, b, c]
#
# So, if we loop from `0` to `2^n - 1`, each number’s binary form tells us which elements to include.
#
# - Bit 1 → include element
# - Bit 0 → exclude element

# ----------------------------------------------------------------------

# Problem Logic (Step-by-Step):
# 1 Calculate total subsets → 2^n = (1 << n)
# 2 For each number (mask) from 0 to (2^n - 1):
#     - Create an empty subset list.
# 3 For each bit position `i` in the mask:
#     - Check if the i-th bit is set using `(mask & (1 << i)) != 0`
#     - If True → include nums[i] in the current subset.
# 4 Append the subset to the result list.
# 5 Return the final list of all subsets.

# ----------------------------------------------------------------------

# 🧮 Python Code Implementation:
"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        total_subset = 1 << n   # 2^n total subsets
        result = []             # List to store all subsets
        
        # Loop through each bitmask from 0 to 2^n - 1
        for mask in range(total_subset):
            subset = []
            for i in range(n):
                # Check if the i-th bit in mask is set
                if mask & (1 << i):
                    subset.append(nums[i])
            result.append(subset)
        
        return result

# ----------------------------------------------------------------------
""""
# Code Explanation:
# - The expression `1 << n` shifts `1` to the left by `n` bits → 2^n.
# - Each `mask` is a unique combination of bits representing one subset.
# - `(mask & (1 << i))` checks if bit `i` is set → include nums[i].
# - This approach avoids recursion and is very efficient.

# ----------------------------------------------------------------------

# Example Dry Run:
# nums = [1, 2, 3], n = 3 → total subsets = 1 << 3 = 8
# masks → binary → subset
# 0 → 000 → []
# 1 → 001 → [1]
# 2 → 010 → [2]
# 3 → 011 → [1,2]
# 4 → 100 → [3]
# 5 → 101 → [1,3]
# 6 → 110 → [2,3]
# 7 → 111 → [1,2,3]

# Output → [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

# ----------------------------------------------------------------------

# Time Complexity:
# O(n * 2^n)
# - There are 2^n possible subsets.
# - For each subset, we check n bits to decide which elements to include.

# Space Complexity:
# O(1) auxiliary space (ignoring the output list)
# - We use constant extra space other than the result.

# ----------------------------------------------------------------------

# Real-world Analogy:
# Imagine `nums` = [shirt, jeans, shoes]
# Each day you decide whether to wear each item (yes or no).
# The combination of choices gives you all possible outfits — the power set!

# ----------------------------------------------------------------------

# Example Run:
solution = Solution()
nums = [1, 2, 3]
print("All Subsets (Using Bit Manipulation):")
print(solution.subsets(nums))

# Output:
# All Subsets (Using Bit Manipulation):
# [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

# ----------------------------------------------------------------------

# Key Takeaways:
# - This method is **non-recursive** and **efficient** for small `n` (<= 20).
# - It’s a great demonstration of how **binary representation** can model combinatorial problems.
# - Bitmasking is a powerful trick used in dynamic programming, subset problems, and combinatorial optimization.
"""

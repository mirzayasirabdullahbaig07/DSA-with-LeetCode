"""
LeetCode 2035: Partition Array Into Two Arrays to Minimize Sum Difference
-------------------------------------------------------------------------

Problem Summary:
You are given an array `nums` of length 2 * n.
You must split the array into two subarrays of length n such that
the absolute difference between their sums is minimized.

Key Insight:
- Since each subarray must have exactly n elements, this is NOT a simple
  subset sum problem.
- The constraint n ≤ 15 makes brute force over all subsets of size n
  infeasible (C(30,15) is too large).
- However, we can use a **Meet-in-the-Middle** approach to reduce complexity.

High-Level Strategy (Meet-in-the-Middle):
1. Split the array into two halves:
   - left = first n elements
   - right = last n elements
2. Enumerate all subset sums of each half.
3. Group subset sums by how many elements are chosen.
4. For each valid combination (k from left, n-k from right),
   find the pair of sums closest to half of the total sum.

Why Meet-in-the-Middle Works:
- Each half has at most 15 elements.
- Enumerating all subsets per half costs O(2^15), which is feasible.
- Combining results using binary search keeps the solution efficient.

Detailed Steps:

1. Preprocessing:
   - Let total_sum be the sum of all elements in nums.
   - Split nums into two arrays: left and right.

2. Subset Sum Generation:
   - For each half, generate all possible subset sums.
   - Store sums in a list of lists:
       res[k] contains all subset sums using exactly k elements.
   - This allows us to enforce the constraint of selecting exactly n elements.

3. Sorting:
   - Sort the subset sums of the right half for each possible subset size.
   - This enables efficient binary search.

4. Optimization via Binary Search:
   - For each subset sum s1 from left_sums[k]:
       - We need a subset sum s2 from right_sums[n-k]
       - The goal is to minimize:
             | total_sum - 2 * (s1 + s2) |
       - This is equivalent to making (s1 + s2) as close as possible
         to total_sum / 2.
   - Use binary search to find the closest candidate(s) in right_sums.

5. Update Answer:
   - Check both the found index and its previous index
     (binary search neighbors).
   - Keep track of the minimum absolute difference.

Final Result:
- The minimum absolute difference between the sums of the two partitions
  is returned.

Time Complexity:
- O(2^(n) * n + 2^(n) * log(2^(n)))
- With n ≤ 15, this is efficient.

Space Complexity:
- O(2^(n)) for storing subset sums.

Why This Solution Is Optimal:
- Fully respects the equal-size constraint.
- Efficiently balances brute force and optimization.
- Uses advanced techniques (Meet-in-the-Middle + Binary Search),
  which are highly valued in interviews.

Key Techniques Used:
- Bitmasking
- Meet-in-the-Middle
- Binary Search
- Subset enumeration
"""
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        from typing import List
import bisect

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        left = nums[:n]
        right = nums[n:]
        total_sum = sum(nums)

        # Generate subset sums grouped by count
        def subset_sums(arr):
            res = [[] for _ in range(len(arr) + 1)]
            m = len(arr)
            for mask in range(1 << m):
                s = 0
                cnt = 0
                for i in range(m):
                    if mask & (1 << i):
                        s += arr[i]
                        cnt += 1
                res[cnt].append(s)
            return res

        left_sums = subset_sums(left)
        right_sums = subset_sums(right)

        # Sort right sums for binary search
        for i in range(n + 1):
            right_sums[i].sort()

        ans = float('inf')

        # Try all k elements from left, n-k from right
        for k in range(n + 1):
            for s1 in left_sums[k]:
                need = (total_sum / 2) - s1
                arr = right_sums[n - k]

                idx = bisect.bisect_left(arr, need)

                if idx < len(arr):
                    s2 = arr[idx]
                    ans = min(ans, abs(total_sum - 2 * (s1 + s2)))

                if idx > 0:
                    s2 = arr[idx - 1]
                    ans = min(ans, abs(total_sum - 2 * (s1 + s2)))

        return ans

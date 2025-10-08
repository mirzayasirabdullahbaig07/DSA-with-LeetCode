"""
Problem: 410. Split Array Largest Sum
------------------------------------
Given an integer array nums and an integer k,
split nums into k non-empty subarrays such that 
the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

------------------------------------
Example 1:
Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

Example 2:
Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation:
Split into [1,2,3] and [4,5], 
largest sum = max(6, 9) = 9 (minimum possible).

------------------------------------
Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 10^6
1 <= k <= min(50, nums.length)
"""

from typing import List

# -------------------------------------------------------------------
# ✅ Optimal Solution using Binary Search + Greedy Check
# -------------------------------------------------------------------
class Solution:
    """
    Intuition:
    ----------
    We want to divide the array into k parts so that 
    the maximum subarray sum is minimized.

    - Imagine each subarray sum cannot exceed some value `max_sum`.
    - Then we can greedily check if we can split the array into <= k subarrays.
    - If we can, try a smaller `max_sum`.
    - If not, increase it.
    
    → This forms a binary search problem on the answer.

    The range of `max_sum` is between:
    - low  = max(nums)   (minimum possible largest sum)
    - high = sum(nums)   (maximum possible largest sum)
    """

    # ---------------------------------------------------------------
    # Helper Function: canSplit
    # ---------------------------------------------------------------
    def canSplit(self, nums: List[int], k: int, max_sum: int) -> bool:
        """
        Checks if it's possible to split the array into ≤ k subarrays
        such that no subarray has a sum greater than max_sum.

        Parameters:
        -----------
        nums : List[int]
            The input array of integers.
        k : int
            The number of allowed subarrays.
        max_sum : int
            The maximum allowed sum for any subarray.

        Returns:
        --------
        bool : True if possible to split, else False.
        """

        subarrays = 1   # at least one subarray initially
        curr_sum = 0    # current running sum

        for num in nums:
            # If an element itself is greater than allowed max_sum → impossible
            if num > max_sum:
                return False

            # If adding current element exceeds max_sum → start new subarray
            if curr_sum + num > max_sum:
                subarrays += 1
                curr_sum = num  # start new subarray
                if subarrays > k:
                    return False  # too many subarrays
            else:
                curr_sum += num  # continue adding in current subarray

        return True  # possible to split into ≤ k subarrays


    # ---------------------------------------------------------------
    # Main Function: splitArray
    # ---------------------------------------------------------------
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        Uses Binary Search on the answer space to find 
        the minimum possible largest subarray sum.

        Steps:
        -------
        1. Define the range of possible largest sums:
            low  = max(nums)
            high = sum(nums)
        2. Perform binary search on this range.
        3. Use canSplit() to check feasibility.
        4. Narrow down the range accordingly.

        Returns:
        --------
        int : The minimized largest subarray sum.
        """

        low, high = max(nums), sum(nums)
        result = high  # start with max possible sum

        while low <= high:
            mid = (low + high) // 2  # mid is our trial max_sum

            # Check if we can split with this max_sum
            if self.canSplit(nums, k, mid):
                result = mid          # valid → store and try smaller
                high = mid - 1
            else:
                low = mid + 1         # invalid → increase max_sum

        return result


# -------------------------------------------------------------------
# 🧩 Dry Run Example
# -------------------------------------------------------------------
"""
nums = [7,2,5,10,8], k = 2
--------------------------------
Range:
low  = max(nums) = 10
high = sum(nums) = 32

Binary Search Steps:
---------------------
mid = (10 + 32)//2 = 21
canSplit(nums, 2, 21):
  [7,2,5] sum=14 → OK
  add 10 → sum=24 > 21 → start new subarray
  subarrays = 2 → add 8 → sum=18 → OK → ✅ True

→ 21 works → try smaller
high = 20

mid = (10 + 20)//2 = 15
canSplit(nums, 2, 15):
  [7,2,5] sum=14 → OK
  add 10 → sum=24 > 15 → new subarray
  subarrays = 2 → add 8 → sum=18 > 15 → new subarray → subarrays=3 ❌ False

→ Need larger → low = 16

mid = (16 + 20)//2 = 18
canSplit(nums, 2, 18):
  [7,2,5] sum=14 → OK
  add 10 → sum=24 > 18 → new subarray
  subarrays=2 → add 8 → sum=18 → OK ✅ True

→ result = 18, high = 17 → loop ends

✅ Final Answer: 18
"""

# -------------------------------------------------------------------
# ⏱️ Time and Space Complexity
# -------------------------------------------------------------------
"""
Time Complexity:
----------------
- canSplit() runs in O(n)
- Binary search runs on the range [max(nums), sum(nums)]
  → approximately log(sum(nums))
Overall: O(n * log(sum(nums)))

For n = 1000, nums[i] up to 10^6 → efficient enough.

Space Complexity:
-----------------
O(1) → uses only constant extra variables (no extra data structures)
"""

# -------------------------------------------------------------------
# 🔍 Example Usage (you can test locally)
# -------------------------------------------------------------------
if __name__ == "__main__":
    nums = [7, 2, 5, 10, 8]
    k = 2
    sol = Solution()
    print("Minimized Largest Sum:", sol.splitArray(nums, k))

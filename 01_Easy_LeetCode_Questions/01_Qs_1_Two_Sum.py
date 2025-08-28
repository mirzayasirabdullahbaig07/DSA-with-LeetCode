"""
Problem: Two Sum (LeetCode #1)

Given an array of integers nums and an integer target, return indices of 
the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 9

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Follow-up: Can you solve it in less than O(n^2)?
"""


# -------------------------------
# Solution 1: Brute Force (O(n^2))
# -------------------------------

class SolutionBruteForce:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):  # check every pair
                if nums[i] + nums[j] == target:
                    return [i, j]


"""
Dry Run (Brute Force):
nums = [2,7,11,15], target = 9

i=0, j=1 -> nums[0]+nums[1] = 2+7 = 9 -> Found! return [0,1]
"""

# Time Complexity: O(n^2)  (two loops for pairs)
# Space Complexity: O(1)   (no extra data structure used)


# ---------------------------------
# Solution 2: Optimized (Hash Map)
# ---------------------------------

class SolutionOptimized:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}  # store numbers we have seen {value: index}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:  # check if complement exists
                return [num_map[complement], i]
            num_map[num] = i  # store current number and its index


"""
Dry Run (Optimized):
nums = [2,7,11,15], target = 9

Step 1: i=0, num=2, complement=7 -> not in map -> store {2:0}
Step 2: i=1, num=7, complement=2 -> found in map -> return [0,1]

Output: [0,1]
"""

# Time Complexity: O(n)  (one pass through nums)
# Space Complexity: O(n) (dictionary stores seen numbers)


# -------------------------
# Example Usage (Testing)
# -------------------------
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print("Brute Force:", SolutionBruteForce().twoSum(nums, target))   # [0,1]
    print("Optimized:", SolutionOptimized().twoSum(nums, target))     # [0,1]

"""
 PROBLEM: Binary Subarrays With Sum
--------------------------------------
You are given a binary array `nums` (which contains only 0s and 1s)
and an integer `goal`. You need to find the number of non-empty contiguous
subarrays whose sum is equal to `goal`.

A subarray is a continuous segment of the array.

--------------------------------------
 Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4

Explanation:
The 4 valid subarrays with sum = 2 are:
1. [1,0,1]
2. [0,1,0,1]
3. [1,0,1,0]
4. [1,0,1]

--------------------------------------
 Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15

Explanation:
Every subarray made of zeros has a sum of 0.
There are 15 total subarrays in [0,0,0,0,0].

--------------------------------------
 Constraints:
1 <= nums.length <= 30,000
nums[i] is either 0 or 1
0 <= goal <= nums.length


======================================
 APPROACH 1: BRUTE FORCE (O(n²))
======================================

 Intuition:
For each starting index `i`, expand the subarray ending at every index `j`.
Keep a running sum and stop early if the sum exceeds the goal
(since adding more 1’s can only increase it).

 Steps:
1. Initialize count = 0
2. For every start index i:
   - Set total = 0
   - For every end index j >= i:
       - Add nums[j] to total
       - If total > goal → break (optimization)
       - If total == goal → increment count
3. Return count

 Code:
------------------------------------------------
"""
def numSubarraysWithSum(nums, goal):
    count = 0
    n = len(nums)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total > goal:
                break
            if total == goal:
                count += 1
    return count
"""
------------------------------------------------

 Why It Works:
The sum in a binary array is non-decreasing as we extend the window,
so we can break early when total > goal.

 Complexity:
Time: O(n²)
Space: O(1)

 Drawback:
Very slow for large inputs (n up to 30,000).



======================================
 APPROACH 2: OPTIMAL SLIDING WINDOW
       (AtMost Trick → O(n) Time)
======================================

 Core Idea:
In a binary array, we can efficiently count subarrays
whose sum is **at most X** using a sliding window.

To get the **exact goal**, use:
    count(sum == goal) = count(sum ≤ goal) − count(sum ≤ goal−1)

 Helper Logic:
Count subarrays where sum ≤ goal.
Use two pointers (left, right):
1. Add nums[right] to the window.
2. If window sum > goal, shrink it from the left.
3. The number of valid subarrays ending at `right`
   is (right - left + 1), since any start in [left, right] is valid.

 Code:
------------------------------------------------
"""
class Solution:
    def countSubArrayLessThanOrEqualToGoal(self, nums, goal):
        if goal < 0:
            return 0
        count = 0
        left = 0
        Sum = 0
        for right in range(len(nums)):
            Sum += nums[right]
            while Sum > goal:
                Sum -= nums[left]
                left += 1
            count += (right - left + 1)
        return count

    def numSubarraysWithSum(self, nums, goal):
        return (self.countSubArrayLessThanOrEqualToGoal(nums, goal)
                - self.countSubArrayLessThanOrEqualToGoal(nums, goal - 1))
"""
------------------------------------------------

 Why It Works:
For binary arrays, the sum changes predictably (increases by 1 at most),
allowing a simple sliding window.
We count all subarrays with sum ≤ goal,
then subtract those with sum ≤ goal−1,
giving exactly the subarrays with sum == goal.

 Complexity:
Time: O(n)
Space: O(1)

 Example Walkthrough:
nums = [1,0,1,0,1], goal = 2

1 count(sum ≤ 2):
   → 13 valid subarrays
2 count(sum ≤ 1):
   → 9 valid subarrays
Result = 13 - 9 = 4 

--------------------------------------
 Edge Cases:
- goal = 0 → only all-zero subarrays are valid
- goal > total sum → result = 0
- Empty array → result = 0


======================================
 APPROACH 3: PREFIX SUM + HASHMAP
======================================

 Intuition:
Let prefix[i] = sum of first i elements.
Then subarray(i, j) has sum = prefix[j] - prefix[i-1].
We can rearrange:
    prefix[i] - goal = previous prefix value we need.

So we count how many times (prefix_sum - goal) occurred before.

 Code:
------------------------------------------------
"""
def numSubarraysWithSum(nums, goal):
    from collections import defaultdict
    prefix_sum = 0
    count = 0
    freq = defaultdict(int)
    freq[0] = 1  # base case

    for num in nums:
        prefix_sum += num
        if (prefix_sum - goal) in freq:
            count += freq[prefix_sum - goal]
        freq[prefix_sum] += 1
    return count
"""
------------------------------------------------

 Example:
nums = [1,0,1,0,1], goal = 2

prefix sums = [1,1,2,2,3]
Valid subarrays correspond to prefix differences = goal.

 Complexity:
Time: O(n)
Space: O(n)

 Advantage:
Generalizes beyond binary arrays (works for any integers).



======================================
 FINAL TAKEAWAY
======================================
- Use Brute Force → to understand the problem deeply.
- Use Sliding Window (AtMost Trick) → for efficient O(n) solution.
- Use Prefix Sum + HashMap → for general cases (non-binary arrays).

 Remember Formula:
    count(sum == goal) = count(sum ≤ goal) − count(sum ≤ goal−1)

 Patterns You Learn:
- Sliding window technique
- Prefix sum with hashmap
- Binary array optimization

These patterns reappear in other advanced problems like:
- "Subarray Sum Equals K"
- "Longest Subarray with Sum ≤ K"
- "Count Nice Subarrays"
--------------------------------------
"""

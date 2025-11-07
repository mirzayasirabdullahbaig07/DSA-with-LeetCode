"""
 PROBLEM: Count Number of Nice Subarrays
------------------------------------------
Given an integer array `nums` and an integer `k`, we define a subarray
as "nice" if it contains exactly `k` odd numbers.

Your task: Return the total number of nice subarrays in `nums`.

------------------------------------------
 Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation:
The only subarrays with exactly 3 odd numbers are:
1. [1,1,2,1]
2. [1,2,1,1]

------------------------------------------
 Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation:
There are no odd numbers at all → no valid subarrays.

------------------------------------------
 Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
Explanation:
There are 16 subarrays that contain exactly 2 odd numbers.

------------------------------------------
 Constraints:
1 <= nums.length <= 50,000
1 <= nums[i] <= 10^5
1 <= k <= nums.length


===============================================================
 APPROACH 1: BRUTE FORCE (O(n²))
===============================================================

 Intuition:
For every possible subarray, count the number of odd numbers.
If the count equals `k`, increment the answer.

 Steps:
1. Initialize `count = 0`
2. For each start index `i`:
   - Initialize `odd_count = 0`
   - For each end index `j` (i → n−1):
       - If nums[j] is odd, increment `odd_count`
       - If `odd_count == k`, increment total count
       - If `odd_count > k`, break (since adding more odds won’t help)
3. Return total count

 Code:
------------------------------------------------------------
"""
def numberOfSubarrays(nums, k):
    count = 0
    n = len(nums)
    for i in range(n):
        odd_count = 0
        for j in range(i, n):
            if nums[j] % 2 == 1:
                odd_count += 1
            if odd_count == k:
                count += 1
            elif odd_count > k:
                break
    return count
"""
------------------------------------------------------------

 Why It Works:
The loop checks all subarrays and counts only those
with exactly k odd numbers.

 Complexity:
Time: O(n²)
Space: O(1)

 Limitation:
Very slow for large arrays (n = 50,000 → 2.5 billion checks).



===============================================================
 APPROACH 2: PREFIX SUM + HASHMAP (O(n) Time, O(n) Space)
===============================================================

 Core Idea:
Convert each number into 1 (if odd) or 0 (if even).
Now the problem becomes **“count the number of subarrays
whose sum = k”**, just like the "Subarray Sum Equals K" problem.

 Steps:
1. Convert nums into `odd = [num % 2 for num in nums]`
2. Keep track of running prefix sum (`prefix_sum`)
3. Use a dictionary `count_map` to store how many times
   each prefix_sum has occurred.
4. For each prefix_sum:
   - If `prefix_sum - k` exists in map → add its frequency to the result
   - Increment count of current prefix_sum in map

 Code:
------------------------------------------------------------
"""
from collections import defaultdict

def numberOfSubarrays(nums, k):
    prefix_sum = 0
    result = 0
    count_map = defaultdict(int)
    count_map[0] = 1  # base case

    for num in nums:
        prefix_sum += num % 2  # add 1 for odd, 0 for even
        if (prefix_sum - k) in count_map:
            result += count_map[prefix_sum - k]
        count_map[prefix_sum] += 1
    return result
"""
------------------------------------------------------------

 Example Walkthrough:
nums = [1,1,2,1,1], k = 3
odd version = [1,1,0,1,1]
prefix sums = [1,2,2,3,4]
Count of subarrays with sum = 3 → 2 

 Complexity:
Time: O(n)
Space: O(n)

 Advantage:
Works for any array (not just binary or even/odd pattern).



===============================================================
 APPROACH 3: OPTIMAL SLIDING WINDOW (AtMost → Exact)
===============================================================

 Key Formula:
exact(k) = atMost(k) − atMost(k−1)

That is, the number of subarrays with exactly k odds
equals the difference between:
- Number of subarrays with at most k odds
- Number of subarrays with at most k−1 odds

 Helper Function:
countSubArrayLessThanOrEqualToGoal(nums, goal)
→ counts subarrays with at most `goal` odd numbers.

 Sliding Window Logic:
1. Maintain a window [left..right] and variable `Sum` for count of odds.
2. Expand right → add `nums[right] % 2` to Sum.
3. While Sum > goal → shrink from left.
4. For each right, add `(right - left + 1)` valid subarrays.

 Code:
------------------------------------------------------------
"""
class Solution:
    def countSubArrayLessThanOrEqualToGoal(self, nums, goal):
        if goal < 0:
            return 0
        count = 0
        left = 0
        Sum = 0
        for right in range(len(nums)):
            Sum += nums[right] % 2
            while Sum > goal:
                Sum -= nums[left] % 2
                left += 1
            count += (right - left + 1)
        return count

    def numberOfSubarrays(self, nums, k):
        return (self.countSubArrayLessThanOrEqualToGoal(nums, k)
                - self.countSubArrayLessThanOrEqualToGoal(nums, k - 1))
"""
------------------------------------------------------------

 Example Walkthrough:
nums = [1,1,2,1,1], k = 3

1 count(atMost(3)) = 13
2 count(atMost(2)) = 11
 exact(3) = 13 - 11 = 2

→ Output = 2 

 Complexity:
Time: O(n)
Space: O(1)

 Advantages:
 Linear time  
 Constant space  
 Works perfectly for large input (n up to 50,000)


===============================================================
 FINAL TAKEAWAY
===============================================================

✔ Brute Force – builds intuition (O(n²))  
✔ Prefix Sum + Hashmap – works for any integers (O(n) / O(n))  
✔ Sliding Window (AtMost Trick) – best for this problem (O(n) / O(1))

 Formula:
    exact(k) = atMost(k) − atMost(k−1)

 Reusable Concept:
This exact pattern works for:
- Binary Subarrays with Sum
- Subarray Sum Equals K
- Count Number of Nice Subarrays

 Why It’s Elegant:
By turning the problem into “at most” computations,
we transform a complex exact-count problem into two clean
linear scans using the sliding window technique.
"""

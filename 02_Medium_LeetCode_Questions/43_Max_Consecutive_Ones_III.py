"""
==============================
LeetCode 1004 — Max Consecutive Ones III
==============================

 Problem Statement:
---------------------
Given a binary array 'nums' (containing only 0s and 1s) and an integer 'k',
you are allowed to flip at most 'k' zeros into ones.
Return the maximum number of consecutive 1's in the array after flipping.

 Example 1:
-------------
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: Flip the two 0’s in the middle → [1,1,1,0,0,1,1,1,1,1,1]
The longest consecutive 1’s subarray length is 6.

 Example 2:
-------------
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: By flipping 3 zeros, we can form the longest streak of 10 ones.

 Intuition:
-------------
We need to find the longest subarray (continuous window) that contains at most 'k' zeros.
Every time the number of zeros exceeds 'k', we shrink the window from the left.

This is a classic **Sliding Window problem**.

---------------------------------------
1 BRUTE FORCE APPROACH (O(n²) Time)
---------------------------------------
Idea:
- Try all possible windows.
- Count how many zeros are in each window.
- If zeros <= k, update the max length.
- Otherwise, break and move to the next window.

 Code:
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        n = len(nums)
        for i in range(n):
            zeros = 0
            for j in range(i, n):
                if nums[j] == 0:
                    zeros += 1
                if zeros <= k:
                    length = j - i + 1
                    max_length = max(max_length, length)
                else:
                    break
        return max_length

 Time Complexity: O(n²)
 Space Complexity: O(1)
 Not suitable for large inputs.

--------------------------------------------
2 BETTER APPROACH — SLIDING WINDOW (O(n))
--------------------------------------------
Idea:
- Maintain two pointers (left and right) that define a window.
- Expand the right pointer, count zeros.
- If zeros > k, move the left pointer until zeros ≤ k again.
- Track the maximum window size during the process.

 Code:
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        max_length = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        
        return max_length

 Time Complexity: O(n)
 Space Complexity: O(1)
 Each element is processed at most twice (once by right pointer, once by left).

-----------------------------------------
3 WHY SLIDING WINDOW IS OPTIMAL
-----------------------------------------
 Each index is visited only twice → O(n) efficiency.
 Maintains a window that always satisfies the constraint (zeros ≤ k).
 Works for any value of k (even k = 0).

-----------------------------------------
 Step-by-Step Example:
-----------------------------------------
nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2

→ Expand right pointer:
   - Add elements to window
   - Count zeros
   - When zeros > 2, move left pointer until zeros ≤ 2 again

→ Windows during iteration:
   [1,1,1] → zeros=0 → length=3
   [1,1,1,0] → zeros=1 → length=4
   [1,1,1,0,0] → zeros=2 → length=5
   [1,1,1,0,0,0] → zeros=3 → shrink left → length decreases
   ...
   Max window found = 6.

-----------------------------------------
 Time and Space Complexity:
-----------------------------------------
⏱ Time Complexity: O(n)
 Space Complexity: O(1)

-----------------------------------------
 When to Use:
-----------------------------------------
- When you need to find a longest/shortest subarray with some condition.
- Especially useful in problems involving “at most k changes” or “at most k distinct elements”.

-----------------------------------------
 Real-World Analogy:
-----------------------------------------
Imagine you have a row of light bulbs (1 = ON, 0 = OFF),
and you can repair at most ‘k’ faulty bulbs (0 → 1).
You want to find the longest continuous section of working bulbs after fixing.

-----------------------------------------
 Key Takeaways:
-----------------------------------------
 Always maintain a window that satisfies the constraint.
 Shrink only when condition breaks (zeros > k).
 Sliding window = efficient + elegant.

-----------------------------------------
Final Answer Example:
-----------------------------------------
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: The longest possible streak after flipping 2 zeros is 6.
"""

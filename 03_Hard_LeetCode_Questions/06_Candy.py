"""
 LeetCode #2149 — Rearrange Array Elements by Sign
============================================================

 Problem Statement:
------------------------------------------------------------
You are given a 0-indexed integer array `nums` of even length consisting of an equal number 
of positive and negative integers.

Your task is to rearrange the elements of `nums` so that:
1 Every consecutive pair of integers has opposite signs.
2 For all integers with the same sign, the order from the original array is preserved.
3 The rearranged array starts with a positive integer.

Return the modified array that satisfies all these conditions.


------------------------------------------------------------
 Example 1:
------------------------------------------------------------
Input:
    nums = [3, 1, -2, -5, 2, -4]

Output:
    [3, -2, 1, -5, 2, -4]

Explanation:
    Positive numbers: [3, 1, 2]
    Negative numbers: [-2, -5, -4]
    Alternate them starting with positive → [3, -2, 1, -5, 2, -4]


------------------------------------------------------------
 Example 2:
------------------------------------------------------------
Input:
    nums = [-1, 1]

Output:
    [1, -1]

Explanation:
    Positive = [1]
    Negative = [-1]
    Alternating starting with positive → [1, -1]


============================================================
 Objective:
------------------------------------------------------------
Rearrange the array such that:
     Elements alternate in sign (+, -, +, -, ...)
     The order among same-sign elements is maintained
     The first element is positive


============================================================
 Constraints:
------------------------------------------------------------
2 <= nums.length <= 2 * 10⁵  
nums.length is even  
Each |nums[i]| ≤ 10⁵  
nums contains equal number of positive and negative integers  


============================================================
 Approach 1: Brute Force Solution
============================================================

 Intuition:
-------------
The simplest way to solve this problem is by dividing the array into two parts:
- One for positive numbers  
- One for negative numbers  

Once separated, we can merge them back alternately into the array:
Positive → Negative → Positive → Negative …  

This ensures both alternate signs and preserves the relative order.


------------------------------------------------------------
 Code Implementation:
------------------------------------------------------------

"""
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        n = len(nums)

        # Step 1: Separate positive and negative numbers
        for i in range(n):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])

        # Step 2: Rearrange alternately
        for i in range(len(pos)):
            nums[2 * i] = pos[i]
            nums[2 * i + 1] = neg[i]

        return nums
"""

------------------------------------------------------------
 Dry Run:
------------------------------------------------------------
Input:
    nums = [3, 1, -2, -5, 2, -4]

Step 1 → Separate positives and negatives:
    pos = [3, 1, 2]
    neg = [-2, -5, -4]

Step 2 → Merge alternately:
    nums[0] = 3 (pos[0])
    nums[1] = -2 (neg[0])
    nums[2] = 1 (pos[1])
    nums[3] = -5 (neg[1])
    nums[4] = 2 (pos[2])
    nums[5] = -4 (neg[2])

Final Output:
    [3, -2, 1, -5, 2, -4]


------------------------------------------------------------
 Code Explanation:
------------------------------------------------------------
1 Create two lists — one for positive (pos) and one for negative (neg).  
2 Traverse the array and separate all numbers accordingly.  
3 Place them alternately back in the array (even index for positive, odd index for negative).  
4 Return the rearranged array.

------------------------------------------------------------
 Time Complexity:
O(N) for separation + O(N) for rearranging = O(2N) ≈ O(N)

 Space Complexity:
O(N) — additional space for the two temporary lists.


------------------------------------------------------------
 Advantages:
 Very easy to understand and implement  
 Maintains the original order perfectly  
 Disadvantages:
 Uses extra memory for two lists (not in-place)


============================================================
 Approach 2: Optimal Solution (Using Two Pointers)
============================================================

 Intuition:
-------------
Instead of maintaining two separate lists for positive and negative numbers, 
we can use a **new array (`ans`)** and place each number in the correct position on the go.  

We maintain:
- `posIndex` for positive numbers (even indices → 0, 2, 4, …)  
- `negIndex` for negative numbers (odd indices → 1, 3, 5, …)

As we iterate:
- If we find a positive → place it at `ans[posIndex]` and increment `posIndex` by 2.  
- If we find a negative → place it at `ans[negIndex]` and increment `negIndex` by 2.  

This guarantees alternation and order preservation.


------------------------------------------------------------
 Code Implementation:
------------------------------------------------------------
"""
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        posIndex, negIndex = 0, 1

        for i in range(n):
            if nums[i] < 0:
                ans[negIndex] = nums[i]
                negIndex += 2
            else:
                ans[posIndex] = nums[i]
                posIndex += 2

        return ans

"""
------------------------------------------------------------
 Dry Run:
------------------------------------------------------------
Input:
    nums = [3, 1, -2, -5, 2, -4]

Initial State:
    ans = [0, 0, 0, 0, 0, 0]
    posIndex = 0, negIndex = 1

Step-by-step:
    nums[0] = 3 → positive → ans[0] = 3 → posIndex = 2
    nums[1] = 1 → positive → ans[2] = 1 → posIndex = 4
    nums[2] = -2 → negative → ans[1] = -2 → negIndex = 3
    nums[3] = -5 → negative → ans[3] = -5 → negIndex = 5
    nums[4] = 2 → positive → ans[4] = 2 → posIndex = 6
    nums[5] = -4 → negative → ans[5] = -4 → negIndex = 7

Final Output:
    [3, -2, 1, -5, 2, -4]


------------------------------------------------------------
 Code Explanation:
------------------------------------------------------------
1 Initialize an empty result array `ans` with zeros.  
2 Keep track of positions for positives (even indices) and negatives (odd indices).  
3 Iterate through `nums` and place elements directly in the right positions.  
4 Return the `ans` array after filling it.


------------------------------------------------------------
 Time Complexity:
O(N) — only one traversal of the array.

 Space Complexity:
O(N) — for the new result array.


------------------------------------------------------------
 Advantages:
 Efficient single-pass approach  
 Easy to implement and understand  
 Maintains order and alternation perfectly  

 Disadvantages:
 Still requires O(N) extra space (not fully in-place)


============================================================
 Comparison Table
============================================================

| Approach              | Time Complexity | Space Complexity | Order Preserved | Description                            |
|-----------------------|-----------------|------------------|-----------------|----------------------------------------|
| Brute Force           | O(N)            | O(N)             |  Yes          | Separate lists + merge alternately     |
| Optimal (Two Pointers)| O(N)            | O(N)             |  Yes          | Direct placement with even/odd indices |


============================================================
 Final Summary
------------------------------------------------------------
Both solutions yield the same correct output, but differ in implementation style.

 Brute Force → Simple & beginner-friendly  
 Optimal → Cleaner and more efficient (used in interviews)  

 Key Takeaway:
Use two pointers when alternating placement of elements based on certain conditions 
(e.g., positive/negative, even/odd, etc.).  
It’s a powerful and common interview pattern.


============================================================
 Example Recap
------------------------------------------------------------

Example 1:
Input:
    nums = [3, 1, -2, -5, 2, -4]
Output:
    [3, -2, 1, -5, 2, -4]

Example 2:
Input:
    nums = [-1, 1]
Output:
    [1, -1]

Both approaches correctly satisfy:
 Starts with a positive  
 Alternating signs  
 Preserved original order of same-sign elements  

============================================================
 Conclusion:
------------------------------------------------------------
The "Rearrange Array Elements by Sign" problem is a perfect example to master 
array manipulation, pointer handling, and order preservation.

Start with the brute-force approach to understand the logic, then move to the 
optimal version for better performance and professional-level implementation.
"""

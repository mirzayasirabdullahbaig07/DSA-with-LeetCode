"""
=============================================
LeetCode 1423 — Maximum Points You Can Obtain from Cards
=============================================

 Problem Statement:
---------------------
You are given an integer array `cardPoints` where each element represents 
the number of points on a card. All cards are arranged in a line.

In one move, you can take a card from either the **beginning** or the **end** of the row.  
You must take exactly `k` cards.  
Your total score is the sum of the points of all cards you take.

Return the **maximum possible score** you can obtain.

---------------------------------------------
 Example 1:
---------------------------------------------
Input:  cardPoints = [1,2,3,4,5,6,1], k = 3  
Output: 12  
Explanation:
Take 1 card from the left and 2 cards from the right → 1 + 6 + 5 = 12.

---------------------------------------------
 Example 2:
---------------------------------------------
Input:  cardPoints = [2,2,2], k = 2  
Output: 4  
Explanation:
No matter which two cards you choose, total = 4.

---------------------------------------------
 Example 3:
---------------------------------------------
Input:  cardPoints = [9,7,7,9,7,7,9], k = 7  
Output: 55  
Explanation:
You have to take all the cards, so total = 9 + 7 + 7 + 9 + 7 + 7 + 9 = 55.

---------------------------------------------
 Constraints:
---------------------------------------------
1 <= cardPoints.length <= 10^5  
1 <= cardPoints[i] <= 10^4  
1 <= k <= cardPoints.length  

---------------------------------------------
 Intuition:
---------------------------------------------
If you are required to take **k** cards from either end, that means:
you are leaving **n - k** cards unpicked in the middle.

So instead of directly maximizing the picked sum,  
you can minimize the sum of the middle (unpicked) subarray of size (n - k).

Then:
    maximum points = total sum of all cards - minimum sum of (n - k) consecutive cards.

Alternatively, you can use a **two-pointer / sliding window** approach:
- Take all k cards from the left initially.
- Gradually move one card at a time from left to right side.
- Track the best (maximum) combination.

---------------------------------------------
 Step-by-Step Approach:
---------------------------------------------
1 Edge Case:
   If k == len(cardPoints):
       → You must take all cards → return sum(cardPoints)

2 Initialize:
   - left_sum = sum of first k cards
   - right_sum = 0
   - max_sum = left_sum
   - n = len(cardPoints)

3 Sliding Window Movement:
   - Starting from i = k-1 down to 0:
       a. Subtract the last left card from left_sum.
       b. Add one right card (from the end) into right_sum.
       c. Update max_sum = max(max_sum, left_sum + right_sum)

   This effectively explores every possible split:
   Take x cards from left and (k - x) cards from right.

4 Return max_sum.

---------------------------------------------
 Dry Run Example:
---------------------------------------------
Input: cardPoints = [1,2,3,4,5,6,1], k = 3

Step 1: left_sum = 1+2+3 = 6, right_sum = 0 → max_sum = 6  
Step 2: Move one card from left to right:
        left_sum = 6 - 3 = 3, right_sum = 1 → total = 4 → max = 6  
Step 3: Move another card:
        left_sum = 3 - 2 = 1, right_sum = 1 + 6 = 7 → total = 8 → max = 8  
Step 4: Move last card:
        left_sum = 1 - 1 = 0, right_sum = 7 + 5 = 12 → total = 12 → max = 12  

 Final Answer = 12

---------------------------------------------
 Code Implementation:
---------------------------------------------
"""
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Edge case: if k == total number of cards, take them all
        if k == len(cardPoints):
            return sum(cardPoints)
        
        n = len(cardPoints)
        left_sum = sum(cardPoints[:k])  # take first k from left
        right_sum = 0
        max_sum = left_sum
        right_index = n - 1

        # Gradually move cards from left to right
        for i in range(k - 1, -1, -1):
            left_sum -= cardPoints[i]           # remove one from left
            right_sum += cardPoints[right_index] # add one from right
            right_index -= 1
            max_sum = max(max_sum, left_sum + right_sum)
        
        return max_sum
"""
---------------------------------------------
 Time and Space Complexity:
---------------------------------------------
 Time Complexity: O(k)
   - Initial left_sum: O(k)
   - Sliding loop: O(k)
   - Total ≈ O(k)

 Space Complexity: O(1)
   - Only a few variables used.

---------------------------------------------
 Alternate View (Minimum Window Approach):
---------------------------------------------
Let total = sum(cardPoints)
Let window_size = n - k

Find the minimum sum subarray of length (n - k).
Then:
    max_points = total - min_subarray_sum

This works because leaving the smallest unpicked portion 
gives you the maximum picked total.

---------------------------------------------
 Real-Life Analogy:
---------------------------------------------
Imagine you’re playing a card game where you can draw cards
from either end of the table — you want the **highest total score** 
after exactly k draws.  
This method efficiently finds that by comparing all possible
“left-right” combinations in linear time.

---------------------------------------------
 Edge Cases to Test:
---------------------------------------------
 k = 0 → Output = 0 (no cards taken)
 k = len(cardPoints) → Output = sum(cardPoints)
 Array with all equal elements → Output = k * cardPoints[0]
 Large input → Must run efficiently in O(k) time.

---------------------------------------------
 Key Takeaways:
---------------------------------------------
✔ Convert “pick from ends” problems into “leave middle subarray” form.
✔ Sliding window is powerful for such fixed-size subarray challenges.
✔ Understand both intuitive (left-right) and complementary (min window) approaches.

 Pattern to Remember:
   → Longest or maximum sum with limited changes → use sliding window.
   → Fixed number of picks/removals from both ends → simulate left/right splits.

---------------------------------------------
 Final Output Example:
---------------------------------------------
Input: cardPoints = [1,2,3,4,5,6,1], k = 3  
Output: 12  
Explanation: Best strategy is to pick last two and first one → 12.
"""

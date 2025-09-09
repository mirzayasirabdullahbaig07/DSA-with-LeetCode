"""
LEETCODE PROBLEM: 121. Best Time to Buy and Sell Stock
------------------------------------------------------

QUESTION STATEMENT:
-------------------
You are given an array prices where prices[i] is the price of a given stock on the i-th day.

You want to maximize your profit by choosing a single day to buy one stock 
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.


EXAMPLES:
---------
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation:
- Buy on day 2 (price = 1)
- Sell on day 5 (price = 6)
- Profit = 6 - 1 = 5

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation:
- Prices keep decreasing → no profit possible
- Hence return 0


CONSTRAINTS:
------------
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4


APPROACH / TECHNIQUE:
---------------------
We use the "Single Pass with Tracking Minimum Price" technique:
1. Keep track of the lowest price seen so far (`min_price`).
2. For each day's price:
   - Update `min_price` if the current price is smaller.
   - Otherwise, calculate the profit if we sold today: price - min_price.
   - Update `max_profit` if this profit is larger than current max.

This way, we ensure:
- We always "buy before sell" (because `min_price` is always from a past day).
- We find the maximum possible profit in O(n) time.


TIME COMPLEXITY:
----------------
- Single pass through prices → O(n)

SPACE COMPLEXITY:
-----------------
- Only two variables (`min_price` and `max_profit`) → O(1)


DRY RUN:
--------
prices = [7,1,5,3,6,4]
min_price = inf, max_profit = 0

Day 1: price=7 → min_price=7, max_profit=0
Day 2: price=1 → min_price=1, max_profit=0
Day 3: price=5 → profit=5-1=4 → max_profit=4
Day 4: price=3 → profit=3-1=2 → max_profit=4
Day 5: price=6 → profit=6-1=5 → max_profit=5
Day 6: price=4 → profit=4-1=3 → max_profit=5

Final Answer = 5
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # lowest price seen so far
        max_profit = 0           # best profit so far

        for price in prices:
            # Update min_price if current price is smaller
            if price < min_price:
                min_price = price
            # Otherwise check if selling now gives better profit
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

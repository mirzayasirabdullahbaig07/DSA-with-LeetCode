"""
LeetCode 1482. Minimum Number of Days to Make m Bouquets

Problem:
---------
You are given:
- bloomDay[]: an array where bloomDay[i] = day when ith flower blooms.
- m: number of bouquets needed.
- k: number of adjacent flowers required per bouquet.

You want to make m bouquets, each with k adjacent flowers. 
A flower can only be used once, after it blooms.

Return:
-------
The minimum number of days required to make m bouquets.
If impossible, return -1.

------------------------------------------------------------
Examples:
------------------------------------------------------------
Example 1:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: 
After day 3 → [x, _, x, _, x]
We can pick 3 flowers → 3 bouquets.

Example 2:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: 
We need 6 flowers total (3 bouquets × 2 flowers each), 
but only 5 flowers exist → impossible.

Example 3:
Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: 
Day 7 → only 1 bouquet possible.
Day 12 → 2 bouquets possible → answer is 12.

------------------------------------------------------------
Constraints:
------------------------------------------------------------
1 <= n = len(bloomDay) <= 10^5
1 <= bloomDay[i] <= 10^9
1 <= m <= 10^6
1 <= k <= n
------------------------------------------------------------
Brute Force Solution (Try Every Day)
------------------------------------------------------------
Intuition:
----------
1. Try every day from min(bloomDay) to max(bloomDay).
2. For each day, check if we can make at least m bouquets.
3. Return the first day that works.

Helper Function:
- canMakeBouquet(day) → counts how many bouquets possible by that day.

Time Complexity: O((max-min) * n)
- Too slow when bloomDay values are large (up to 10^9).
Space Complexity: O(1)
------------------------------------------------------------
Code Implementation (Brute Force):
------------------------------------------------------------
"""

from typing import List

class Solution:
    # Helper: Check if we can make m bouquets by a given day
    def canMakeBouquet(self, bloomDay: List[int], m: int, k: int, day: int) -> bool:
        bouquets = 0
        flowers = 0
        for bloom in bloomDay:
            if bloom <= day:              # flower bloomed
                flowers += 1
                if flowers == k:          # collected k adjacent flowers
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0               # reset if flower not bloomed
        return bouquets >= m

    # Brute force approach
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1   # Not enough flowers at all
        
        min_day, max_day = min(bloomDay), max(bloomDay)

        for day in range(min_day, max_day + 1):
            if self.canMakeBouquet(bloomDay, m, k, day):
                return day
        return -1

"""
------------------------------------------------------------
Dry Run (Brute Force):
------------------------------------------------------------
Input: bloomDay = [1,10,3,10,2], m=3, k=1

min_day = 1, max_day = 10

Day=1 → [x,_,_,_,_] → 1 bouquet
Day=2 → [x,_,_,_,x] → 2 bouquets
Day=3 → [x,_,x,_,x] → 3 bouquets → Answer=3

Output: 3
------------------------------------------------------------
Conclusion:
- Easy to understand
- Not efficient for large input
------------------------------------------------------------
Optimal Solution (Binary Search)
------------------------------------------------------------
Intuition:
----------
- Minimum day = min(bloomDay), maximum day = max(bloomDay).
- If we can make m bouquets on day X, then any day > X also works.
- This is a monotonic condition → Perfect for binary search.

Algorithm:
----------
1. Set search space [low, high] = [min(bloomDay), max(bloomDay)].
2. While low <= high:
    mid = (low + high)//2
    - If canMakeBouquet(mid) → save answer, try smaller (high=mid-1).
    - Else → need more time, try larger (low=mid+1).
3. Return the smallest valid day.

Time Complexity: O(n * log(max-min))
- Each check scans bloomDay.
- Binary search reduces range exponentially.
Space Complexity: O(1)

------------------------------------------------------------
Code Implementation (Binary Search):
------------------------------------------------------------
"""

class Solution:
    def canMakeBouquet(self, bloomDay: List[int], m: int, k: int, day: int) -> bool:
        total = 0
        count = 0
        for bloom in bloomDay:
            if bloom <= day:
                count += 1
                if count == k:
                    total += 1
                    count = 0
            else:
                count = 0
        return total >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        low, high = min(bloomDay), max(bloomDay)
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if self.canMakeBouquet(bloomDay, m, k, mid):
                ans = mid           # possible → store and try smaller
                high = mid - 1
            else:
                low = mid + 1       # not possible → try larger
        return ans

"""
------------------------------------------------------------
Dry Run (Binary Search):
------------------------------------------------------------
Input: bloomDay = [7,7,7,7,12,7,7], m=2, k=3

low=7, high=12
mid=9 → Day 9: only 1 bouquet → Not enough → low=10
mid=11 → Day 11: only 1 bouquet → Not enough → low=12
mid=12 → Day 12: 2 bouquets → Works → ans=12, high=11

Loop ends → answer=12
------------------------------------------------------------
Conclusion:
- Efficient and works for large inputs
- Classic binary search on answer problem
- Always check monotonicity before applying binary search
------------------------------------------------------------
"""

"""
LeetCode 875. Koko Eating Bananas

Problem:
---------
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. 
- Each hour, she chooses some pile and eats k bananas from it.
- If the pile has less than k bananas, she eats all of them and stops for that hour.

Goal:
-----
Return the minimum integer k such that Koko can eat all the bananas within h hours.

Example 1:
----------
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
----------
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
----------
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:
------------
1 <= piles.length <= 10^4
piles.length <= h <= 10^9
1 <= piles[i] <= 10^9

This is a **binary search variation problem** often asked in interviews.
------------------------------------------------------------
Brute Force Solution (Try Every Speed)
------------------------------------------------------------
Intuition:
----------
1. Try every possible speed from 1 to the maximum pile size.
2. For each speed, calculate total hours required to eat all bananas.
3. Return the first speed where total hours <= h.

Time Complexity: O(n * max(piles))
Space Complexity: O(1)
------------------------------------------------------------
Code Implementation (Brute Force):
------------------------------------------------------------
"""

import math
from typing import List

class Solution:
    # Function to calculate total hours for given speed
    def totalHours(self, piles, hourly_rate):
        total = 0
        for pile in piles:
            total += math.ceil(pile / hourly_rate)  # hours for each pile
        return total

    # Brute force approach
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum_banana = max(piles)             # Maximum possible speed
        for k in range(1, maximum_banana + 1):  # Try every speed
            if self.totalHours(piles, k) <= h: # Can finish within h hours
                return k

"""
------------------------------------------------------------
Dry Run (Brute Force):
------------------------------------------------------------
Input: piles = [3,6,7,11], h = 8

Try k=1: total hours = 3+6+7+11 = 27 (too high)
Try k=2: total hours = 2+3+4+6 = 15 (too high)
Try k=3: total hours = 1+2+3+4 = 10 (too high)
Try k=4: total hours = 1+2+2+3 = 8 (just right, return 4)

Output: 4
------------------------------------------------------------
Conclusion:
- Simple to understand
- Works for small inputs
- Inefficient for large piles or high h
"""

"""
------------------------------------------------------------
Optimal Solution (Binary Search)
------------------------------------------------------------
Intuition:
----------
- Minimum speed is 1, maximum speed is max(piles)
- totalHours(piles, k) is monotonic: as k increases, hours decrease
- Use binary search on speed to find minimum valid k

Algorithm:
----------
1. Initialize low = 1, high = max(piles)
2. While low <= high:
    a. mid = (low + high) // 2
    b. Calculate total hours for speed = mid
    c. If total hours <= h → store mid as answer, try smaller speed (high = mid-1)
    d. Else → need faster speed (low = mid+1)
3. Return minimum valid speed found
------------------------------------------------------------
Code Implementation (Binary Search):
------------------------------------------------------------
"""

class Solution:
    def totalHours(self, piles, hourly_rate):
        total = 0
        for pile in piles:
            total += math.ceil(pile / hourly_rate)  # hours for each pile
        return total

    # Binary search approach
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            total_hours = self.totalHours(piles, mid)
            
            if total_hours <= h:
                ans = mid           # mid works, try smaller
                high = mid - 1
            else:
                low = mid + 1       # mid too slow, try larger
        return ans

"""
------------------------------------------------------------
Dry Run (Binary Search):
------------------------------------------------------------
Input: piles = [3,6,7,11], h = 8

low=1, high=11
mid=6 → total_hours = 1+1+2+2 = 6 ≤ 8 → ans=6, try smaller → high=5
mid=3 → total_hours = 1+2+3+4 = 10 > 8 → low=4
mid=4 → total_hours = 1+2+2+3 = 8 ≤ 8 → ans=4, try smaller → high=3

Loop ends → answer = 4
------------------------------------------------------------
Time and Space Complexity:
- Time Complexity: O(n * log(max(piles))) → Binary search * checking piles
- Space Complexity: O(1) → Only variables used
------------------------------------------------------------
Conclusion:
- Efficient for large piles and high h
- Classic binary search optimization problem
- Start with brute force to understand, then use binary search for best performance
"""

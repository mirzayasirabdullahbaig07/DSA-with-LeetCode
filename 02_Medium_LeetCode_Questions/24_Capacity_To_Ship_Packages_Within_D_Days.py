"""
LeetCode 1011: Capacity To Ship Packages Within D Days
------------------------------------------------------

Problem:
--------
You are given an array weights where each element represents the weight of a package. 
You have D days to ship all the packages. You must ship the packages in order (no reordering).

Each day, you can ship as many packages as you want, as long as 
their total weight does not exceed the ship’s capacity.

Task:
-----
Find the minimum ship capacity needed to ship all packages within D days.
"""

from typing import List

class Solution:
    def find_days(self, weights: List[int], capacity: int) -> int:
        """
        Helper function to calculate the number of days required
        given a ship capacity.
        
        Args:
            weights (List[int]): List of package weights.
            capacity (int): Ship capacity to test.
            
        Returns:
            int: Total days needed to ship all packages.
        """
        total_days = 1
        current_load = 0

        for weight in weights:
            # If adding this package exceeds capacity, start a new day
            if current_load + weight > capacity:
                total_days += 1
                current_load = 0
            current_load += weight

        return total_days

    def shipWithinDays_bruteforce(self, weights: List[int], days: int) -> int:
        """
        Brute Force Solution:
        ---------------------
        Try every possible ship capacity from:
            - max(weights) (minimum possible)
            - sum(weights) (maximum possible)
            
        For each capacity, check if we can ship within D days.
        Return the first valid capacity.
        
        Time Complexity: O((sum(weights) - max(weights)) * n)
        Space Complexity: O(1)

        Dry Run Example:
        ----------------
        Input: weights = [3,2,2,4,1,4], days = 3

        - start = max(weights) = 4
        - end = sum(weights) = 16

        Try capacity = 4 → requires 5 days ❌
        Try capacity = 5 → requires 4 days ❌
        Try capacity = 6 → requires 3 days ✅  (Answer = 6)
        """
        start_weight = max(weights)   # Minimum possible capacity
        end_weight = sum(weights)     # Maximum possible capacity
        
        for w in range(start_weight, end_weight + 1):
            total_days_taken = self.find_days(weights, w)
            if total_days_taken <= days:
                return w   # First valid capacity found
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Optimal Solution (Binary Search):
        ---------------------------------
        Use binary search on the range [max(weights), sum(weights)].
        
        - If mid capacity works within D days → try smaller capacity (move left).
        - Otherwise → need larger capacity (move right).
        
        Why binary search?
        ------------------
        The function "days needed" is monotonic:
        - As capacity increases → required days decrease.
        
        Time Complexity: O(n * log(sum(weights) - max(weights)))
        Space Complexity: O(1)

        Dry Run Example:
        ----------------
        Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5

        - low = max(weights) = 10
        - high = sum(weights) = 55

        Iteration 1: mid = (10+55)//2 = 32 → days = 2 (≤5) → try smaller → high = 31
        Iteration 2: mid = (10+31)//2 = 20 → days = 3 (≤5) → try smaller → high = 19
        Iteration 3: mid = (10+19)//2 = 14 → days = 6 (>5) → too small → low = 15
        Iteration 4: mid = (15+19)//2 = 17 → days = 4 (≤5) → try smaller → high = 16
        Iteration 5: mid = (15+16)//2 = 15 → days = 5 (≤5) → try smaller → high = 14

        Loop ends → low = 15 (Answer)
        """
        low = max(weights)   # Lower bound (must fit the heaviest package)
        high = sum(weights)  # Upper bound (all in one day)
        
        while low <= high:
            mid = (low + high) // 2
            numberOfDays = self.find_days(weights, mid)
            
            if numberOfDays <= days:
                # Capacity is valid, try smaller
                high = mid - 1
            else:
                # Too small, need bigger capacity
                low = mid + 1
        
        return low   # Minimum valid capacity found


# ---------------------------
# ✅ Example Test Cases
# ---------------------------
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    weights = [1,2,3,4,5,6,7,8,9,10]
    days = 5
    print("Brute Force:", sol.shipWithinDays_bruteforce(weights, days))  # Expected 15
    print("Binary Search:", sol.shipWithinDays(weights, days))          # Expected 15

    # Example 2
    weights = [3,2,2,4,1,4]
    days = 3
    print("Brute Force:", sol.shipWithinDays_bruteforce(weights, days))  # Expected 6
    print("Binary Search:", sol.shipWithinDays(weights, days))          # Expected 6

    # Example 3
    weights = [1,2,3,1,1]
    days = 4
    print("Brute Force:", sol.shipWithinDays_bruteforce(weights, days))  # Expected 3
    print("Binary Search:", sol.shipWithinDays(weights, days))          # Expected 3

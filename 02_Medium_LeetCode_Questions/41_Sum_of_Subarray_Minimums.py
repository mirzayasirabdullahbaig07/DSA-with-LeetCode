"""
PROBLEM: Sum of Subarray Minimums
--------------------------------------
Given an array of integers `arr`, we need to find the sum of the minimum element
of every possible contiguous subarray.

Since the answer can be very large, return it modulo (10^9 + 7).

Example:
---------
Input: arr = [3, 1, 2, 4]
Output: 17

Explanation:
------------
All possible subarrays are:
[3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]

Their minimums are:
 3, 1, 2, 4, 1, 1, 2, 1, 1, 1
Sum = 17

--------------------------------------
There are TWO main approaches:
1 Brute Force (O(n^2))
2 Optimal Monotonic Stack (O(n))
--------------------------------------
"""

# =====================================================================
# 1. BRUTE FORCE SOLUTION (For understanding)
# =====================================================================

class BruteForceSolution:
    def sumSubarrayMins(self, arr):
        """
        Intuition:
        -----------
        - Enumerate all subarrays starting at i and ending at j.
        - For each subarray arr[i..j], find its minimum.
        - Add up all the minimums modulo (10^9 + 7).
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """

        MOD = 10**9 + 7         # Because result can be large
        total_sum = 0           # Will store final result
        n = len(arr)

        # Outer loop for start index
        for i in range(n):
            current_min = float("inf")  # Initialize with infinity
            # Inner loop for end index
            for j in range(i, n):
                # Keep track of running minimum in subarray arr[i..j]
                current_min = min(current_min, arr[j])
                # Add the minimum of current subarray
                total_sum = (total_sum + current_min) % MOD

        return total_sum


"""
Brute Force Summary:
-----------------------
 Works correctly but slow (O(n^2))
 Good for learning conceptually.
 Not suitable for large arrays (up to 30,000 elements).
"""

# =====================================================================
# 2. OPTIMAL SOLUTION using Monotonic Stack (O(n))
# =====================================================================

class OptimalStackSolution:
    def sumSubarrayMins(self, arr):
        """
        Intuition:
        -----------
        Each element arr[i] acts as the minimum for certain subarrays.
        We find:
        - How many subarrays on the LEFT can start before i (where arr[i] is still min)
        - How many subarrays on the RIGHT can end after i (where arr[i] remains min)

        The total number of subarrays where arr[i] is the minimum = left * right

        Then, arr[i]'s contribution = arr[i] * left * right

        Sum over all elements gives final answer.
        """

        MOD = 10**9 + 7
        n = len(arr)

        # Arrays to store indices of Previous Less Element (PLE) and Next Less Element (NLE)
        ple = [-1] * n  # Default -1 means no smaller element to the left
        nle = [n] * n   # Default n means no smaller element to the right

        stack = []

        # Step 1: Find PLE (Previous Less Element)
        # ------------------------------------------
        # Traverse left to right
        for i in range(n):
            # Maintain a monotonic increasing stack (strictly increasing)
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            ple[i] = stack[-1] if stack else -1
            stack.append(i)

        # Reset stack for next pass
        stack = []

        # Step 2: Find NLE (Next Less Element)
        # ------------------------------------------
        # Traverse right to left
        for i in range(n - 1, -1, -1):
            # Maintain a monotonic stack, but use >= to handle duplicates properly
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nle[i] = stack[-1] if stack else n
            stack.append(i)

        # Step 3: Calculate total contribution
        result = 0
        for i in range(n):
            left = i - ple[i]      # distance to left boundary
            right = nle[i] - i     # distance to right boundary
            # arr[i] contributes arr[i] * left * right
            result = (result + arr[i] * left * right) % MOD

        return result


"""
WHY “>” for PLE and “>=” for NLE?
-------------------------------------
- To handle duplicates and prevent double-counting.
- PLE uses ">" so that equal elements break to the right.
- NLE uses ">=" so that equal elements break to the left.
- This ensures each subarray's minimum is counted exactly once.

 Time Complexity: O(n)
 Space Complexity: O(n)
 Handles duplicates and large arrays efficiently.
"""

# =====================================================================
# TESTING BOTH SOLUTIONS
# =====================================================================

if __name__ == "__main__":
    arr1 = [3, 1, 2, 4]
    arr2 = [11, 81, 94, 43, 3]

    brute = BruteForceSolution()
    optimal = OptimalStackSolution()

    print(" Brute Force Output 1:", brute.sumSubarrayMins(arr1))
    print(" Optimal Output 1:", optimal.sumSubarrayMins(arr1))  # Expected 17

    print(" Brute Force Output 2:", brute.sumSubarrayMins(arr2))
    print(" Optimal Output 2:", optimal.sumSubarrayMins(arr2))  # Expected 444

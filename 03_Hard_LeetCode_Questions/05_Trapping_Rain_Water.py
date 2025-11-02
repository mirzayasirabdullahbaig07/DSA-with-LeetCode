"""
Problem: Trapping Rain Water

Given `n` non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example:
---------
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: 6 units of rainwater are trapped between bars.

Intuition:
-----------
Think of the heights as buildings. Water can be trapped only between two taller bars,
and the height of trapped water at any point depends on the shorter of the tallest bars
to the left and right.

Key Formula:
----------------
For each index i:
    Water[i] = min(max_left[i], max_right[i]) - height[i]
    
If the value is negative → no water trapped.

This problem is about **finding how much area (volume) of water**
can accumulate between the elevations.

Why this problem is important:
-------------------------------
 Common interview question (FAANG)
 Tests logic, arrays, and optimization ability
 Relates to real-world problems like terrain modeling, fluid simulation, etc.

Let's go step by step 
"""

# =============================================================
# Approach 1: Brute Force (Prefix & Suffix Arrays)
# =============================================================

"""
 Idea:
For each index i:
 - Find the tallest bar on the left (prefixMax[i])
 - Find the tallest bar on the right (suffixMax[i])
 - The water at i = min(prefixMax[i], suffixMax[i]) - height[i]

We precompute both arrays to speed it up from O(n²) → O(n).

 Why it works:
Water at any point is limited by the smaller of the highest walls on each side.

 Time Complexity: O(n)
 Space Complexity: O(2n) = O(n)
"""

from typing import List

class BruteForceSolution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        n = len(height)

        # Step 1: Initialize prefix and suffix max arrays
        prefixMax = [0] * n
        suffixMax = [0] * n

        # Step 2: Fill prefix max (tallest from left to right)
        prefixMax[0] = height[0]
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i - 1], height[i])

        # Step 3: Fill suffix max (tallest from right to left)
        suffixMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            suffixMax[i] = max(suffixMax[i + 1], height[i])

        # Step 4: Calculate total trapped water
        trapped_water = 0
        for i in range(n):
            trapped_water += min(prefixMax[i], suffixMax[i]) - height[i]

        return trapped_water


"""
Example:
height = [0,1,0,2,1,0,1,3,2,1,2,1]
prefixMax = [0,1,1,2,2,2,2,3,3,3,3,3]
suffixMax = [3,3,3,3,3,3,3,3,2,2,2,1]
Trapped water = 6 units
"""


# =============================================================
# Approach 2: Better Solution (One Suffix Array + Running LeftMax)
# =============================================================

"""
 Idea:
We only need one full array for the right side (rightMax)
and keep a single variable `leftMax` as we move left → right.

For each index:
    Water[i] = min(leftMax, rightMax[i]) - height[i]

 Why it works:
We can compute the right max in one pass,
and then keep updating the left max while iterating again.

 Time Complexity: O(n)
 Space Complexity: O(n)
"""

class BetterSolution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        # Step 1: Precompute rightMax array
        rightMax = [0] * n
        rightMax[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        # Step 2: Traverse and calculate using running leftMax
        leftMax = 0
        trapped_water = 0
        for i in range(n):
            leftMax = max(leftMax, height[i])
            trapped_water += min(leftMax, rightMax[i]) - height[i]

        return trapped_water


"""
 Explanation:
We eliminate one array (prefixMax), saving memory.
Still O(n) time, O(n) space, but simpler and more efficient.
"""


# =============================================================
# Approach 3: Optimal Solution (Two Pointer Technique)
# =============================================================

"""
 Idea:
Use two pointers — one at the left and one at the right.

Logic:
 - Water level is limited by the smaller side.
 - If left height < right height:
      - If height[left] < leftMax → water += leftMax - height[left]
      - Else update leftMax
      - Move left++
 - Else do the same for right pointer

 Why it works:
We always move the pointer at the smaller height side
because water trapped depends on the shorter wall.

 Time Complexity: O(n)
 Space Complexity: O(1)
 Fastest and most memory efficient
"""

class OptimalSolution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        trapped_water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    trapped_water += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    trapped_water += rightMax - height[right]
                right -= 1

        return trapped_water


"""
 Why this is the best:
- Single pass (O(n))
- Constant memory (O(1))
- Works efficiently even for large data

 Real-World Use:
Used in hydrology, topographic analysis, and
AI simulation of terrain and liquid behavior.

 Example:
height = [4,2,0,3,2,5]
Output: 9 units of trapped water
"""


# =============================================================
# Testing All Three Solutions
# =============================================================

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]

    print("Brute Force Result:", BruteForceSolution().trap(height))
    print("Better Solution Result:", BetterSolution().trap(height))
    print("Optimal Solution Result:", OptimalSolution().trap(height))

"""
Expected Output:
----------------
Brute Force Result: 6
Better Solution Result: 6
Optimal Solution Result: 6

Summary of Approaches:
| Approach | Time Complexity | Space Complexity | Comment |
|-----------|----------------|------------------|----------|
| Brute Force | O(n) | O(n) | Easy to understand |
| Better | O(n) | O(n) | Less memory usage |
| Optimal | O(n) | O(1) | Best for interviews & production |
"""

"""
========================================================
Problem: Asteroid Collision (LeetCode #735)
========================================================
We are given an array `asteroids` of integers representing asteroids in a row.

- Each asteroid's absolute value represents its size.
- The sign represents its direction:
    + Positive → moving right
    + Negative → moving left
- All asteroids move at the same speed.

When two asteroids moving in opposite directions meet:
--------------------------------------------------------
- The smaller one explodes.
- If both have the same size → both explode.
- Asteroids moving in the same direction never meet.

Goal:
--------------------------------------------------------
Return the final state of the asteroids after all collisions.

--------------------------------------------------------
Examples:
--------------------------------------------------------
Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation:
10 and -5 collide → 10 survives (bigger)
5 and 10 never meet → result = [5,10]

Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation:
8 and -8 collide → both have same size → both explode.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation:
2 and -5 collide → -5 survives.
Then 10 and -5 collide → 10 survives → result = [10]

--------------------------------------------------------
Constraints:
--------------------------------------------------------
2 <= asteroids.length <= 10^4
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
========================================================


========================================================
Intuition
========================================================
👉 Use a **stack** to simulate the collision process.

Why stack?
- Right-moving asteroids (+) are stored because they can collide
  with a future left-moving one (−).
- When we meet a left-moving asteroid:
  - Compare it with the stack's right-moving top(s).
  - Destroy smaller right movers until:
      • The stack is empty (no collision possible), OR
      • We find an equal-sized asteroid (both explode), OR
      • We find a left mover (no collision possible).

Thus, each asteroid is pushed/popped at most once → O(n) time.

========================================================
Algorithm
========================================================
1️⃣ Initialize an empty stack `st`.
2️⃣ Traverse each asteroid `a` in asteroids:
    - If `a > 0`: push it (moving right).
    - If `a < 0`: handle collisions with right-movers in stack:
        🔹 While top is smaller right mover → pop (destroy).
        🔹 If top is equal-sized right mover → pop both.
        🔹 If stack empty or top is left mover → push current left mover.
3️⃣ Return the final stack state as the remaining asteroids.

========================================================
Python Implementation
========================================================
"""

class Solution:
    def asteroidCollision(self, asteroids):
        """
        Simulates asteroid collisions using a stack.

        :param asteroids: List[int] → asteroid sizes and directions
        :return: List[int] → remaining asteroids after collisions
        """

        st = []  # Stack to store stable asteroids

        for a in asteroids:
            # Case 1: Moving right → safe for now, push it
            if a > 0:
                st.append(a)

            # Case 2: Moving left → potential collisions
            else:
                # Handle all smaller right movers
                while st and st[-1] > 0 and st[-1] < abs(a):
                    st.pop()  # smaller right asteroid destroyed

                # Equal size → both explode
                if st and st[-1] == abs(a):
                    st.pop()

                # Stack empty OR top is left-moving → safe to add
                elif not st or st[-1] < 0:
                    st.append(a)

        return st


"""
========================================================
Dry Run Example
========================================================
Input: asteroids = [5, 10, -5]

Step 1: a = 5  → right → push → st = [5]
Step 2: a = 10 → right → push → st = [5, 10]
Step 3: a = -5 → left  → check collisions
        - Top = 10 > 0 and 10 > 5 → |10| > 5 → 10 survives
        - -5 destroyed
Output: [5, 10]

--------------------------------------------------------
Another Example:
Input: [10, 2, -5]
st = []
a=10 → push → [10]
a=2 → push → [10,2]
a=-5 → left:
    - st[-1]=2<5 → pop(2)
    - st[-1]=10>5 → -5 destroyed
Result = [10]
========================================================


========================================================
Time & Space Complexity
========================================================
Operation          Time      Explanation
--------------------------------------------------------
Each asteroid      O(1)*     Pushed/popped at most once
Overall            O(n)
Space              O(n)      For stack (no collisions case)

========================================================
Key Takeaways
========================================================
✔ Stack simulates forward-in-time collisions perfectly.
✔ Each asteroid interacts only once per collision chain.
✔ Pattern generalizes to other “directional interaction” problems
  (e.g., merging intervals, collapsing particles, or physics simulations).

========================================================
Technique Used
========================================================
Monotonic Stack Simulation — Used for resolving directional interactions
between entities that may collide, cancel, or dominate each other.
========================================================
"""


# ========================================================
# Testing the Asteroid Collision Function
# ========================================================
if __name__ == "__main__":
    sol = Solution()

    print("Example 1:", sol.asteroidCollision([5,10,-5]))   # [5,10]
    print("Example 2:", sol.asteroidCollision([8,-8]))      # []
    print("Example 3:", sol.asteroidCollision([10,2,-5]))   # [10]
    print("Example 4:", sol.asteroidCollision([3,5,-6,2,-1,4]))  # [-6,2,4]

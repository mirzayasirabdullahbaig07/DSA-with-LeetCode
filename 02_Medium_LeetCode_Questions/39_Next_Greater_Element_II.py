"""
========================================================
Problem: Next Greater Element II (LeetCode #503)
========================================================
Given a **circular integer array** `nums` (i.e., the next element of
`nums[nums.length - 1]` is `nums[0]`), return the **next greater number**
for every element in `nums`.

The next greater number of an element `x` is the **first greater number**
to its right in traversal order — and since the array is circular, it may
wrap around to the start. If such a number doesn't exist, return `-1`.

--------------------------------------------------------
Example:
--------------------------------------------------------
Input 1:
nums = [1, 2, 1]
Output: [2, -1, 2]
Explanation:
- The first 1 → next greater is 2.
- The 2 → has no greater element, return -1.
- The second 1 → circularly finds 2 as the next greater.

Input 2:
nums = [1, 2, 3, 4, 3]
Output: [2, 3, 4, -1, 4]

--------------------------------------------------------
Constraints:
--------------------------------------------------------
1 <= len(nums) <= 10^4
-10^9 <= nums[i] <= 10^9

=======================================================
Problem Intuition
========================================================
In the normal "Next Greater Element" problem (non-circular), you can scan
from **right to left** while maintaining a **monotonic decreasing stack**.

But in this circular version:
- Each element’s next greater element could be found *after* looping to
  the start of the array again.
- So, we simulate this by traversing the array **twice** using `i % n`.

========================================================
🪜 Brute Force Idea (Inefficient)
========================================================
For each element, loop through all elements to its right (circularly)
until you find a greater number.

--------------------------------------------------------
Algorithm:
--------------------------------------------------------
1. For each i in range(n):
    - Search j = (i + 1) % n repeatedly until:
      - nums[j] > nums[i] → record it
      - or back to i → return -1
2. Store results in a list.

--------------------------------------------------------
Time Complexity: O(n²)
Space Complexity: O(n)
--------------------------------------------------------
This is **too slow** for large inputs.
We need an O(n) optimized approach.

========================================================
Optimal Solution: Using Monotonic Stack
========================================================
Intuition:
--------------------------------------------------------
We can handle the circular nature by looping the array **2 times**.
This ensures that even the last elements can check future elements
beyond the end.

For each element (from right to left):
- Pop smaller/equal elements from the stack (they can’t be next greater).
- The top of the stack (if any) is the next greater element.
- Push the current element to the stack.

========================================================
Step-by-Step Algorithm:
========================================================
1 Initialize:
    - n = len(nums)
    - result = [-1] * n
    - stack = []  # monotonic decreasing stack

2 Traverse from (2*n - 1) → 0 (simulate circular array):
    - While stack not empty and stack[-1] <= nums[i % n]:
        pop() smaller elements
    - If i < n (first pass only):
        - If stack not empty:
            result[i] = stack[-1]  # top is next greater
    - Push nums[i % n] onto stack

3 Return `result`.

========================================================
Python Implementation:
========================================================
"""

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n    # Initialize all with -1 (default)
        stack = []           # Monotonic decreasing stack

        # Traverse twice to simulate circular behavior
        for i in range(2 * n - 1, -1, -1):
            # Remove smaller or equal elements (not useful)
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()

            # For first pass only (i < n)
            if i < n:
                if stack:
                    result[i] = stack[-1]

            # Push current element
            stack.append(nums[i % n])

        return result


"""
========================================================
Dry Run Example:
========================================================
Input:
nums = [1, 2, 1]

Process (Right → Left, 2 loops simulated):

i = 5 → nums[2]=1 → stack=[] → push(1)
i = 4 → nums[1]=2 → pop(1), stack=[] → push(2)
i = 3 → nums[0]=1 → stack top=2 → result[0]=2 → push(1)

First real pass:
i = 2 → nums[2]=1 → stack top=2 → result[2]=2 → push(1)
i = 1 → nums[1]=2 → pop(1), pop(2) → stack empty → result[1]=-1 → push(2)
i = 0 → nums[0]=1 → stack top=2 → result[0]=2

Final Result: [2, -1, 2]

========================================================
Complexity Analysis:
========================================================
Time Complexity:  O(n)
    - Each element pushed/popped at most twice.
Space Complexity: O(n)
    - Stack and result list of size n.

========================================================
Summary Table:
========================================================
| Approach         | Time Complexity | Space Complexity | Technique Used           |
|------------------|-----------------|------------------|---------------------------|
| Brute Force      | O(n²)           | O(n)             | Nested loops              |
| Monotonic Stack  | O(n)            | O(n)             | Stack + Modulo iteration  |

========================================================
Key Takeaways:
========================================================
- Simulate circular arrays by traversing twice (2 * n) using modulo.
- Use a **monotonic decreasing stack** to efficiently find NGEs.
- This is a standard stack pattern used in many NGE problems.
- Time-efficient (O(n)) and space-balanced (O(n)).

========================================================
Testing:
========================================================
"""

if __name__ == "__main__":
    solution = Solution()
    print("Example 1 →", solution.nextGreaterElements([1, 2, 1]))       # [2, -1, 2]
    print("Example 2 →", solution.nextGreaterElements([1, 2, 3, 4, 3])) # [2, 3, 4, -1, 4]

"""
========================================================
Problem: Min Stack (LeetCode #155)
========================================================
Design a stack that supports push, pop, top, and retrieving the
minimum element — all in constant time (O(1)).

--------------------------------------------------------
Problem Statement:
--------------------------------------------------------
Implement a class MinStack with the following methods:
- MinStack() → initializes the stack.
- push(val) → pushes val onto the stack.
- pop() → removes the top element.
- top() → returns the top element.
- getMin() → retrieves the minimum element in O(1).

--------------------------------------------------------
Example:
--------------------------------------------------------
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output:
[null,null,null,null,-3,null,0,-2]

Explanation:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin() → -3
minStack.pop()
minStack.top() → 0
minStack.getMin() → -2

--------------------------------------------------------
Constraints:
--------------------------------------------------------
-2^31 <= val <= 2^31 - 1
At most 3 * 10^4 operations will be made.
All pop, top, getMin are called on non-empty stacks.

========================================================
Brute Force Idea (Inefficient)
========================================================
Use a single stack.
- For `getMin()`, traverse the stack to find the minimum.
- This leads to O(n) per getMin().

Time Complexity: O(n)
Space Complexity: O(n)

This is inefficient and not acceptable in interviews or large systems.

========================================================
Optimal Solution (O(1) Min Retrieval)
========================================================
Intuition:
--------------------------------------------------------
We store **pairs** in the stack:
(value, current_min)

Whenever a new value is pushed:
- If the stack is empty → (val, val)
- Otherwise → compare val with stack[-1][1] (previous min)
  and store the smaller one as the new min.

--------------------------------------------------------
Algorithm:
--------------------------------------------------------
1 Initialize an empty list `stack`.
2 On push(val):
     - If empty → push (val, val)
     - Else → push (val, min(val, stack[-1][1]))
3 On pop():
     - stack.pop()
4 On top():
     - Return stack[-1][0]
5 On getMin():
     - Return stack[-1][1]

--------------------------------------------------------
Python Implementation:
--------------------------------------------------------
"""

class MinStack:
    def __init__(self):
        # Stack holds tuples of (value, current_min)
        self.stack = []

    def push(self, val: int) -> None:
        """Push val along with current minimum."""
        if not self.stack:
            # First element → itself is the min
            self.stack.append((val, val))
        else:
            # Compare new value with current minimum
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        """Remove the top element."""
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        """Return the top element value."""
        if not self.stack:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        """Return the minimum element in the stack."""
        if not self.stack:
            return None
        return self.stack[-1][1]


"""
--------------------------------------------------------
Dry Run Example:
--------------------------------------------------------
Operations:
minStack = MinStack()
minStack.push(3)   → stack = [(3,3)]
minStack.push(5)   → stack = [(3,3),(5,3)]
minStack.push(2)   → stack = [(3,3),(5,3),(2,2)]
minStack.push(1)   → stack = [(3,3),(5,3),(2,2),(1,1)]
minStack.push(4)   → stack = [(3,3),(5,3),(2,2),(1,1),(4,1)]

minStack.getMin() → 1
minStack.pop()    → removes (4,1)
minStack.getMin() → 1
minStack.pop()    → removes (1,1)
minStack.getMin() → 2
minStack.top()    → 2

--------------------------------------------------------
Time and Space Complexity:
--------------------------------------------------------
Operation     Time     Space
----------------------------------
push()        O(1)     O(1)
pop()         O(1)     O(1)
top()         O(1)     O(1)
getMin()      O(1)     O(1)
----------------------------------
Overall       O(1)     O(n)

--------------------------------------------------------
Technique Used:
--------------------------------------------------------
Stack with auxiliary tracking — store both the value
and the current minimum to make getMin() constant time.

--------------------------------------------------------
Key Takeaways:
--------------------------------------------------------
- getMin() achieved in O(1) using pair storage.
- Elegant space-time tradeoff (store extra data with each push).
- Core interview concept for mastering stack design problems.
"""

# ========================================================
# Testing the MinStack class
# ========================================================
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print("Current Min:", minStack.getMin())  # -3
    minStack.pop()
    print("Top Element:", minStack.top())      # 0
    print("Current Min:", minStack.getMin())  # -2

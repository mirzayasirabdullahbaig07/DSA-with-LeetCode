"""
------------------------------------------------------------
Problem: LeetCode 232 — Implement Queue using Stacks
------------------------------------------------------------
You are asked to implement a FIFO (First-In-First-Out) queue
using only standard operations of a stack:
 - push to top
 - pop/peek from top
 - size
 - isEmpty

You must design a class `MyQueue` with methods:
    1 push(x)
    2 pop()
    3 peek()
    4 empty()

------------------------------------------------------------
Example:
------------------------------------------------------------
Input:
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]

Output:
[null, null, null, 1, 1, false]

Explanation:
MyQueue myQueue = new MyQueue()
myQueue.push(1)     → queue: [1]
myQueue.push(2)     → queue: [1, 2]
myQueue.peek()      → returns 1
myQueue.pop()       → returns 1, queue becomes [2]
myQueue.empty()     → returns False

------------------------------------------------------------
Constraints:
------------------------------------------------------------
1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All calls to pop and peek are valid.

Follow-up:
Can you make each operation run in amortized O(1) time?
------------------------------------------------------------


============================================================
BRUTE FORCE APPROACH — Using Two Stacks (Reordering Each Time)
============================================================

Intuition:
-------------
A stack follows LIFO order, but a queue follows FIFO order.
We can simulate FIFO using two stacks by ensuring that the 
oldest element is always at the top of one of the stacks.

Idea:
1. Use two stacks — stack1 and stack2.
2. For each push(x):
   - Move all elements from stack1 to stack2.
   - Push x into stack1.
   - Move all elements back from stack2 to stack1.
   → This ensures that the oldest element stays at the top.
3. For pop/peek, just use stack1’s top element.
4. For empty, check if stack1 is empty.

Why it works:
-------------
By reversing elements during every push, we ensure 
that the front of the queue always stays at the top of stack1.

Algorithm:
-------------
1. push(x):
   - Move all items from stack1 → stack2
   - Push x into stack1
   - Move all items back from stack2 → stack1
2. pop():
   - Pop from stack1
3. peek():
   - Return top of stack1
4. empty():
   - Return True if stack1 is empty

Time Complexity:
----------------
push(): O(n) — need to move all elements twice
pop():  O(1)
peek(): O(1)
empty(): O(1)

Space Complexity:
-----------------
O(n) — due to two stacks storing elements

Technique Used:
----------------
- Stack Simulation
- Order Reversal

"""

class MyQueue:
    def __init__(self):
        self.stack1 = []  # Main stack (represents queue)
        self.stack2 = []  # Helper stack

    def push(self, x: int) -> None:
        """
        Push x to back of queue by reordering all elements.
        """
        # Step 1: Move all elements to helper stack
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        # Step 2: Push new element into stack1
        self.stack1.append(x)
        # Step 3: Move all back to stack1 (restore order)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        """Remove front element (top of stack1)."""
        return self.stack1.pop()

    def peek(self) -> int:
        """Return front element without removing."""
        return self.stack1[-1]

    def empty(self) -> bool:
        """Return True if queue is empty."""
        return len(self.stack1) == 0



"""
Simplifying It:
----------------
Imagine two baskets (stacks).
When you add a new ball (push), 
you first empty basket A into basket B, 
put the new ball in A, then move everything back.
Now the oldest ball stays at the bottom,
so when you pop, you always get the front of the queue first.

This ensures FIFO but costs more time on each push.
"""


# ============================================================
# OPTIMAL APPROACH — Using Two Stacks (Amortized O(1))
# ============================================================

"""
Intuition:
-------------
Instead of rearranging on every push, 
we can delay it until absolutely necessary (lazy approach).

We use:
- in_stack  → receives new elements (acts like queue’s back)
- out_stack → gives elements in queue order (acts like front)

When we need to pop or peek:
- If out_stack is empty → move all elements from in_stack → out_stack.
  (This reverses their order)
- Then pop/peek from out_stack directly.

This ensures FIFO order efficiently, as each element
is moved at most once.

Algorithm:
-------------
1. push(x):
   - Push x into in_stack.
2. pop():
   - If out_stack is empty, move all elements from in_stack → out_stack.
   - Pop from out_stack.
3. peek():
   - If out_stack is empty, move all elements from in_stack → out_stack.
   - Return the top element of out_stack.
4. empty():
   - Return True if both in_stack and out_stack are empty.

Why It Works:
--------------
The first stack collects elements, 
and the second reverses them only when needed.
This lazy evaluation reduces redundant transfers.

Time Complexity:
----------------
push():  O(1)
pop():   Amortized O(1)
peek():  Amortized O(1)
empty(): O(1)

Space Complexity:
-----------------
O(n) — total elements in both stacks

Technique Used:
----------------
- Lazy Transfer / Deferred Computation
- Amortized Analysis
- Data Structure Simulation (Queue using Stacks)
"""

class MyQueue:
    def __init__(self):
        # Two stacks for managing input and output
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        """Push element x to the back of queue."""
        self.in_stack.append(x)

    def pop(self) -> int:
        """Remove and return the front element."""
        self.peek()  # Ensure front is ready in out_stack
        return self.out_stack.pop()

    def peek(self) -> int:
        """Return the front element."""
        if not self.out_stack:
            # Transfer all elements from in_stack → out_stack
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        """Check if the queue is empty."""
        return not self.in_stack and not self.out_stack



"""
Simplifying It:
----------------
Think of in_stack as a loading dock and out_stack as a delivery truck.

When you push(x), you load new items at the dock (in_stack).
When you pop(), if the truck (out_stack) is empty,
you transfer all items from the dock to the truck — reversing the order.

Now, the oldest item is at the top of the truck, ready for delivery.
Each item is moved only once, keeping everything efficient.
"""


# ============================================================
# COMPARISON SUMMARY
# ============================================================
"""
| Approach              | push() | pop() | peek() | Space | Concept              |
|------------------------|--------|-------|--------|--------|----------------------|
| Two Stacks (Brute)     | O(n)   | O(1)  | O(1)   | O(n)  | Reorder on each push |
| Two Stacks (Optimal)   | O(1)   | O(1)* | O(1)*  | O(n)  | Lazy transfer        |

*Amortized O(1): Each element is moved at most once.

Key Idea:
----------
Brute Force: Reverses every time during push → expensive insertions.
Optimal: Reverses only when needed → efficient overall.

Technique Used:
----------------
- Stack Simulation
- Lazy Transfer / Amortized Time Optimization
- Order Reversal Logic

Real-World Analogy:
--------------------
Imagine a conveyor belt (in_stack) loading boxes into a truck (out_stack).
You don’t reload every time a new box arrives.
You only move boxes when the truck is empty and needs to deliver again.
That’s the essence of amortized optimization here.
"""

# Example Test
queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())    # Output: 1
print(queue.pop())     # Output: 1
print(queue.empty())   # Output: False

"""
 Problem: LeetCode 225 — Implement Stack using Queues
--------------------------------------------------------
You are asked to implement a LIFO (Last-In-First-Out) stack using
only standard operations of a queue:
 - push to back
 - peek/pop from front
 - size
 - isEmpty

You must design a class `MyStack` with methods:
    1 push(x)
    2 pop()
    3 top()
    4 empty()

Constraints:
-------------
1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All pop/top calls are valid.

Follow-up:
Can you implement it using only **one queue**?

Example:
---------
Input:
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output:
[null, null, null, 2, 2, false]

Explanation:
-------------
MyStack myStack = new MyStack()
myStack.push(1)
myStack.push(2)
myStack.top()    2
myStack.pop()    2
myStack.empty()  False
"""

# ============================================================
#  BRUTE FORCE APPROACH — Using Two Queues
# ============================================================
"""
 Intuition:
-------------
We use two queues to simulate stack behavior.

Queue works on FIFO (First In First Out),
Stack works on LIFO (Last In First Out).

We can reverse the order in queues during `push()`
to make the newly added element come to the "front" of q1,
so that `pop()` or `top()` directly returns the latest element.

 Algorithm:
--------------
1 Initialize two queues → q1 (main), q2 (helper)
2 push(x):
    - Enqueue x into q2
    - Move all elements from q1 → q2 (so order reverses)
    - Swap q1 and q2
3 pop():
    - Dequeue from q1 (top of stack)
4 top():
    - Peek the front of q1
5 empty():
    - Check if q1 is empty

 Technique Used:
------------------
 Queue Simulation
 Reversing Order Logic
 O(n) insertion to maintain LIFO behavior

 Time Complexity:
-------------------
push():  O(n) — need to move n elements
pop():   O(1)
top():   O(1)
empty(): O(1)

 Space Complexity:
--------------------
O(n) — two queues store up to n elements
"""

from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()  # Main queue
        self.q2 = deque()  # Helper queue

    def push(self, x: int) -> None:
        """
        Add x to the stack.
        Steps:
        1. Add new element to q2
        2. Move all elements from q1 → q2 (reverse order)
        3. Swap q1 and q2
        """
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        """Remove and return the top element (front of q1)."""
        return self.q1.popleft()

    def top(self) -> int:
        """Return the top element without removing."""
        return self.q1[0]

    def empty(self) -> bool:
        """Return True if stack is empty."""
        return len(self.q1) == 0


"""
 Simplifying It:
------------------
Imagine two lines (queues).
When someone new arrives (push),
you make them stand in an empty line (q2),
then move everyone from q1 behind them.
Now the new person is at the front (like stack top).

Pop just removes the person at the front of q1 — O(1).
Push is costly (O(n)), but rest operations are fast.
"""


# ============================================================
#  OPTIMAL APPROACH — Using One Queue with Rotation
# ============================================================
"""
 Intuition:
-------------
We can use just one queue and rotate it during `push()`
so that the most recent element moves to the front.

When we insert a new element x,
we push it to the back of the queue,
then we move all other elements before it to the back again,
so x comes to the front (like top of the stack).

 Algorithm:
--------------
1 Initialize a single queue
2 push(x):
    - Enqueue x
    - Rotate: for (size - 1) times, dequeue front and enqueue back
3 pop():
    - Dequeue from front
4 top():
    - Peek front
5 empty():
    - Return True if queue is empty

 Technique Used:
------------------
 Queue Rotation
 Single Data Structure Optimization
 Reordering via Cyclic Shifts

 Time Complexity:
-------------------
push():  O(n) — rotates all existing elements
pop():   O(1)
top():   O(1)
empty(): O(1)

 Space Complexity:
--------------------
O(n) — single queue
"""

class MyStack:
    def __init__(self):
        self.queue = deque()  # Single queue used as stack

    def push(self, x: int) -> None:
        """
        Add x to stack and rotate queue so x becomes front.
        """
        self.queue.append(x)
        # Rotate (len - 1) times to move new element to front
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        """Remove top element (front of queue)."""
        return self.queue.popleft()

    def top(self) -> int:
        """Return top element (front of queue)."""
        return self.queue[0]

    def empty(self) -> bool:
        """Return True if stack is empty."""
        return len(self.queue) == 0


"""
 Simplifying It:
------------------
Imagine one line of people (queue).
You add a new person at the end (push),
then make everyone in front step behind them one by one,
until the new person becomes first.

This rotation puts the latest element at the front
so you can pop or peek easily (LIFO).

 Less space (only one queue)
 Same time complexity for push
 Cleaner, interview-preferred solution
"""


# ============================================================
#  SUMMARY COMPARISON
# ============================================================
"""
Approach Comparison Table:
---------------------------------------------------------------
| Approach              | push() | pop() | Space | Concept         |
|------------------------|--------|-------|--------|----------------|
| Two Queues (Brute)     | O(n)   | O(1)  | O(n)  | Reverse Order  |
| One Queue (Optimal)    | O(n)   | O(1)  | O(n)  | Queue Rotation |

 Brute Force: Easier to understand — uses extra queue for clarity
 Optimal: Saves space — uses rotation trick for efficiency

 Core Concept:
----------------
Simulate LIFO (stack) behavior using FIFO (queue)
by reversing element order at insertion time.

 Technique Used:
------------------
 Queue Manipulation
 Reordering / Rotation
 Data Structure Simulation

 Real-World Analogy:
-----------------------
Imagine a single queue in front of a ticket counter.
When a new VIP person comes, you make all others step behind
until the VIP reaches the front. That’s exactly what happens
in the “rotate” operation!
"""

# Example Test
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())    # Output: 2
print(stack.pop())    # Output: 2
print(stack.empty())  # Output: False

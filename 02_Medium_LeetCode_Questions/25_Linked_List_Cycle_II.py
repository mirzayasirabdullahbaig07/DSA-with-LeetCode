"""
Problem: Linked List Cycle II
-----------------------------
Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return None.

There is a cycle in a linked list if there is some node in the list that
can be reached again by continuously following the next pointer.
Note: Do not modify the linked list.

Follow-up:
Can you solve it using O(1) (i.e. constant) memory?

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0

Example 3:
Input: head = [1], pos = -1
Output: no cycle
"""

# ----------------------------------------------------------------
# Definition for singly-linked list.
# ----------------------------------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ----------------------------------------------------------------
# ✅ Solution 1: Brute Force Approach (Using Set)
# ----------------------------------------------------------------
class Solution_Set:
    """
    Intuition:
    -----------
    - Keep track of visited nodes using a set.
    - While traversing the list, if we encounter a node already in the set,
      that node is the starting point of the cycle.
    - If we reach the end (None), there is no cycle.
    """

    def detectCycle(self, head):
        visited = set()       # Store visited nodes
        temp = head           # Start traversal

        while temp:
            # If node already seen, it's the start of the cycle
            if temp in visited:
                return temp
            visited.add(temp)  # Mark node as visited
            temp = temp.next   # Move forward

        return None            # No cycle found


"""
Dry Run Example:
----------------
Linked List: 1 -> 2 -> 3 -> 4 -> 2 (cycle starts at node 2)

Step 1: visited = {}, temp = 1 → add 1
Step 2: visited = {1}, temp = 2 → add 2
Step 3: visited = {1,2}, temp = 3 → add 3
Step 4: visited = {1,2,3}, temp = 4 → add 4
Step 5: visited = {1,2,3,4}, temp = 2 (already seen) → cycle at node 2

Time Complexity  : O(n)
Space Complexity : O(n)
"""


# ----------------------------------------------------------------
# ✅ Solution 2: Optimal Approach (Floyd’s Cycle Detection Algorithm)
# ----------------------------------------------------------------
class Solution_Floyd:
    """
    Intuition:
    -----------
    This uses the classic "Tortoise and Hare" algorithm:
    1. Use two pointers — slow and fast.
    2. Move slow by 1 step, fast by 2 steps.
    3. If they meet, a cycle exists.
    4. Reset one pointer to head and move both one step at a time.
       They will meet exactly at the cycle start node.

    Why it works:
    --------------
    Let:
      L1 = distance from head to cycle start
      L2 = distance from cycle start to meeting point
      C  = cycle length

    Since fast moves twice as fast:
        2 * (L1 + L2) = L1 + L2 + k*C
    Simplify:
        L1 = C - L2
    → Meaning: the distance from head to cycle start equals the distance
      from meeting point to cycle start.
    """

    def detectCycle(self, head):
        slow, fast = head, head

        # Phase 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # Cycle detected
            if slow == fast:
                # Phase 2: Find cycle start
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow  # Start of cycle

        return None  # No cycle found


"""
Dry Run Example:
----------------
Linked List: 1 -> 2 -> 3 -> 4 -> 2 (cycle)

Phase 1: Detect Cycle
---------------------
Initial: slow = 1, fast = 1
Step 1: slow = 2, fast = 3
Step 2: slow = 3, fast = 2
Step 3: slow = 4, fast = 4 (meeting point found)

Phase 2: Find Start
-------------------
Reset slow to head
slow = 1, fast = 4
Move one step each:
slow = 2, fast = 2 → meet at node 2 (cycle start)

Time Complexity  : O(n)
Space Complexity : O(1)
"""


# ----------------------------------------------------------------
# 🔍 Example Usage (You can test this part locally)
# ----------------------------------------------------------------
if __name__ == "__main__":
    # Create a linked list with a cycle:
    # 3 -> 2 -> 0 -> -4
    #       ↑         |
    #       └─────────┘ (cycle at node with value 2)

    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Create cycle here

    solution = Solution_Floyd()
    cycle_node = solution.detectCycle(node1)

    if cycle_node:
        print(f"Cycle starts at node with value: {cycle_node.val}")
    else:
        print("No cycle found.")

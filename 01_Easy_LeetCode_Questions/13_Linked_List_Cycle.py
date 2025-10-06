"""
LeetCode 141: Linked List Cycle
-------------------------------

Problem:
------------
Given head, the head of a linked list, determine if the linked list has a cycle in it.

A cycle exists if some node can be reached again by continuously following the `next` pointer.
Return True if there is a cycle in the linked list, otherwise return False.

Problem Link:
https://leetcode.com/problems/linked-list-cycle/

Examples:
-------------
Input: head = [3,2,0,-4], pos = 1
Output: True
Explanation: There is a cycle where the tail connects to the 1st node.

Input: head = [1,2], pos = 0
Output: True
Explanation: There is a cycle where the tail connects to the 0th node.

Input: head = [1], pos = -1
Output: False
Explanation: There is no cycle.

Constraints:
---------------
- The number of nodes is in the range [0, 10⁴].
- -10⁵ <= Node.val <= 10⁵
- pos is -1 or a valid index in the linked list.

Follow-up:
Can you solve it using O(1) memory?
"""


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
------------------------------------------------------------
Solution 1: Brute Force (Using Set)
------------------------------------------------------------
Intuition:
-------------
Imagine walking through a maze and dropping a breadcrumb at every spot.
If you ever reach a place where a breadcrumb already exists, you’re walking in a circle!

Approach:
-------------
1. Use a set to store visited nodes.
2. Traverse the linked list one node at a time.
3. Before visiting each node, check if it’s already in the set.
4. If it is → cycle detected (return True).
5. If you reach the end (None) → no cycle (return False).

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def hasCycle_set(self, head: Optional[ListNode]) -> bool:
        temp = head
        visited = set()

        while temp:
            if temp in visited:
                return True  # Cycle detected
            visited.add(temp)
            temp = temp.next
        
        return False


"""
Dry Run Example:
--------------------
Input: 1 -> 2 -> 3 -> 2 (cycle from 3 back to 2)

Step 1: temp=1, visited={}
         add 1 → visited={1}
Step 2: temp=2, visited={1}
         add 2 → visited={1,2}
Step 3: temp=3, visited={1,2}
         add 3 → visited={1,2,3}
Step 4: temp=2, visited={1,2,3}
         2 already in visited → return True 

Result: Cycle Detected!
------------------------------------------------------------
"""


"""
------------------------------------------------------------
Solution 2: Optimal Approach (Floyd’s Cycle Detection)
------------------------------------------------------------
Intuition:
-------------
Think of two people running on a circular track — 
one runs slowly (1 step at a time), the other runs faster (2 steps at a time).
If the track is circular, the faster runner will eventually lap the slower one.

Approach:
-------------
1. Create two pointers: slow and fast.
2. Move slow by 1 step, fast by 2 steps each iteration.
3. If slow == fast at any point → cycle detected.
4. If fast reaches the end (None) → no cycle.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True  # Cycle detected

        return False  # No cycle


"""
Dry Run Example:
--------------------
Input: 1 -> 2 -> 3 -> 4 -> 2 (cycle from 4 back to 2)

Initial: slow=1, fast=1

Step 1:
    slow=2, fast=3   (not equal)
Step 2:
    slow=3, fast=2   (not equal)
Step 3:
    slow=4, fast=4  equal → cycle detected!

Result: True (cycle exists)

------------------------------------------------------------
"""

"""
------------------------------------------------------------
Summary:
------------------------------------------------------------
Approach                  | Time  | Space | Difficulty | Best For
------------------------------------------------------------
Brute Force (Using Set)   | O(n)  | O(n)  | Easy       | Learning concept
Floyd’s Two Pointers      | O(n)  | O(1)  | Medium     | Production / Interviews
------------------------------------------------------------

Recommended Approach:
Use **Floyd’s Cycle Detection** for optimal efficiency.
The **Set-based** approach is easier to understand when learning linked lists.
------------------------------------------------------------
"""


# ---------------------------
# Example Test Code
# ---------------------------

def create_linked_list(values, pos):
    """
    Helper function to create a linked list.
    If pos != -1, connect the tail to the node at position 'pos' (0-indexed).
    """
    if not values:
        return None

    head = ListNode(values[0])
    curr = head
    nodes = [head]

    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
        nodes.append(curr)

    if pos != -1:
        curr.next = nodes[pos]  # Create cycle

    return head


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    head = create_linked_list([3,2,0,-4], 1)
    print("Example 1:", sol.hasCycle(head))  # Expected: True

    # Example 2
    head = create_linked_list([1,2], 0)
    print("Example 2:", sol.hasCycle(head))  # Expected: True

    # Example 3
    head = create_linked_list([1], -1)
    print("Example 3:", sol.hasCycle(head))  # Expected: False

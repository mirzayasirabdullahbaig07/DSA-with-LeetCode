"""
LeetCode 206: Reverse Linked List
---------------------------------

Problem:
------------
Given the head of a singly linked list, reverse the list and return the reversed list.

Problem Link:
https://leetcode.com/problems/reverse-linked-list/

Examples:
-------------
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []

Constraints:
---------------
- The number of nodes in the list is in the range [0, 5000].
- -5000 <= Node.val <= 5000

Follow-up:
A linked list can be reversed either iteratively or recursively. 
Could you implement both?

------------------------------------------------------------
Solution 1: Brute Force (Using Stack)
------------------------------------------------------------
Intuition:
-------------
Think of this like stacking plates! When you put plates on a stack, 
the last plate you put becomes the first one you take out.
We’ll use this same idea – store all the values in a stack, 
then put them back in reverse order.

Approach:
-------------
1. Traverse the linked list and store all node values in a stack.
2. Traverse again and replace each node’s value with values popped from the stack.
3. Stack follows LIFO (Last In, First Out), so it gives reverse order automatically.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList_stack(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        stack = []

        # First pass: Push all node values to stack
        while temp:
            stack.append(temp.val)
            temp = temp.next

        temp = head
        # Second pass: Pop values from stack and assign to nodes
        while temp:
            temp.val = stack.pop()
            temp = temp.next

        return head


"""
Dry Run Example:
--------------------
Input: 1 -> 2 -> 3

First Pass:
stack = [1, 2, 3]

Second Pass:
node 1: pop 3 → 3
node 2: pop 2 → 2
node 3: pop 1 → 1

Output: 3 -> 2 -> 1
------------------------------------------------------------
"""


"""
------------------------------------------------------------
Solution 2: Iterative (Optimal Solution)
------------------------------------------------------------
Intuition:
-------------
Imagine a line of people holding hands.
To face the opposite direction, we just change who’s holding whose hand!
Each node needs to point to the previous node instead of the next one.

Approach:
-------------
1. Keep track of three pointers: prev, curr, and next.
2. Reverse each link by making `curr.next = prev`.
3. Move all pointers forward by one step.
4. Continue until current node becomes None.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def reverseList_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            front = curr.next   # Store next node
            curr.next = prev    # Reverse current link
            prev = curr         # Move prev forward
            curr = front        # Move current forward

        return prev


"""
Dry Run Example:
--------------------
Input: 1 -> 2 -> 3

Initial:
prev = None, curr = 1

Iteration 1:
front = 2
curr.next = prev (1->None)
prev = 1, curr = 2

Iteration 2:
front = 3
curr.next = prev (2->1)
prev = 2, curr = 3

Iteration 3:
front = None
curr.next = prev (3->2)
prev = 3, curr = None

Output: 3 -> 2 -> 1
------------------------------------------------------------
"""


"""
------------------------------------------------------------
Solution 3: Recursive Approach
------------------------------------------------------------
Intuition:
-------------
Think of recursion as passing control down the chain.
Each node tells the next node: 
"Reverse the rest of the list, and when you're done, 
come back and connect me at the end."

Approach:
-------------
1. Base Case → If list is empty or single node, return head.
2. Recursively reverse the rest of the list.
3. Fix current connection:
   - Let front = head.next
   - Make front.next = head
   - Set head.next = None
4. Return new_head from recursion.

Time Complexity: O(n)
Space Complexity: O(n) (due to recursion stack)
"""

class Solution:
    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case
        if not head or not head.next:
            return head

        # Recursively reverse the rest
        new_head = self.reverseList_recursive(head.next)

        # Fix current connection
        front = head.next
        front.next = head
        head.next = None

        return new_head


"""
Dry Run Example:
--------------------
Input: 1 -> 2 -> 3

reverseList(1)
    → reverseList(2)
        → reverseList(3)
            returns 3
        Fix 3->2
    Fix 2->1
Return 3

Output: 3 -> 2 -> 1
------------------------------------------------------------
"""


"""
------------------------------------------------------------
Summary:
------------------------------------------------------------
Approach       | Time   | Space | Difficulty | Best For
------------------------------------------------------------
Brute Force    | O(n)   | O(n)  | Easy       | Learning concept
Iterative      | O(n)   | O(1)  | Medium     | Production code
Recursive      | O(n)   | O(n)  | Medium     | Interviews / Recursion
------------------------------------------------------------

Recommended Approach:
Use the **iterative** solution for efficiency.
Understand the **recursive** one for interviews.
The **stack** method is helpful to understand conceptually.
------------------------------------------------------------
"""


# ---------------------------
# Example Test Code
# ---------------------------
def create_linked_list(values):
    if not values: return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    sol = Solution()

    head = create_linked_list([1, 2, 3, 4, 5])
    print("Brute Force:", print_linked_list(sol.reverseList_stack(head)))

    head = create_linked_list([1, 2, 3, 4, 5])
    print("Iterative:", print_linked_list(sol.reverseList_iterative(head)))

    head = create_linked_list([1, 2, 3, 4, 5])
    print("Recursive:", print_linked_list(sol.reverseList_recursive(head)))

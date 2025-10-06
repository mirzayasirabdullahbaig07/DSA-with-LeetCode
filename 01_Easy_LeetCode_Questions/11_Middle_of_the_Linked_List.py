"""
LeetCode 876: Middle of the Linked List
---------------------------------------

Problem:
------------
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Problem Link:
https://leetcode.com/problems/middle-of-the-linked-list/

Example 1:
-------------
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
-------------
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, 
we return the second one.

Constraints:
---------------
- The number of nodes in the list is in the range [1, 100].
- 1 <= Node.val <= 100

------------------------------------------------------------
Brute Force Solution (Count then Traverse)
------------------------------------------------------------
Intuition:
-------------
To find the middle, we need to know how many nodes there are.
Since we cannot access elements by index in a linked list, we must first traverse it.

Approach:
------------
1. Traverse the list once to count the number of nodes (`n`).
2. Compute the middle index as `n // 2`.
3. Traverse again from head to the middle index.
4. Return that node.

Works for both odd and even lengths:
- Odd: middle = n//2 (e.g., 5 → index 2)
- Even: middle = n//2 (e.g., 6 → index 3 → second middle)

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode_bruteforce(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        temp = head

        # First pass: Count total nodes
        while temp:
            n += 1
            temp = temp.next

        temp = head
        # Second pass: Move to middle position
        for i in range(n // 2):
            temp = temp.next

        return temp


"""
------------------------------------------------------------
Dry Run Example:
------------------------------------------------------------
Input: head = [1,2,3,4,5]

Step 1: Counting nodes
----------------------
temp = 1 → n=1
temp = 2 → n=2
temp = 3 → n=3
temp = 4 → n=4
temp = 5 → n=5

Step 2: Finding middle
----------------------
n // 2 = 2 → move 2 steps from head
Move 1: temp = 2
Move 2: temp = 3

Middle Node = 3
Output: [3,4,5]
------------------------------------------------------------


------------------------------------------------------------
Optimal Solution (Two-Pointer / Fast and Slow)
------------------------------------------------------------
Intuition:
-------------
Use two pointers moving at different speeds.
- Slow pointer → moves 1 step each time
- Fast pointer → moves 2 steps each time

When fast reaches the end, slow will be at the middle.

Why does this work?
If the list length = n,
- Slow travels n/2 steps
- Fast travels n steps (2x speed)
Thus, when fast is done, slow is halfway.

Handles both odd & even lengths:
- Odd: fast stops at last node
- Even: fast passes the end → slow is second middle

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        # Move fast by 2 steps and slow by 1 step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # When fast reaches end, slow is at middle
        return slow


"""
------------------------------------------------------------
Dry Run Example:
------------------------------------------------------------
Input: head = [1,2,3,4,5,6]

Initial: slow = 1, fast = 1

Iteration 1:
    slow = 2
    fast = 3

Iteration 2:
    slow = 3
    fast = 5

Iteration 3:
    slow = 4
    fast = None (reached end)

Middle Node = 4
Output: [4,5,6]
------------------------------------------------------------


------------------------------------------------------------
Final Notes:
------------------------------------------------------------
Brute Force:
- Simple & clear.
- Two passes through the list.

Optimal (Two Pointers):
- One-pass solution.
- Elegant & efficient.
- Most preferred in interviews.

Key Takeaway:
--------------
The two-pointer (slow-fast) technique is one of the most powerful 
patterns in linked list problems. Mastering it will help you 
solve problems like:
- Detect cycle
- Find start of cycle
- Remove nth node from end
- Reorder linked list
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
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

# Test Examples
if __name__ == "__main__":
    sol = Solution()
    head = create_linked_list([1,2,3,4,5])
    print("Brute Force:", print_linked_list(sol.middleNode_bruteforce(head)))  # [3,4,5]
    
    head = create_linked_list([1,2,3,4,5,6])
    print("Two Pointers:", print_linked_list(sol.middleNode(head)))            # [4,5,6]

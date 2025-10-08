"""
Problem: Remove Nth Node from End of List
-----------------------------------------
Given the head of a linked list, remove the nth node from the end of the list
and return its head.

-----------------------------------------
Example 1:
Input:  head = [1, 2, 3, 4, 5], n = 2
Output: [1, 2, 3, 5]

Example 2:
Input:  head = [1], n = 1
Output: []

Example 3:
Input:  head = [1, 2], n = 1
Output: [1]

-----------------------------------------
Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

Follow-up:
Could you solve this problem in one pass?
"""

# -------------------------------------------------------------------
# Definition for singly-linked list
# -------------------------------------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# -------------------------------------------------------------------
# ✅ Solution 1: Brute Force Approach (Two Pass)
# -------------------------------------------------------------------
class SolutionTwoPass:
    """
    Intuition:
    -----------
    Think of counting people standing in a queue.
    If you want to remove the 3rd person from the end, you first count all,
    then remove the person at (total - n)th position from the start.

    Algorithm Steps:
    ----------------
    1️⃣ Traverse the list to count its total length.
    2️⃣ If n == length, remove the head node directly.
    3️⃣ Find (length - n)th node from the start → node before the target.
    4️⃣ Change its next pointer to skip the nth node from the end.
    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None

        # 1️⃣ First pass – Count total nodes
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # 2️⃣ Edge case: remove the head node
        if n == length:
            new_head = head.next
            head = None
            return new_head

        # 3️⃣ Find node before the target
        curr = head
        pos = 1
        stop_pos = length - n
        while pos < stop_pos:
            curr = curr.next
            pos += 1

        # 4️⃣ Skip the nth node from end
        curr.next = curr.next.next
        return head


# -------------------------------------------------------------------
# ✅ Solution 2: Optimal Approach (One Pass – Two Pointers)
# -------------------------------------------------------------------
class SolutionOnePass:
    """
    Intuition:
    -----------
    Imagine two people walking in a line. The first person (fast pointer)
    starts walking n steps ahead of the second (slow pointer).
    When the fast pointer reaches the end, the slow pointer will be exactly
    one step before the node to remove.

    Algorithm Steps:
    ----------------
    1️⃣ Initialize two pointers: fastp and slowp at the head.
    2️⃣ Move fastp n steps ahead to create the gap.
    3️⃣ If fastp becomes None → removing the head.
    4️⃣ Move both pointers together until fastp reaches the last node.
    5️⃣ Remove the nth node by skipping slowp.next.
    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fastp = head
        slowp = head

        # 1️⃣ Move fast pointer n steps ahead
        for _ in range(n):
            fastp = fastp.next

        # 2️⃣ Edge case – remove head
        if not fastp:
            return head.next

        # 3️⃣ Move both pointers until fast reaches the end
        while fastp.next:
            fastp = fastp.next
            slowp = slowp.next

        # 4️⃣ Remove nth node from end
        slowp.next = slowp.next.next
        return head


# -------------------------------------------------------------------
# 🧩 Dry Run Example
# -------------------------------------------------------------------
"""
Example: head = [1, 2, 3, 4, 5], n = 2

Step 1️⃣ Initialize
    fastp = 1, slowp = 1

Step 2️⃣ Move fastp n=2 steps ahead
    → Step 1: fastp = 2
    → Step 2: fastp = 3
    Now fastp is 2 steps ahead of slowp.

Step 3️⃣ Move both together
    → fastp = 4, slowp = 2
    → fastp = 5, slowp = 3
    fastp.next = None → stop.

Step 4️⃣ Remove node after slowp (4)
    slowp.next = slowp.next.next (skip 4)

✅ Final Linked List: [1, 2, 3, 5]
"""


# -------------------------------------------------------------------
# ⏱️ Time and Space Complexity Analysis
# -------------------------------------------------------------------
"""
Brute Force (Two Pass)
----------------------
Time Complexity:  O(2n) ≈ O(n)
    → One traversal to find length + One to remove node
Space Complexity: O(1)
    → Only a few pointers used

Optimal (One Pass – Two Pointers)
---------------------------------
Time Complexity:  O(n)
    → Single traversal through the list
Space Complexity: O(1)
    → No extra data structure used

-------------------------------------------------
Approach Comparison:
-------------------------------------------------
| Approach          | Time | Space | Passes | Difficulty | Notes                     |
|--------------------|------|--------|--------|-------------|---------------------------|
| Two Pass (Brute)   | O(n) | O(1)  |   2    | Easy        | Simple & clear logic      |
| One Pass (Optimal) | O(n) | O(1)  |   1    | Medium      | Efficient & interview-safe|
-------------------------------------------------
"""


# -------------------------------------------------------------------
# 🔍 Example Usage (For Local Testing)
# -------------------------------------------------------------------
if __name__ == "__main__":
    # Example: [1,2,3,4,5], n = 2 → [1,2,3,5]
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    sol = SolutionOnePass()
    new_head = sol.removeNthFromEnd(n1, 2)

    # Print Result
    curr = new_head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")  # ✅ Output: 1 -> 2 -> 3 -> 5 -> None

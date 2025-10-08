"""
Problem: Delete the Middle Node of a Linked List
-----------------------------------------------
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size `n` is the ⌊n / 2⌋th node 
from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer 
less than or equal to x.

-----------------------------------------------
Example 1:
Input:  head = [1, 3, 4, 7, 1, 2, 6]
Output: [1, 3, 4, 1, 2, 6]
Explanation:
n = 7, so ⌊7/2⌋ = 3 → delete node index 3 (value = 7).

-----------------------------------------------
Example 2:
Input:  head = [1, 2, 3, 4]
Output: [1, 2, 4]
Explanation:
n = 4, so ⌊4/2⌋ = 2 → delete node index 2 (value = 3).

-----------------------------------------------
Example 3:
Input:  head = [2, 1]
Output: [2]
Explanation:
n = 2, so ⌊2/2⌋ = 1 → delete node index 1 (value = 1).

-----------------------------------------------
Constraints:
- The number of nodes in the list is in range [1, 10^5].
- 1 <= Node.val <= 10^5
"""

# -------------------------------------------------------------------
# Definition for singly-linked list.
# -------------------------------------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# -------------------------------------------------------------------
# ✅ Optimal Solution using Modified Tortoise and Hare Algorithm
# -------------------------------------------------------------------
class Solution:
    """
    Intuition:
    ----------
    Imagine two friends running on a track:
    - Fast moves 2 steps at a time 🏃‍♂️💨
    - Slow moves 1 step at a time 🐢
    
    When the fast runner reaches the end, 
    the slow runner will be at the **middle** of the list.

    But our goal is to *delete* the middle node.
    So, we want the slow pointer to stop **just before** the middle node.
    That way, we can remove the middle node by:
        slow.next = slow.next.next

    ------------------------------------
    Algorithm Steps:
    ------------------------------------
    1. Handle Edge Case → if the list has only 1 node, return None.
    2. Initialize two pointers:
        - slow = head (tortoise)
        - fast = head.next.next (hare with a head start)
    3. Traverse the list:
        - Move slow by 1 step
        - Move fast by 2 steps
        - Continue until fast reaches the end
    4. When fast stops, slow will be *just before the middle node*.
    5. Delete middle by:
        slow.next = slow.next.next
    6. Return modified head.
    """

    def deleteMiddle(self, head: ListNode) -> ListNode:
        # Edge Case: If there's only one node, delete it and return None
        if not head.next:
            return None

        # Initialize slow and fast pointers
        slow = head
        fast = head.next.next  # Fast starts two steps ahead

        # Traverse the list until fast reaches the end
        while fast and fast.next:
            slow = slow.next        # Move slow by 1 step
            fast = fast.next.next   # Move fast by 2 steps

        # Delete the middle node
        slow.next = slow.next.next

        # Return modified list head
        return head


# -------------------------------------------------------------------
# 🧩 Dry Run Example
# -------------------------------------------------------------------
"""
Input: head = [1, 2, 3, 4, 5]

Initial State:
--------------
slow = 1
fast = 3 (head.next.next)
List: 1 -> 2 -> 3 -> 4 -> 5

Iteration 1:
-------------
slow moves 1 step → slow = 2
fast moves 2 steps → fast = 5
Current: slow = 2, fast = 5

Iteration 2:
-------------
fast.next = None → stop loop
slow = 2 → slow is just before middle node (3)

Delete middle:
--------------
slow.next = slow.next.next
→ 2.next = 3.next (which is 4)
List becomes: 1 -> 2 -> 4 -> 5

✅ Final Output: [1, 2, 4, 5]
"""


# -------------------------------------------------------------------
# ⏱️ Time and Space Complexity
# -------------------------------------------------------------------
"""
Time Complexity:
----------------
O(n)
→ We traverse the linked list once with the slow and fast pointers.

Space Complexity:
-----------------
O(1)
→ We use only a few pointer variables (slow, fast), no extra data structures.

-------------------------------------
Comparison with Naive Approach:
-------------------------------------
Approach                 Time     Space   Explanation
-----------------------------------------------------
Count & Delete Middle    O(2n)    O(1)    Needs two passes (count + delete)
Tortoise & Hare (Optimal) O(n)    O(1)    One pass, constant space ✅
-----------------------------------------------------
✅ Preferred: Modified Tortoise & Hare (One Pass)
"""


# -------------------------------------------------------------------
# 🔍 Example Usage (for testing locally)
# -------------------------------------------------------------------
if __name__ == "__main__":
    # Create linked list: 1 -> 2 -> 3 -> 4 -> 5
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    sol = Solution()
    new_head = sol.deleteMiddle(n1)

    # Print result: should be 1 -> 2 -> 4 -> 5
    temp = new_head
    result = []
    while temp:
        result.append(temp.val)
        temp = temp.next
    print("Modified List after deleting middle node:", result)

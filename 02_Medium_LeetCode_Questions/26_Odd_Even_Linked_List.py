"""
Problem: Odd Even Linked List
-----------------------------
Given the head of a singly linked list, group all the nodes with odd indices together 
followed by the nodes with even indices, and return the reordered list.

- The first node is considered odd, the second node even, and so on.
- The relative order inside both the odd and even groups should remain as in the input.

You must solve this problem in:
→ O(1) extra space
→ O(n) time complexity

-----------------------------------
Example 1:
Input:  head = [1, 2, 3, 4, 5]
Output: [1, 3, 5, 2, 4]

Example 2:
Input:  head = [2, 1, 3, 5, 6, 4, 7]
Output: [2, 3, 6, 7, 1, 5, 4]

-----------------------------------
Constraints:
- The number of nodes is in range [0, 10^4].
- Node values are in range [-10^6, 10^6].
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# -------------------------------------------------------------------
# ✅ Optimal Solution using Pointer Manipulation (O(n) time, O(1) space)
# -------------------------------------------------------------------
class Solution:
    """
    Intuition:
    ----------
    Instead of creating new lists or arrays, we can rearrange the links in-place.

    Think of two teams:
    - Team Odd: Nodes at positions 1, 3, 5, ...
    - Team Even: Nodes at positions 2, 4, 6, ...
    
    Each team captain (odd pointer & even pointer) collects their teammates 
    by jumping two steps at a time.

    After collecting everyone, the last odd node connects to the first even node,
    merging both groups together.

    ------------------------------------
    Algorithm Steps:
    ------------------------------------
    1. Handle edge cases → empty list or single node → return head.
    2. Initialize:
        - odd = head
        - even = head.next
        - even_head = even (to connect later)
    3. Traverse:
        - While even and even.next exist:
            - odd.next = odd.next.next
            - even.next = even.next.next
            - Move odd and even one step forward.
    4. Finally, link odd.next = even_head.
    5. Return the modified head.
    """

    def oddEvenList(self, head: ListNode) -> ListNode:
        # Base case: if list is empty or has only one node
        if not head or not head.next:
            return head

        # Initialize pointers
        odd = head               # pointer for odd positions
        even = head.next         # pointer for even positions
        even_head = even         # keep the head of even list

        # Traverse and rearrange nodes
        while even and even.next:
            odd.next = odd.next.next       # link odd to next odd
            even.next = even.next.next     # link even to next even
            odd = odd.next                 # move odd pointer forward
            even = even.next               # move even pointer forward

        # Connect end of odd list to start of even list
        odd.next = even_head

        # Return the modified linked list head
        return head


# -------------------------------------------------------------------
# 🧩 Dry Run Example
# -------------------------------------------------------------------
"""
Input:  head = [1, 2, 3, 4, 5]

Step-by-step:
-------------
Initial state:
odd = 1, even = 2, even_head = 2
List connections: 1 -> 2 -> 3 -> 4 -> 5

Iteration 1:
------------
odd.next = odd.next.next → 1 -> 3
even.next = even.next.next → 2 -> 4
Move odd = 3, even = 4
Current state:
Odd chain: 1 -> 3
Even chain: 2 -> 4

Iteration 2:
------------
odd.next = odd.next.next → 3 -> 5
even.next = even.next.next → 4 -> None
Move odd = 5, even = None
Current state:
Odd chain: 1 -> 3 -> 5
Even chain: 2 -> 4

Final Step:
-----------
odd.next = even_head → 5 -> 2
Final list: 1 -> 3 -> 5 -> 2 -> 4

✅ Output: [1, 3, 5, 2, 4]
"""


# -------------------------------------------------------------------
# ⏱️ Time and Space Complexity
# -------------------------------------------------------------------
"""
Time Complexity:
----------------
O(n) → We traverse the list once. Each node is visited exactly once.

Space Complexity:
-----------------
O(1) → Only a few pointer variables (odd, even, even_head). 
No extra data structure used.

-------------------------------------
Comparing Both Approaches:
-------------------------------------
Approach              Time    Space   Explanation
-------------------------------------------------
Brute Force (Array)   O(n)    O(n)    Needs extra list to store values
Optimal (Pointers)    O(n)    O(1)    In-place rearrangement using links
-------------------------------------------------
✅ Preferred: Optimal (Pointer Manipulation)
"""

# -------------------------------------------------------------------
# 🔍 Example Usage (you can test locally)
# -------------------------------------------------------------------
if __name__ == "__main__":
    # Creating linked list: 1 -> 2 -> 3 -> 4 -> 5
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    sol = Solution()
    new_head = sol.oddEvenList(n1)

    # Print result: should be 1 -> 3 -> 5 -> 2 -> 4
    temp = new_head
    result = []
    while temp:
        result.append(temp.val)
        temp = temp.next
    print("Reordered List:", result)

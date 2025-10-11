"""
🧠 Problem:
Given the heads of two singly linked lists, headA and headB,
return the node at which the two lists intersect.
If the two linked lists have no intersection, return None.

Example:
List A: 4 -> 1 -> 8 -> 4 -> 5
List B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
Output: Node with value 8 (intersection)

Constraints:
- Lists retain original structure
- No cycles exist
- 1 <= len(listA), len(listB) <= 3*10^4

--------------------------------------------
💡 Intuition (Two-Pointer Technique)
--------------------------------------------
Imagine two friends walking on separate paths. 
- When one reaches the end of their path, they switch to the other path.
- If the paths intersect, they will meet at the intersection node.
- If not, both will eventually reach the end (None) at the same time.

This ensures both pointers traverse exactly the same total distance:
lengthA + lengthB

--------------------------------------------
⚙️ Algorithm Steps
--------------------------------------------
1️⃣ Edge Case Check:
    - If either headA or headB is None → no intersection → return None

2️⃣ Initialize Pointers:
    - pointer1 = headA
    - pointer2 = headB

3️⃣ Traverse Lists:
    - While pointer1 != pointer2:
        - Move pointer1 to next node, if None switch to headB
        - Move pointer2 to next node, if None switch to headA
    - Loop ends when pointers meet at intersection or both become None

4️⃣ Return:
    - Return pointer1 (intersection node or None)

--------------------------------------------
⚙️ Code Implementation
--------------------------------------------
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        if not headA or not headB:
            return None  # If either list is empty, intersection impossible

        pointer1, pointer2 = headA, headB  # Initialize two pointers

        # Traverse both lists
        while pointer1 != pointer2:
            # Move to next node or switch to the other list's head
            pointer1 = pointer1.next if pointer1 else headB
            pointer2 = pointer2.next if pointer2 else headA

        return pointer1  # Intersection node or None

"""
--------------------------------------------
🧩 Dry Run Example
--------------------------------------------
List A: 4 -> 1 -> 8 -> 4 -> 5
List B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
Intersection at node with value 8

Step | pointer1 | pointer2 | Action
-----|----------|----------|--------
 1   | 4        | 5        | Not same → move next
 2   | 1        | 6        | Not same → move next
 3   | 8        | 1        | Not same → move next
 4   | 4        | 8        | Not same → move next
 5   | 5        | 4        | Not same → move next
 6   | None     | 5        | pointer1 switches to headB
 7   | 5        | None     | pointer2 switches to headA
 8   | 6        | 4        | Not same → move next
 9   | 1        | 1        | Not same → move next
10   | 8        | 8        | ✅ Same → intersection found, return node 8

Result: Node with value 8

--------------------------------------------
⏱️ Time Complexity Analysis
--------------------------------------------
- Each pointer traverses at most both lists once
- Total steps ≤ lengthA + lengthB
✅ Time Complexity: O(m + n), where m = len(listA), n = len(listB)

--------------------------------------------
💾 Space Complexity Analysis
--------------------------------------------
- Only two pointers are used
✅ Space Complexity: O(1) (constant space)

--------------------------------------------
💡 Why It Works
--------------------------------------------
- By switching lists when a pointer reaches the end, both pointers travel the same total distance.
- If there is an intersection, they meet at the node.
- If there is no intersection, both become None simultaneously.

--------------------------------------------
🧱 Edge Cases
--------------------------------------------
1️⃣ One list is empty → return None
2️⃣ Lists do not intersect → return None
3️⃣ Intersection is at the head → return headA or headB
4️⃣ Intersection is at the last node → works fine

--------------------------------------------
✅ Summary
--------------------------------------------
Approach:      Two-Pointer Technique
Time Complexity: O(m + n)
Space Complexity: O(1)
Best For:       Production code, optimal for any linked list intersection problem
--------------------------------------------
"""

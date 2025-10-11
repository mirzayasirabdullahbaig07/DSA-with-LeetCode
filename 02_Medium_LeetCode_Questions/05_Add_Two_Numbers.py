# 🧠 Problem:
# Given two non-empty linked lists representing two non-negative integers,
# digits stored in reverse order. Add the numbers and return the sum as a linked list.
#
# Example:
# l1 = [2,4,3], l2 = [5,6,4] → Output: [7,0,8] (342 + 465 = 807)
# l1 = [0], l2 = [0] → Output: [0]
# l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] → Output: [8,9,9,9,0,0,0,1]

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        --------------------------------------------
        💡 Intuition (Digit-by-Digit Addition)
        --------------------------------------------
        - Think of adding two numbers manually from right to left.
        - Since linked lists store digits in reverse order, we can add corresponding digits directly.
        - Track carry from previous addition.
        - Build result list as we go using a dummy node.

        --------------------------------------------
        ⚙️ Algorithm Steps
        --------------------------------------------
        1️⃣ Create dummy node to simplify result list construction
        2️⃣ Initialize temp pointer to dummy node
        3️⃣ Initialize carry = 0
        4️⃣ Traverse lists while l1, l2, or carry exists:
            a. total = carry
            b. If l1 exists, add l1.val to total and move l1 forward
            c. If l2 exists, add l2.val to total and move l2 forward
            d. carry = total // 10
            e. Create new node with total % 10 and attach to temp.next
            f. Move temp to temp.next
        5️⃣ Return result.next (skip dummy node)

        --------------------------------------------
        ⏱️ Time Complexity
        --------------------------------------------
        - O(max(m, n)), m = length of l1, n = length of l2
        - Each node is processed exactly once.

        --------------------------------------------
        💾 Space Complexity
        --------------------------------------------
        - O(max(m, n)) for result linked list
        - No extra space used apart from output nodes

        --------------------------------------------
        🧩 Dry Run Example
        --------------------------------------------
        l1 = [2,4,3] (represents 342)
        l2 = [5,6,4] (represents 465)
        
        Step | l1.val | l2.val | carry | total | Result Node | Action
        -----|--------|--------|-------|-------|-------------|--------
        1    | 2      | 5      | 0     | 7     | 7           | move l1, l2
        2    | 4      | 6      | 0     | 10    | 0           | carry=1, move l1, l2
        3    | 3      | 4      | 1     | 8     | 8           | carry=0, move l1, l2
        End  | None   | None   | 0     | -     | -           | Done

        Final Result: [7,0,8] → 807

        --------------------------------------------
        💡 Why It Works
        --------------------------------------------
        - Dummy node simplifies list construction; no need to handle first node separately
        - Using carry allows proper addition beyond 9
        - Loop continues until all digits and carry are processed
        - Modulo gives current digit, integer division gives carry

        --------------------------------------------
        🧱 Edge Cases
        --------------------------------------------
        1️⃣ Different length lists → works fine
        2️⃣ One list empty → returns other list
        3️⃣ Carry at last digit → extra node created
        4️⃣ All zeros → handled correctly

        --------------------------------------------
        ✅ Summary
        --------------------------------------------
        Approach:      Digit-by-Digit Addition
        Time Complexity: O(max(m, n))
        Space Complexity: O(max(m, n))
        Best For:       Production code, simple and efficient for adding linked list numbers
        --------------------------------------------
        """

        result = ListNode(0)      # Dummy head node
        temp = result             # Pointer to build result list
        carry = 0                 # To store carry from addition

        # Traverse both lists and handle carry
        while l1 or l2 or carry:
            total = carry         # Start with carry

            if l1:
                total += l1.val   # Add digit from l1
                l1 = l1.next

            if l2:
                total += l2.val   # Add digit from l2
                l2 = l2.next

            carry = total // 10    # Calculate carry for next iteration
            temp.next = ListNode(total % 10)  # Create node for current digit
            temp = temp.next       # Move result pointer

        return result.next         # Skip dummy node and return actual result

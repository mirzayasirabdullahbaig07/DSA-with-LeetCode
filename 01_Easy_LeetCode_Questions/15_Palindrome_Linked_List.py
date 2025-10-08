"""
Problem: Palindrome Linked List
--------------------------------
Given the head of a singly linked list, return True if it is a palindrome, 
or False otherwise.

A palindrome is a sequence that reads the same backward as forward.

--------------------------------
Example 1:
Input: head = [1, 2, 2, 1]
Output: True

Example 2:
Input: head = [1, 2]
Output: False

--------------------------------
Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 0 <= Node.val <= 9

Follow up:
Could you do it in O(n) time and O(1) space?
"""

# -------------------------------------------------------------------
# Definition for singly-linked list
# -------------------------------------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# -------------------------------------------------------------------
# ✅ Solution 1: Brute Force (Using Stack)
# -------------------------------------------------------------------
class SolutionStack:
    """
    Intuition:
    -----------
    Think of this like reading a string forward and backward.
    If both are the same → palindrome ✅

    Idea:
    -----
    1. Traverse the linked list once and store all node values in a stack.
    2. Traverse again and compare each node value with the popped stack value.
       Since stack pops elements in reverse order (LIFO),
       it effectively gives the reversed sequence.
    3. If all match → return True, else False.
    """

    def isPalindrome(self, head: ListNode) -> bool:
        temp = head
        stack = []

        # 1️⃣ Store all values in stack
        while temp:
            stack.append(temp.val)
            temp = temp.next

        # 2️⃣ Reset temp to head to start comparison
        temp = head

        # 3️⃣ Compare with reversed values using stack
        while temp:
            if temp.val != stack.pop():
                return False
            temp = temp.next

        return True


# -------------------------------------------------------------------
# ✅ Solution 2: Optimal Approach (Two Pointers + Reverse)
# -------------------------------------------------------------------
class SolutionOptimal:
    """
    Intuition:
    -----------
    To achieve O(1) space, we avoid using any extra list or stack.
    We do it in-place using two main techniques:
    - Tortoise and Hare (two pointers)
    - Reversing the second half of the list

    Algorithm Steps:
    ----------------
    1️⃣ Find the middle node using two pointers (slow & fast)
        - slow moves 1 step, fast moves 2 steps
        - when fast reaches end, slow is at middle
    2️⃣ Reverse the second half of the list.
    3️⃣ Compare first half and reversed second half node by node.
    4️⃣ If all values match → it's a palindrome.
    5️⃣ (Optional) Reverse back the second half to restore list.
    """

    # Helper function to reverse a linked list
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def isPalindrome(self, head: ListNode) -> bool:
        # Edge case: 0 or 1 node is always a palindrome
        if not head or not head.next:
            return True

        # 1️⃣ Find the middle node
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2️⃣ Reverse the second half
        second_half = self.reverseList(slow.next)

        # 3️⃣ Compare both halves
        first_half = head
        temp_second = second_half
        result = True
        while temp_second:
            if first_half.val != temp_second.val:
                result = False
                break
            first_half = first_half.next
            temp_second = temp_second.next

        # 4️⃣ Restore the original list (optional)
        slow.next = self.reverseList(second_half)

        # 5️⃣ Return result
        return result


# -------------------------------------------------------------------
# 🧩 Dry Run Example
# -------------------------------------------------------------------
"""
Example Input: [1, 2, 2, 1]

Step 1️⃣ Find Middle
--------------------
Initial: slow = 1, fast = 1
Move slow → 2, fast → 2 (second one)
Move slow → 2 (second one), fast → None (end)
Middle = slow = second '2'

Step 2️⃣ Reverse Second Half
-----------------------------
Original Second Half: [2 → 1]
After Reverse: [1 → 2]

Step 3️⃣ Compare
----------------
First Half:  1 → 2
Second Half: 1 → 2
Compare → 1==1 ✓ , 2==2 ✓ → All matched ✅

Step 4️⃣ Restore Original (optional)
Reverse second half again → back to [2 → 1]

✅ Final Output: True
"""

# -------------------------------------------------------------------
# ⏱️ Time & Space Complexity
# -------------------------------------------------------------------
"""
Brute Force Approach (Using Stack)
---------------------------------
Time Complexity:  O(n)  → traverse twice (store + compare)
Space Complexity: O(n)  → extra stack to store all node values

Optimal Approach (Two Pointer + Reverse)
----------------------------------------
Time Complexity:  O(n)  → find middle + reverse + compare
Space Complexity: O(1)  → in-place reversal, no extra memory

-------------------------------------------------
Approach Comparison:
-------------------------------------------------
| Approach                | Time  | Space | Notes                     |
|--------------------------|-------|--------|---------------------------|
| Stack (Brute Force)      | O(n) | O(n)  | Simple, easy to implement |
| Two Pointer (Optimal)    | O(n) | O(1)  | Best for interviews ✅    |
-------------------------------------------------
"""


# -------------------------------------------------------------------
# 🔍 Example Usage (For Local Testing)
# -------------------------------------------------------------------
if __name__ == "__main__":
    # Example 1: [1, 2, 2, 1] → True
    n4 = ListNode(1)
    n3 = ListNode(2, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    sol = SolutionOptimal()
    print("Is Palindrome:", sol.isPalindrome(n1))  # ✅ True

    # Example 2: [1, 2] → False
    a2 = ListNode(2)
    a1 = ListNode(1, a2)
    print("Is Palindrome:", sol.isPalindrome(a1))  # ❌ False

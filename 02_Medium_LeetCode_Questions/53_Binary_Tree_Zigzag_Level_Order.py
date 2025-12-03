"""
103. Binary Tree Zigzag Level Order Traversal — Explanation (VS Code Ready)

QUESTION SUMMARY:
-----------------
You are given the root of a binary tree.  
You must return the LEVEL ORDER traversal but in a special way:

Level 0  → left to right  
Level 1  → right to left  
Level 2  → left to right  
Level 3  → right to left  
and so on...

This alternating direction is called a *ZIGZAG* traversal.

EXAMPLE:
--------
Input:  [3,9,20,null,null,15,7]

Level 0: [3]                → left to right  
Level 1: [20, 9]            → right to left  
Level 2: [15, 7]            → left to right  
Output: [[3], [20,9], [15,7]]

WHAT THE ALGORITHM DOES:
------------------------
This algorithm uses a classic Breadth-First Search (BFS) approach:

1. Use a queue to traverse the tree level-by-level.
2. For each level:
   - Create an array `level` of size `level_size`.
   - If direction = left-to-right:
         place node at index `i`
     If direction = right-to-left:
         place node at index `level_size - i - 1`
3. After finishing each level:
   - Append `level` to result
   - Toggle the direction (reverse for next level)

WHY USE A PLACEHOLDER ARRAY?
----------------------------
We pre-create a list of correct size:
    level = [0] * level_size

Then we fill values at correct positions based on direction.
This avoids the need to reverse lists, making the solution efficient.

ALGORITHM TYPE:
---------------
→ BFS (Breadth-First Search)  
→ Uses deque queue  
→ Zigzag direction controlled by a boolean flag

TIME COMPLEXITY:
----------------
O(N)
Each node is processed exactly once.

SPACE COMPLEXITY:
-----------------
O(N)
Queue + output list both may hold up to N elements.

This is the optimal BFS zigzag solution.

"""

from collections import deque
from typing import List, Optional

class Solution:
    def zigzagLevelOrder(self, root: Optional['TreeNode']) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []
        left_to_right = True   # flag to control direction

        while queue:
            level_size = len(queue)
            level = [0] * level_size   # placeholder for zigzag insertion

            for i in range(level_size):
                node = queue.popleft()

                # Position depends on direction
                index = i if left_to_right else (level_size - i - 1)
                level[index] = node.val

                # Push children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)
            left_to_right = not left_to_right   # toggle direction for next level

        return result

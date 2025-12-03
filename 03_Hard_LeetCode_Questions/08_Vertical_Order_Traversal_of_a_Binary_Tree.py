"""
987. Vertical Order Traversal of a Binary Tree
------------------------------------------------

EXPLANATION (in simple words):

We assign coordinates (row, col) to every node:
    - Root is at (0, 0)
    - Left child  => (row + 1, col - 1)
    - Right child => (row + 1, col + 1)

We must group nodes by their "col" value from leftmost to rightmost.

If multiple nodes have:
    - The same column
    - The same row
Then we sort them by their node values.

STEPS:
1. Use BFS traversal so nodes are processed level-by-level.
2. Store each node into a dictionary: col -> list of (row, value)
3. After BFS, sort each column by:
        (row, value)
4. Extract only the values and build the final vertical order list.

TIME COMPLEXITY:
    O(N log N)  – because each column list needs sorting.

SPACE COMPLEXITY:
    O(N) – storing nodes in the dictionary.
"""

from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root):
        if not root:
            return []

        # Dictionary: column_index -> list of (row, value)
        col_table = defaultdict(list)

        # BFS queue: stores (node, row, col)
        queue = deque([(root, 0, 0)])

        while queue:
            node, row, col = queue.popleft()

            # Add current node to the column table
            col_table[col].append((row, node.val))

            # Left child goes to col-1
            if node.left:
                queue.append((node.left, row + 1, col - 1))

            # Right child goes to col+1
            if node.right:
                queue.append((node.right, row + 1, col + 1))

        result = []

        # Process columns in sorted order
        for col in sorted(col_table.keys()):
            # Sort by row first, then by node value
            col_nodes = sorted(col_table[col], key=lambda x: (x[0], x[1]))

            # Append only node values
            result.append([val for row, val in col_nodes])

        return result

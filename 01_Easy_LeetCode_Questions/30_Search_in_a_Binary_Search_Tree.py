"""
700. Search in a Binary Search Tree
-----------------------------------

EXPLANATION (in simple words):

You are given a Binary Search Tree (BST) and an integer value "val".

BST Property:
    - Left subtree contains nodes with smaller values.
    - Right subtree contains nodes with larger values.

Goal:
    Find the node whose value == val and return that node (which includes its entire subtree).

If the value is not found, return None.

How the algorithm works:
1. Start from the root.
2. If root.val == val → return this node.
3. If val < root.val → go to the left child.
4. If val > root.val → go to the right child.
5. If we reach a null node, the value does not exist → return None.

TIME COMPLEXITY:
    Best / Average: O(log N)
    Worst case (skewed tree): O(N)

SPACE COMPLEXITY:
    O(1) – we use iterative traversal (no extra stack).
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: 'TreeNode', val: int) -> 'TreeNode':
        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right

        return None

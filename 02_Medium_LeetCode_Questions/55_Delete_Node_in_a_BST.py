"""
450. Delete Node in a Binary Search Tree
----------------------------------------

EXPLANATION (in simple words):

You are given a BST and a key. The task is to delete the node with that key
while keeping the BST properties intact.

BST Properties:
    - Left subtree contains smaller values
    - Right subtree contains larger values

BST Deletion has 3 cases:

1. Node has no children (leaf node)
    - Simply remove it.

2. Node has one child
    - Replace the node with its child.

3. Node has two children
    - Replace the node with its in-order predecessor (max value in left subtree)
      or in-order successor (min value in right subtree).
    - Here, we attach the right subtree to the rightmost node of the left subtree
      and return the left child as new root for this subtree.

Algorithm (Iterative Search + Helper Deletion):
1. If root is None → return None.
2. Search iteratively for the node with the given key.
3. Once found, call a helper function `deletion(node)` to handle the 3 cases.
4. Return the (possibly updated) root.

TIME COMPLEXITY:
    O(height of tree) – search and deletion both depend on height

SPACE COMPLEXITY:
    O(1) – iterative search, only pointers used
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None

        # If root itself is the node to delete
        if root.val == key:
            return self.deletion(root)

        temp = root

        # Iteratively find the node to delete
        while temp is not None:
            if key < temp.val:
                if temp.left and temp.left.val == key:
                    temp.left = self.deletion(temp.left)
                    break
                else:
                    temp = temp.left
            else:
                if temp.right and temp.right.val == key:
                    temp.right = self.deletion(temp.right)
                    break
                else:
                    temp = temp.right

        return root

    def deletion(self, node: TreeNode) -> TreeNode:
        """Delete the node according to BST deletion rules."""

        # Case 1: No left child
        if node.left is None:
            return node.right

        # Case 2: No right child
        if node.right is None:
            return node.left

        # Case 3: Node has two children
        # Attach right subtree to the rightmost node of the left subtree
        right_child = node.right
        last_right = self.findLastRight(node.left)
        last_right.right = right_child
        return node.left

    def findLastRight(self, node: TreeNode) -> TreeNode:
        """Find rightmost node in a subtree."""
        while node.right:
            node = node.right
        return node

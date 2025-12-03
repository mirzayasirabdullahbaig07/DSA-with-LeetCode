"""
701. Insert into a Binary Search Tree
-------------------------------------

EXPLANATION (in simple words):

You are given a Binary Search Tree (BST) and a value "val" to insert.
BST Property:
    - Left subtree contains nodes with smaller values.
    - Right subtree contains nodes with larger values.

Goal:
    Insert "val" into the BST so that it remains a valid BST.

Algorithm (Iterative Approach):
1. If the tree is empty (root is None), create a new node with "val" and return it as root.
2. Start from the root and traverse the tree:
    a. If val < current node value:
        - Go left
        - If left child is None, insert the new node here.
    b. If val > current node value:
        - Go right
        - If right child is None, insert the new node here.
3. Stop when the node is inserted.
4. Return the original root node.

TIME COMPLEXITY:
    Average: O(log N) – balanced BST
    Worst: O(N) – skewed BST

SPACE COMPLEXITY:
    O(1) – iterative traversal, no extra stack used.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: 'TreeNode', val: int) -> 'TreeNode':
        # If the tree is empty, create a new node as root
        if root is None:
            return TreeNode(val)

        temp = root
        while True:
            # Go to the left subtree
            if val < temp.val:
                if temp.left is None:
                    temp.left = TreeNode(val)
                    break
                temp = temp.left
            # Go to the right subtree
            else:
                if temp.right is None:
                    temp.right = TreeNode(val)
                    break
                temp = temp.right

        # Return the original root node
        return root

"""
236. Lowest Common Ancestor of a Binary Tree
-------------------------------------------

PROBLEM:
Given a binary tree and two nodes p and q, find their lowest common ancestor (LCA).

Definition of LCA:
    The lowest node in the tree that has both p and q as descendants (a node can be a descendant of itself).

TECHNIQUE USED:
    - Recursion
    - Depth-First Search (DFS)
    
ALGORITHM / APPROACH:
1. Base Case:
    - If root is None → return None
    - If root is either p or q → return root (this node could be LCA)

2. Recursive Search:
    - Search left subtree for p and q
    - Search right subtree for p and q

3. Determine LCA:
    - If both left and right recursive calls return non-null → current root is LCA
    - If only one side is non-null → propagate that node upward
    - If both sides are null → return None

WHY IT WORKS:
    - DFS ensures we traverse the entire tree.
    - When p and q are found in separate subtrees of a node → that node is the first common ancestor.

TIME COMPLEXITY:
    - O(N) where N is the number of nodes
    - Each node is visited once

SPACE COMPLEXITY:
    - O(H) due to recursion stack, H = height of the tree
    - Worst case (skewed tree): H = N
    - Best case (balanced tree): H = log N
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base Case: empty node or node is p/q itself
        if not root or root == p or root == q:
            return root
        
        # Recurse on left and right subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If p and q are found in different subtrees → current root is LCA
        if left and right:
            return root
        
        # Otherwise propagate non-null result
        return left if left else right

"""
98. Validate Binary Search Tree
-------------------------------

TECHNIQUE USED:
    - Recursion
    - Depth-First Search (DFS)

ALGORITHM / APPROACH:
    1. This problem uses a recursive approach to traverse the tree.
    2. For each node, we maintain a valid range (min, max) for its value.
        - Root node has initial range (-infinity, +infinity)
        - For left child: max becomes current node's value
        - For right child: min becomes current node's value
    3. At each node:
        - If node is None → return True (base case)
        - If node.val is outside the range → return False
    4. Recursively check left and right subtrees with updated ranges.
    5. If all nodes satisfy the BST property → return True

WHY IT WORKS:
    - BST property: left < node < right
    - By maintaining limits for every subtree, we ensure all nodes
      satisfy BST constraints, even beyond immediate parent comparison.

TIME COMPLEXITY:
    - O(N) where N = number of nodes
    - Each node is visited exactly once.

SPACE COMPLEXITY:
    - O(H) where H = height of the tree (recursion stack)
    - In worst case (skewed tree), H = N
    - In best case (balanced tree), H = log N
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def solve(self, node, limit):
        """
        Helper function to validate BST using recursion.

        node: current TreeNode
        limit: [min_val, max_val] valid range for node.val
        """
        if node is None:
            return True

        # Check current node's value within allowed limits
        if not (limit[0] < node.val < limit[1]):
            return False

        # Check left subtree: max limit becomes current node
        left = self.solve(node.left, [limit[0], node.val])
        if left == False:
            return False

        # Check right subtree: min limit becomes current node
        right = self.solve(node.right, [node.val, limit[1]])

        return left and right

    def isValidBST(self, root: 'TreeNode') -> bool:
        """
        Main function to validate BST.

        Starts with the entire range (-infinity, +infinity)
        """
        return self.solve(root, [float("-inf"), float("inf")])

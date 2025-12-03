"""
101. Symmetric Tree — Explanation (for VS Code)

QUESTION SUMMARY:
-----------------
You are given the root of a binary tree. You must check whether the tree
is symmetric around its center. In simpler words:
A tree is symmetric if its left subtree is a mirror image of its right subtree.

EXAMPLE:
--------
Input:  [1,2,2,3,4,4,3]
Output: True  
Because the left subtree and right subtree are perfect mirror images.

Input:  [1,2,2,null,3,null,3]
Output: False  
Because the structure and/or values do not mirror each other.

WHAT THE ALGORITHM DOES:
------------------------
The solution uses a helper function `isMirror(t1, t2)` which compares two nodes
to check whether their subtrees are mirror images of each other.

MIRROR CONDITION:
-----------------
Two trees are mirrors if:
1. Their root values are equal.
2. The left subtree of the first tree is a mirror of the right subtree of the second tree.
3. The right subtree of the first tree is a mirror of the left subtree of the second tree.

This gives the recursive relation:
    isMirror(t1, t2) =
        (t1.val == t2.val) AND
        isMirror(t1.left, t2.right) AND
        isMirror(t1.right, t2.left)

ALGORITHM TYPE:
---------------
→ Depth-First Search (DFS)
→ Uses recursion to compare corresponding nodes
→ Classic Tree Recursion / Divide & Conquer

TIME COMPLEXITY:
----------------
O(N)
Where N = number of nodes in the tree.
Explanation:
Every node is visited once when comparing left-right and right-left.

SPACE COMPLEXITY:
-----------------
O(H)
Where H = height of the tree.
This is due to recursion call stack.

If the tree is skewed → worst case O(N)
If the tree is balanced → O(log N)

The algorithm is optimal.

"""

class Solution:
    def isMirror(self, t1, t2):
        # If both nodes are None, it's symmetric at this level
        if t1 is None and t2 is None:
            return True
        
        # If only one of them is None, not symmetric
        if t1 is None or t2 is None:
            return False
        
        # Check:
        # 1. Values must be equal
        # 2. Left of t1 matches Right of t2
        # 3. Right of t1 matches Left of t2
        return (
            t1.val == t2.val and
            self.isMirror(t1.left, t2.right) and
            self.isMirror(t1.right, t2.left)
        )

    def isSymmetric(self, root):
        # A tree is symmetric if the left and right subtrees mirror each other
        return self.isMirror(root.left, root.right)

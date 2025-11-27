"""
100. Same Tree — FULL EXPLANATION (String Comment Format)

---------------------------------------------------------
PROBLEM SUMMARY:
You are given the roots of two binary trees p and q.
You must return True if both trees are:

1. Structurally identical
2. Node values are equal at every corresponding position

If either the structure differs OR any value differs → return False.

---------------------------------------------------------
CORE IDEA:
We compare the two trees using recursion.

At each pair of nodes (p, q):

1) If BOTH nodes are NULL → identical here.
      return True

2) If ONE node is NULL and the other is NOT → not same.
      return False

3) If values differ (p.val != q.val) → not same.
      return False

4) Otherwise:
      nodes match → we check:
         - left subtree
         - right subtree
      return (leftSame AND rightSame)

---------------------------------------------------------
ALGORITHM (recursive):
function isSameTree(p, q):

    if p is None AND q is None:
        return True

    if one is None OR values differ:
        return False

    # both nodes valid and equal
    return isSameTree(p.left, q.left)
           AND
           isSameTree(p.right, q.right)

---------------------------------------------------------
WHY THIS WORKS:
The comparison is depth-first.
The moment any mismatch appears:
      → return False immediately.

If no mismatches occur:
      → return True.

We ensure structure + values both match.

---------------------------------------------------------
DRY RUN — EXAMPLE 1:
Input:
    p = [1,2,3]
    q = [1,2,3]

Trees:
       1                  1
      / \                / \
     2   3              2   3

Steps:
- Compare 1 and 1 → OK
- Compare 2 and 2 → OK
    - left NULL vs NULL → OK
    - right NULL vs NULL → OK
- Compare 3 and 3 → OK
    - left NULL vs NULL → OK
    - right NULL vs NULL → OK

Everything matches → True.

---------------------------------------------------------
DRY RUN — EXAMPLE 2:
Input:
    p = [1,2]
    q = [1,null,2]

Trees:
   p:          q:
     1          1
    /            \
   2              2

Steps:
- Compare 1 and 1 → OK
- Compare p.left=2 vs q.left=NULL → mismatch → False

Output → False

---------------------------------------------------------
DRY RUN — EXAMPLE 3:
Input:
    p = [1,2,1]
    q = [1,1,2]

Trees:
      p:              q:
        1               1
       / \             / \
      2   1           1   2

Steps:
- Compare 1 and 1 → OK
- Compare 2 vs 1 → mismatch → False

Output → False

---------------------------------------------------------
TIME & SPACE COMPLEXITY:

Time Complexity: O(N)
We compare each node once.

Space Complexity: O(H)
H = tree height (recursive depth)
Worst case (skewed tree): O(N)
Best case (balanced tree): O(log N)

---------------------------------------------------------
FINAL SUMMARY:
✔ Both NULL → True  
✘ One NULL → False  
✘ Values differ → False  
✔ Otherwise → check left + right subtrees  
✔ Ideal recursive tree comparison technique  

---------------------------------------------------------
CODE USED FOR EXPLANATION:

# Definition for a binary tree node.
"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # If both nodes are None — trees are identical here
        if not p and not q:
            return True
        
        # If one is None OR values differ — trees aren't the same
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check left subtree AND right subtree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



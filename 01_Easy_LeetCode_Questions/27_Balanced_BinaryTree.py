"""
110. Balanced Binary Tree — Full Explanation (String Comment Format)

---------------------------------------------------------
PROBLEM SUMMARY:
You are given the root of a binary tree. You must determine whether 
the tree is height-balanced.

A binary tree is "height-balanced" if for every node:
    | height(left subtree) – height(right subtree) | ≤ 1

This must be true for ALL nodes in the tree.

---------------------------------------------------------
KEY IDEA:
For each node:
- Calculate height of left subtree.
- Calculate height of right subtree.
- If the difference > 1 → tree is NOT balanced.
- If any subtree is unbalanced, we should immediately STOP and
  return a special signal (-1).

We use "-1" as a signal that a subtree is unbalanced.


---------------------------------------------------------
WHY WE RETURN -1?
Instead of computing full height and then checking, we stop early.

Example:
If a subtree is already unbalanced, we don’t need to check anything else.
We simply bubble up "-1", and the whole tree becomes unbalanced.

This makes the algorithm efficient.

---------------------------------------------------------
ALGORITHM DETAILS (solve function):
solve(node) returns:
    - height of subtree if subtree is balanced
    - -1 if subtree is UNBALANCED

Steps:
1. If node is None → return height = 0
2. Recursively compute left subtree height
3. If left subtree returned -1 → propagate -1 upward
4. Recursively compute right subtree height
5. If right subtree returned -1 → propagate -1 upward
6. If abs(leftHeight - rightHeight) > 1 → return -1
7. Otherwise return height = 1 + max(leftHeight, rightHeight)

Finally:
Tree is balanced if solve(root) != -1

---------------------------------------------------------
DRY RUN THROUGH CODE:
"""
class Solution:
    def isBalanced(self, root):
        
        def solve(node):
            if not node:
                return 0

            left = solve(node.left)
            if left == -1:
                return -1

            right = solve(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return solve(root) != -1
"""
---------------------------------------------------------
EXAMPLE 1:
Input:
    [3,9,20,null,null,15,7]

Tree structure:
        3
      /   \
     9    20
         /  \
        15   7

Heights:
- Node 9: height = 1
- Node 15: height = 1
- Node 7: height = 1
- Node 20: height = 1 + max(1,1) = 2
- Root 3: height = 1 + max(1,2) = 3

Balance checks:
- abs(1 - 1) = 0 ✓
- abs(1 - 1) = 0 ✓
- abs(1 - 1) = 0 ✓
- abs(1 - 2) = 1 ✓

Everything valid → true

Output: true

---------------------------------------------------------
EXAMPLE 2:
Input:
    [1,2,2,3,3,null,null,4,4]

Tree:
          1
        /   \
       2     2
      / \
     3   3
    / \
   4   4

Heights (bottom-up):
- Node 4 left = 1
- Node 4 right = 1
- Node 3 height = 2

Now:
Left subtree of main 2 has height = 2
Right subtree of main 2 has height = 0

Check:
abs(2 - 0) = 2 → NOT balanced

solve returns -1 immediately.

Output: false

---------------------------------------------------------
EXAMPLE 3:
Input:
    []

Empty tree:
By definition, it is balanced.
solve(root) returns 0
Final result → true

Output: true

---------------------------------------------------------
TIME & SPACE COMPLEXITY:

Time Complexity: O(N)
Each node is visited once.

Space Complexity: O(H)
H = height of tree due to recursion stack.

Worst case: O(N) for skewed tree
Best case (balanced): O(log N)

---------------------------------------------------------
FINAL SUMMARY:
We recursively compute heights and check balance simultaneously.
Using -1 as a signal allows EARLY stopping when an imbalance is found.
This is the optimal way to solve Balanced Binary Tree.
"""

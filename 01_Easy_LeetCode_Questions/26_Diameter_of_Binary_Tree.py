"""
543. Diameter of Binary Tree — Full Explanation (String Comment Format)

---------------------------------------------------------
PROBLEM SUMMARY:
You are given the root of a binary tree. The task is to return the
diameter of the tree.

The diameter is defined as the length (number of edges) of the
longest path between any two nodes in the entire tree. The path may
or may not pass through the root.

---------------------------------------------------------
KEY OBSERVATION:
The longest path in a binary tree always has the form:

    left subtree height + right subtree height

at some node.

This is because:
- The longest path must go DOWNWARD.
- The only place a path can branch is at a node.
So, if a node is in the middle of the longest path, the left side of
the path is the height of its left subtree, and the right side is the
height of its right subtree.

Therefore:
diameter passing through a node = leftHeight + rightHeight

Our job is to compute this for EVERY node and keep the maximum.

---------------------------------------------------------
HOW WE SOLVE IT:
We perform a DFS that returns the height of each subtree.

The function returns:
height(node) = 1 + max(height of left, height of right)

While returning height upward, we simultaneously calculate the diameter:
self.diameter = max(self.diameter, leftHeight + rightHeight)

This ensures we check every possible path in the tree.

---------------------------------------------------------
WHY HEIGHT + HEIGHT?
Because the path is measured in EDGES.
Example:

       A
      / \
     B   C
    / \
   D   E

If A is the center:
- longest path down the left is edges from A → B → D (height 2)
- longest path down the right is A → C (height 1)

So total = 2 + 1 = 3 edges = diameter through A.

---------------------------------------------------------
DRY RUN OF THE GIVEN CODE:
"""
class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def solve(node):
            if node is None:
                return 0

            leftHeight = solve(node.left)
            rightHeight = solve(node.right)

            # update the diameter
            self.diameter = max(self.diameter, leftHeight + rightHeight)

            # return height for parent calculation
            return 1 + max(leftHeight, rightHeight)

        solve(root)
        return self.diameter
"""
---------------------------------------------------------
EXAMPLE 1:
Input:
    [1,2,3,4,5]

Tree:
        1
       / \
      2   3
     / \
    4   5

Step-by-step:

Node 4:
- left = 0, right = 0 → height = 1
- diameter = 0

Node 5:
- left = 0, right = 0 → height = 1
- diameter = 0

Node 2:
- leftHeight = 1 (from 4)
- rightHeight = 1 (from 5)
- diameter = max(0, 1+1 = 2)
- height = 1 + max(1,1) = 2

Node 3:
- left = 0, right = 0 → height = 1
- diameter stays 2

Node 1:
- leftHeight = 2 (node 2)
- rightHeight = 1 (node 3)
- diameter = max(2, 2+1 = 3)
- height = 3

Final diameter = 3

This corresponds to paths:
    4 → 2 → 1 → 3
or  5 → 2 → 1 → 3

Length = 3 edges.

---------------------------------------------------------
EXAMPLE 2:
Input:
    [1,2]

Tree:
    1
   /
  2

Node 2:
- left = 0, right = 0 → height = 1
- diameter = 0

Node 1:
- leftHeight = 1
- rightHeight = 0
- diameter = 1

Final diameter = 1
Path = 2 → 1

---------------------------------------------------------
TIME & SPACE COMPLEXITY:

Time Complexity: O(N)
We do a DFS visiting each node once.

Space Complexity: O(H)
H = height of tree (worst-case = N for skewed tree).

---------------------------------------------------------
FINAL CONCLUSION:
The diameter of a binary tree is the longest downward path between any
two nodes. It can be computed efficiently using DFS by calculating
subtree heights and updating the diameter at every node.

This solution is optimal and clean, and is the standard approach used
in interviews.
"""

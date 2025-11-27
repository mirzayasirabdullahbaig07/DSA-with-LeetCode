"""
124. Binary Tree Maximum Path Sum — FULL EXPLANATION (String Comment Format)

---------------------------------------------------------
PROBLEM SUMMARY:
You must find the maximum path sum in a binary tree.

A path:
- Can start/end at ANY node
- Must follow parent-child edges
- Cannot revisit the same node
- Does NOT have to pass through the root

Goal: Maximize the sum of node values along any valid path.

---------------------------------------------------------
MAIN IDEA:
For every node, there are two types of path values to consider:

1) BEST DOWNWARD PATH to return to parent:
      node.val + max(leftGain, rightGain)

   This can choose ONLY ONE side (left OR right), 
   because returning upward cannot take both sides.

2) BEST COMPLETE PATH THROUGH CURRENT NODE:
      leftGain + node.val + rightGain

   This path can include both left and right child.
   This is a potential candidate for maximum path sum.

We maintain a global max value `self.maxi`
and update it using every node’s complete path.

---------------------------------------------------------
IMPORTANT RULE:
Negative path sums should be treated as 0 because:
- Adding a negative path reduces total sum.
- So: max(0, leftSum) and max(0, rightSum)

Examples:
If left subtree gives -5 → we ignore it.

---------------------------------------------------------
ALGORITHM DETAILS:

def solve(node):
    If node is None → return 0 (no contribution)

    leftGain = max(0, solve(node.left))
    rightGain = max(0, solve(node.right))

    # candidate for global maximum
    bestPathThroughNode = leftGain + node.val + rightGain

    update global:
    self.maxi = max(self.maxi, bestPathThroughNode)

    # return best single-side path to parent
    return node.val + max(leftGain, rightGain)

---------------------------------------------------------
TOP LEVEL:
We call solve(root)
Return self.maxi

---------------------------------------------------------
WHY IT WORKS:
At every node we compute:
- The best path that goes THROUGH the node (possibly using both children)
- The best path that goes UP from this node (only one child)

This ensures we explore all possible paths in the tree.

---------------------------------------------------------
DRY RUN OF EXAMPLE 1:
Input: [1,2,3]

Tree:
      1
     / \
    2   3

At node 2:
    left = 0
    right = 0
    bestThrough = 2
    return = 2

At node 3:
    left = 0
    right = 0
    bestThrough = 3
    return = 3

At node 1:
    leftGain = 2
    rightGain = 3
    bestThrough = 2 + 1 + 3 = 6 (candidate for global max)
    return to parent = 1 + max(2,3) = 4

Global max = 6

Output: 6

---------------------------------------------------------
DRY RUN OF EXAMPLE 2:
Input: [-10,9,20,null,null,15,7]

Tree:
           -10
           /  \
          9    20
              /  \
             15   7

Node 9:
    left=0, right=0
    bestThrough = 9
    return = 9

Node 15:
    bestThrough = 15
    return = 15

Node 7:
    bestThrough = 7
    return = 7

Node 20:
    leftGain = 15
    rightGain = 7
    bestThrough = 15 + 20 + 7 = 42   ← big path
    return = 20 + max(15, 7) = 35

Node -10:
    leftGain = 9
    rightGain = 35
    bestThrough = 9 - 10 + 35 = 34
    return = -10 + 35 = 25

Comparing all global updates:
    9, 15, 7, 42, 34 → maximum is 42

Output: 42

---------------------------------------------------------
TIME & SPACE COMPLEXITY:

Time Complexity: O(N)
Every node is processed exactly once.

Space Complexity: O(H)
H = height of tree (recursion depth)
Worst: O(N) (skewed tree)
Best: O(log N) (balanced tree)

---------------------------------------------------------
FINAL SUMMARY:
- We compute two values:
    1) best single-direction path for parent
    2) best full path through node
- Ignore negative paths because they reduce total sum.
- Update global maximum at every node.
- This is the optimal solution used in real interviews.

"""


# === FINAL CODE IMPLEMENTATION ===

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        self.maxi = float('-inf')   # global maximum path sum

        def solve(node):
            if not node:
                return 0

            # compute left and right gains, ignore negatives
            leftGain = max(0, solve(node.left))
            rightGain = max(0, solve(node.right))

            # best complete path that passes through this node
            currentPath = leftGain + node.val + rightGain

            # update global maximum
            self.maxi = max(self.maxi, currentPath)

            # return best gain if path goes up
            return node.val + max(leftGain, rightGain)

        solve(root)
        return self.maxi

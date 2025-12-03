"""
199. Binary Tree Right Side View — Explanation (VS Code Friendly)

QUESTION SUMMARY:
-----------------
Imagine you are standing on the RIGHT side of a binary tree.  
You need to return the list of node values that are visible from top → bottom.

Meaning:
At each level of the tree, the RIGHTMOST node is visible.

EXAMPLE:
--------
Input:  [1,2,3,null,5,null,4]
Right side visible nodes = [1, 3, 4]

WHY?
Level 0 → 1  
Level 1 → 3 (right child of root)  
Level 2 → 4 (rightmost in that level)

WHAT THE ALGORITHM DOES:
------------------------
We use DFS (Depth-First Search) with a simple technique:

→ ALWAYS VISIT RIGHT CHILD FIRST  
→ THEN VISIT LEFT CHILD

Why visit RIGHT first?
Because the FIRST node we see at each level (while going right → left)
is the rightmost node for that level.

We keep a list `ans`, and:
If `level == len(ans)`  
--> this means we are entering this level for the first time  
--> so append the current node value

ALGORITHM TYPE:
---------------
→ DFS (Depth-First Search)  
→ Pre-order style: RIGHT → LEFT  
→ Uses recursion + level tracking  

This guarantees we pick the rightmost nodes.

TIME COMPLEXITY:
----------------
O(N)
Where N is the total number of nodes.
Each node is visited once.

SPACE COMPLEXITY:
-----------------
O(H)
Where H is the height of the tree → recursion stack.

Balanced tree → O(log N)  
Skewed tree → O(N)

This is the optimal solution.

"""

class Solution:
    def rightSideView(self, root):
        ans = []

        def dfs(node, level):
            if not node:
                return
            
            # If this level is visited for the FIRST time,
            # this node is the RIGHTMOST node for that level
            if level == len(ans):
                ans.append(node.val)

            # Always go RIGHT first
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)
        return ans

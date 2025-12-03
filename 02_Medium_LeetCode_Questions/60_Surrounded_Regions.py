"""
130. Surrounded Regions
-----------------------

PROBLEM:
Given an m x n board of 'X' and 'O', capture all regions surrounded by 'X'. 
A region is captured by flipping all 'O's in that region to 'X'. 
An 'O' on the border, or connected to the border, cannot be captured.

TECHNIQUE USED:
    - Depth-First Search (DFS)
    - Graph traversal to mark safe regions

ALGORITHM / APPROACH:
1. Observation:
    - Any 'O' connected to the border (top, bottom, left, right edges) cannot be captured.
    - So we first identify and mark these "safe" 'O's.

2. Steps:
    a. Traverse all border cells. If a border cell has 'O', run DFS to mark all connected 'O's as safe (here we use 'S').
    b. DFS recursively visits 4-directionally adjacent cells and marks 'O' as 'S'.
    c. After marking safe regions:
        - Traverse the entire board:
            - Convert remaining 'O' to 'X' (these are surrounded)
            - Convert 'S' back to 'O' (safe cells)

WHY IT WORKS:
    - DFS ensures all connected 'O's to the border are visited and marked.
    - Remaining unmarked 'O's are completely surrounded by 'X', so they can be safely flipped.

TIME COMPLEXITY:
    - O(M * N) where M = number of rows, N = number of columns
    - Each cell is visited at most once during DFS.

SPACE COMPLEXITY:
    - O(M * N) in worst case due to recursive DFS call stack
"""

class Solution:
    def solve(self, board):
        if not board:
            return
        
        rows, cols = len(board), len(board[0])

        # DFS function to mark safe 'O'
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if board[r][c] != 'O':
                return
            
            board[r][c] = "S"   # Mark as safe
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Mark all 'O' connected to borders
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        # 2. Convert remaining 'O' to 'X' and safe 'S' back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"

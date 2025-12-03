"""
1020. Number of Enclaves
------------------------

PROBLEM:
Given an m x n grid where 0 represents sea and 1 represents land, return the number of land cells 
that cannot reach the boundary of the grid through any sequence of moves (up, down, left, right).

TECHNIQUE USED:
    - Breadth-First Search (BFS)
    - Grid traversal to mark reachable land cells

ALGORITHM / APPROACH:
1. Observation:
    - Any land cell (1) on the boundary, or connected to a boundary land cell, cannot be counted as an enclave.
    - So we first mark all land cells reachable from the boundary as visited.

2. Steps:
    a. Initialize a visited matrix to keep track of visited land cells.
    b. Traverse all boundary cells. If a boundary cell is land (1) and unvisited, add it to a BFS queue.
    c. Perform BFS:
        - Pop a cell from the queue
        - Visit all 4-directionally adjacent land cells and mark them as visited
        - Add them to the queue
    d. After BFS, all land cells reachable from the boundary are marked.
    e. Traverse the grid and count land cells (1) that are unvisited → these are enclaves.

WHY IT WORKS:
    - BFS ensures all land cells connected to the boundary are visited.
    - Remaining unvisited land cells are completely enclosed by sea (0) → they are enclaves.

TIME COMPLEXITY:
    - O(M * N) where M = number of rows, N = number of columns
    - Each cell is visited at most once during BFS.

SPACE COMPLEXITY:
    - O(M * N) for visited matrix + O(M * N) worst-case queue size

"""

from collections import deque
from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque()

        # Step 1: Push all boundary land cells (1's) into queue
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:
                    if grid[r][c] == 1 and visited[r][c] == 0:
                        queue.append((r, c))
                        visited[r][c] = 1

        # Step 2: BFS to mark all reachable land cells from boundary
        while queue:
            i, j = queue.popleft()

            for x, y in [(-1,0), (1,0), (0,-1), (0,1)]:
                new_i = i + x
                new_j = j + y

                if 0 <= new_i < rows and 0 <= new_j < cols:
                    if grid[new_i][new_j] == 1 and visited[new_i][new_j] == 0:
                        queue.append((new_i, new_j))
                        visited[new_i][new_j] = 1
        
        # Step 3: Count land cells NOT visited (these are enclaves)
        enclaves = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c] == 0:
                    enclaves += 1
        
        return enclaves

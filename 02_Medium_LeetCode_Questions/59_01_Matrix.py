"""
542. 01 Matrix
---------------

PROBLEM:
Given a binary matrix `mat`, return a matrix where each cell contains the distance 
to the nearest 0. Distance between two adjacent cells (sharing an edge) is 1.

TECHNIQUE USED:
    - Breadth-First Search (BFS)
    - Multi-source BFS (all 0's are sources)

ALGORITHM / APPROACH:
1. Initialize:
    - A queue containing coordinates of all 0's in the matrix.
    - A visited matrix to mark processed cells.
    - A distance matrix to store distances from nearest 0.
2. BFS traversal:
    - Pop a cell (i, j) and its distance `d` from the queue.
    - Update distance[i][j] = d
    - For all 4-directionally adjacent cells:
        - If in bounds and not visited:
            - Append (new_i, new_j, d+1) to the queue.
            - Mark as visited.
3. Continue until the queue is empty.
4. Return the distance matrix.

WHY IT WORKS:
    - BFS guarantees that we visit cells in increasing order of distance from the nearest 0.
    - Multi-source BFS (starting from all 0's) ensures shortest distance is calculated efficiently.

TIME COMPLEXITY:
    - O(M * N) where M = number of rows, N = number of columns
    - Each cell is visited at most once.

SPACE COMPLEXITY:
    - O(M * N) for the queue in worst case
    - O(M * N) for visited matrix
    - O(M * N) for distance matrix
"""

from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        distance = [[0] * cols for _ in range(rows)]
        visited = [[0] * cols for _ in range(rows)]
        queue = deque()

        # Step 1: Push all 0's into BFS queue
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))
                    visited[r][c] = 1

        # Step 2: BFS
        while queue:
            i, j, d = queue.popleft()
            distance[i][j] = d

            # Check all 4 directions
            for x, y in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                new_i, new_j = i + x, j + y

                # Check boundaries
                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue

                # Skip visited cells
                if visited[new_i][new_j] == 1:
                    continue

                queue.append((new_i, new_j, d + 1))
                visited[new_i][new_j] = 1

        return distance

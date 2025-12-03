"""
994. Rotting Oranges
--------------------

PROBLEM:
Given a grid where:
    0 = empty cell
    1 = fresh orange
    2 = rotten orange
Each minute, fresh oranges 4-directionally adjacent to rotten oranges become rotten.
Return the minimum minutes until no fresh oranges remain, or -1 if impossible.

TECHNIQUE USED:
    - Breadth-First Search (BFS)
    - Queue-based level-order traversal

ALGORITHM / APPROACH:
1. Initialize a queue with all rotten oranges' positions.
2. Count the total number of fresh oranges.
3. Perform BFS level by level:
    - Each level represents one minute.
    - For each rotten orange, rot adjacent fresh oranges (up, down, left, right).
    - Update the queue with newly rotten oranges.
    - Decrease fresh orange count.
4. Stop when queue is empty or no fresh oranges remain.
5. If any fresh oranges remain → return -1.
6. Otherwise → return total minutes elapsed.

WHY IT WORKS:
    - BFS ensures that oranges rot in parallel per minute (level-order traversal).
    - Using a queue preserves the correct order of rotting spread.
    - Each level of BFS corresponds to one minute passing.

TIME COMPLEXITY:
    - O(M*N) where M = number of rows, N = number of columns
    - Each cell is visited at most once.

SPACE COMPLEXITY:
    - O(M*N) for queue in worst case (all oranges rotten initially)
"""

from copy import deepcopy
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        grid_copy = deepcopy(grid)  # To avoid modifying original grid

        fresh_cnt = 0
        queue = deque()

        # Initialize queue with rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid_copy[r][c] == 2:
                    queue.append((r, c))
                elif grid_copy[r][c] == 1:
                    fresh_cnt += 1
                    
        minutes = 0
        
        # BFS: rot adjacent fresh oranges level by level
        while len(queue) != 0 and fresh_cnt > 0:
            minutes += 1
            total_rotten = len(queue)
            for _ in range(total_rotten):
                i, j = queue.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_i, new_j = i + dx, j + dy
                    # Skip out-of-bounds or non-fresh cells
                    if new_i < 0 or new_i == rows or new_j < 0 or new_j == cols:
                        continue
                    if grid_copy[new_i][new_j] == 0 or grid_copy[new_i][new_j] == 2:
                        continue
                    # Rot the fresh orange
                    fresh_cnt -= 1
                    grid_copy[new_i][new_j] = 2
                    queue.append((new_i, new_j))
                    
        # If fresh oranges remain → impossible
        if fresh_cnt > 0:
            return -1
        return minutes

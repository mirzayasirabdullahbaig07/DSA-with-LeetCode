"""
733. Flood Fill
---------------

PROBLEM:
Given an image represented as an m x n grid of integers (pixels), perform a flood fill 
starting from a given pixel (sr, sc) and change all connected pixels of the same 
initial color to a new color. Connected pixels are 4-directionally adjacent.

TECHNIQUE USED:
    - Breadth-First Search (BFS)
    - Queue-based level-order traversal

ALGORITHM / APPROACH:
1. Check if starting pixel already has the target color:
    - If yes, return the original image (no need to process).
2. Initialize:
    - `initial_color` = color at starting pixel.
    - A queue with starting pixel coordinates (sr, sc).
3. BFS traversal:
    - While the queue is not empty:
        - Pop a pixel from the queue.
        - Change its color to the target color.
        - Check all 4-directionally adjacent pixels:
            - If adjacent pixel is within bounds and has the same initial color:
                - Add it to the queue.
4. Continue until all connected pixels of the initial color are updated.
5. Return the modified image.

WHY IT WORKS:
    - BFS ensures we visit all pixels connected to the starting pixel.
    - Each pixel is visited only once, preventing infinite loops.
    - Using a visited grid or modifying in-place avoids revisiting.

TIME COMPLEXITY:
    - O(M * N) where M = number of rows, N = number of columns.
    - Each pixel is visited at most once.

SPACE COMPLEXITY:
    - O(M * N) for queue in worst case (all pixels are same color and connected).
    - O(M * N) extra space if deepcopy is used, can be optimized by modifying in-place.
"""

from collections import deque
from copy import deepcopy

class Solution:
    def floodFill(self, image, sr, sc, color):
        # If the starting pixel is already the target color, no need to process
        if image[sr][sc] == color:
            return image
        
        # Make a copy to avoid modifying the original image
        visited = deepcopy(image)
        rows = len(visited)
        cols = len(visited[0])
        initial_color = visited[sr][sc]
        
        # BFS queue
        queue = deque()
        queue.append((sr, sc))
        
        while len(queue) != 0:
            i, j = queue.popleft()
            visited[i][j] = color
            
            # Check all 4 directions
            for x, y in [(-1,0),(0,-1),(1,0),(0,1)]:
                new_i = i + x
                new_j = j + y
                
                # Check boundaries
                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue
                
                # Add to queue if same as initial color
                if visited[new_i][new_j] == initial_color:
                    queue.append((new_i, new_j))
        
        return visited

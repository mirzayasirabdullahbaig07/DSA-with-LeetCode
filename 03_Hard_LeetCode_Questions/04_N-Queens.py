"""
Problem: LeetCode 51 — N-Queens
-----------------------------------
You are given an integer n, representing an n×n chessboard.
You need to place n queens such that no two queens attack each other.

Return all distinct solutions where 'Q' = Queen and '.' = Empty cell.

Example:
---------
Input: n = 4
Output: [
    [".Q..","...Q","Q...","..Q."],
    ["..Q.","Q...","...Q",".Q.."]
]

Constraint: 1 <= n <= 9
"""

# ============================================================
# BRUTE FORCE APPROACH
# ============================================================
"""
 Intuition:
-------------
Imagine you're placing queens column by column on the chessboard.
For each position, you check:
    - No queen is in the same row
    - No queen on upper-left diagonal
    - No queen on lower-left diagonal

If it’s safe, place the queen and move to the next column.
If not safe, backtrack and try another row.

 Algorithm:
--------------
1 Start from column 0
2 For each row, check if placing a queen is safe:
     - Check upper-left diagonal
     - Check left row
     - Check lower-left diagonal
3 If safe, place 'Q' and recurse for next column
4 If all queens are placed (col == n), store the solution
5 Backtrack: remove 'Q' and try next position

 Time Complexity:
-------------------
O(N^N) — for each column, we explore N rows and check safety in O(N)

 Space Complexity:
--------------------
O(N^2) — for board representation + recursion depth

Technique Used:
------------------
 Backtracking + Full Board Scan
 Simulates the decision tree of possible queen placements
"""

class Solution:
    def isSafe1(self, row, col, board, n):
        # Check upper-left diagonal
        r, c = row, col
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        # Check left row
        c = col
        while c >= 0:
            if board[row][c] == 'Q':
                return False
            c -= 1

        # Check lower-left diagonal
        r, c = row, col
        while r < n and c >= 0:
            if board[r][c] == 'Q':
                return False
            r += 1
            c -= 1

        return True

    def solve(self, col, board, ans, n):
        # Base case: all columns filled
        if col == n:
            ans.append(list(board))
            return
        
        for row in range(n):
            if self.isSafe1(row, col, board, n):
                # Place queen
                board[row] = board[row][:col] + "Q" + board[row][col+1:]
                self.solve(col + 1, board, ans, n)
                # Backtrack
                board[row] = board[row][:col] + "." + board[row][col+1:]

    def solveNQueens(self, n: int):
        ans = []
        board = ["." * n for _ in range(n)]
        self.solve(0, board, ans, n)
        return ans


# ============================================================
# OPTIMAL APPROACH — Using Hash Sets for O(1) Conflict Detection
# ============================================================
"""
Intuition:
-------------
In brute force, checking each direction is costly (O(N)).
We can make it O(1) by tracking rows and diagonals in hash sets.

Observation:
---------------
 Each row has a unique ID → `row`
 Lower diagonal ↘ has constant (row + col)
 Upper diagonal ↗ has constant (n - 1 + col - row)

Using this property, we can quickly check if a position conflicts
with an existing queen in O(1) time instead of scanning.

Algorithm:
--------------
1 Maintain three arrays:
     - leftrow[row] → if a queen is in this row
     - lowerDiagonal[row + col] → if occupied
     - upperDiagonal[n-1 + col - row] → if occupied
2 Place queen only if all three are free
3 Update arrays when placing/removing queens (backtracking)
4 When col == n, store current board as a valid solution

 Time Complexity:
-------------------
O(N!) — still exponential, but safety checks are O(1)

 Space Complexity:
--------------------
O(N) — tracking arrays and recursion depth

Technique Used:
------------------
 Backtracking + Hash Sets (Optimization)
 Mathematical Diagonal Representation
 Constant-Time Conflict Checking
"""

class Solution:
    def solve(self, col, board, ans, leftrow, upperDiagonal, lowerDiagonal, n):
        # Base Case: All queens placed
        if col == n:
            ans.append(board[:])
            return

        for row in range(n):
            if leftrow[row] == 0 and lowerDiagonal[row + col] == 0 and upperDiagonal[n - 1 + col - row] == 0:
                # Place queen
                board[row] = board[row][:col] + "Q" + board[row][col + 1:]
                leftrow[row] = 1
                lowerDiagonal[row + col] = 1
                upperDiagonal[n - 1 + col - row] = 1

                # Move to next column
                self.solve(col + 1, board, ans, leftrow, upperDiagonal, lowerDiagonal, n)

                # Backtrack (Remove queen)
                board[row] = board[row][:col] + "." + board[row][col + 1:]
                leftrow[row] = 0
                lowerDiagonal[row + col] = 0
                upperDiagonal[n - 1 + col - row] = 0

    def solveNQueens(self, n: int):
        ans = []
        board = ["." * n for _ in range(n)]
        leftrow = [0] * n
        upperDiagonal = [0] * (2 * n - 1)
        lowerDiagonal = [0] * (2 * n - 1)
        self.solve(0, board, ans, leftrow, upperDiagonal, lowerDiagonal, n)
        return ans


# ============================================================
# Summary Comparison
# ============================================================
"""
Approach Comparison:
---------------------------------------------------------------
| Approach                  | Time Complexity | Space | Key Idea            |
|-----------------------------|----------------|--------|---------------------|
| Brute Force (Full Scan)     | O(N^N)         | O(N^2) | Check board manually|
| Optimal (Hash Sets + Math)  | O(N!)          | O(N)   | Use diagonals math  |

Optimal Method Advantages:
- O(1) conflict checks (via hash sets)
- No repeated scans
- Mathematically efficient
- Perfect for large N (up to 9 in constraints)

Concept Summary:
-------------------
- Uses Backtracking
- Tracks state using HashSets
- Mathematical Diagonal Representation (row±col)
- Applies Recursive DFS-style exploration
- Classic AI Search / Constraint Satisfaction Pattern

Technique Used:
-------------------
Backtracking + State Tracking + Constraint Pruning
(used in real AI constraint-solving algorithms)
"""

# Example Run
sol = Solution()
print(sol.solveNQueens(4))
"""
Expected Output:
[
    [".Q..","...Q","Q...","..Q."],
    ["..Q.","Q...","...Q",".Q.."]
]
"""

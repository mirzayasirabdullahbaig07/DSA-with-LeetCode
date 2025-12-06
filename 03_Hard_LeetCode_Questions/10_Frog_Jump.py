"""
FROG JUMP – EXPLANATION

We are given a list called 'stones' which contains the positions of stones in a river.
The frog starts at position 0 (stones[0]) and wants to reach the last stone.

RULES:
1. The frog must start with a jump of exactly 1 unit.
2. If the last jump was 'k', the next jump can be:
       - k - 1
       - k
       - k + 1
3. The frog can only move forward.
4. The frog can land ONLY on stones — not in water.

OBJECTIVE:
Return True if the frog can reach the last stone.
Return False otherwise.

---------------------------------
WHY THIS IS NOT A SIMPLE PROBLEM?
---------------------------------
At every stone, the frog may have multiple possible jump sizes.
Every jump size leads to more possibilities, creating a branching effect.

Example:
If the frog jumps with k = 2,
next possible jumps are 1, 2, 3.

We must explore all possible paths and check if ANY path reaches the last stone.

---------------------------------
HOW THE DP (HASHSET) APPROACH WORKS:
---------------------------------
We create a dictionary called 'dp', where:
    dp[stone_position] = set of possible jump sizes that can reach this stone

For example:
    dp[0] = {1}   (frog must start with jump size 1)

Then for each stone:
    For each jump 'k' that can reach this stone:
        compute next_position = stone + k

        If next_position is the last stone:
            return True immediately.

        If next_position is a valid stone:
            Add possible next jumps:
                (k - 1), k, (k + 1)
            But (k - 1) must be > 0.

---------------------------------
WHY THIS WORKS EFFICIENTLY:
---------------------------------
Instead of checking every possible jump on every position,
we store ONLY the jump sizes that can actually reach each stone.

This avoids unnecessary computation.

---------------------------------
FINAL RESULT:
If we can fill dp until the last stone has at least one jump size
that can reach it → return True.
Else → return False.

"""
# Code:
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {stone: set() for stone in stones}
        dp[0].add(1)

        stone_set = set(stones)

        for stone in stones:
            for k in dp[stone]:
                nxt = stone + k
                if nxt == stones[-1]:
                    return True
                if nxt in dp:
                    if k - 1 > 0:
                        dp[nxt].add(k - 1)
                    dp[nxt].add(k)
                    dp[nxt].add(k + 1)

        return False

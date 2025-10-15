"""
💡 LeetCode 2220: Minimum Bit Flips to Convert Number
-----------------------------------------------------

Problem:
Given two integers `start` and `goal`, return the *minimum number of bit flips*
to convert `start` to `goal`.

A bit flip means changing a bit from 0 → 1 or 1 → 0.

Problem Link: https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

Example 1:
-----------
Input: start = 10, goal = 7
Output: 3
Explanation:
Binary of 10 = 1010
Binary of 7  = 0111
We can flip:
 1010 -> 1011 (flip last bit)
 1011 -> 1111 (flip 3rd bit)
 1111 -> 0111 (flip 4th bit)
Hence, total 3 flips.

Example 2:
-----------
Input: start = 3, goal = 4
Output: 3
Explanation:
Binary of 3 = 011
Binary of 4 = 100
We can flip:
 011 -> 010
 010 -> 000
 000 -> 100
Hence, 3 flips required.

Constraints:
------------
0 <= start, goal <= 10^9
"""

# ============================================================
# 🧩 Solution 1: Optimal Approach (Bitwise Shift Method)
# ============================================================

"""
Intuition:
-------------
Think of two binary numbers as two strings of lights.
XOR operation (^) highlights exactly which bits are different.

If start = 10 (1010), goal = 7 (0111)
Then XOR → 1101 → shows 3 differing bits.

Each 1 bit in XOR result represents one flip required.
So, we just need to count the number of 1s in XOR.

Steps:
------
Perform XOR → start ^ goal → gives bits that differ.
For each of 32 bits → check if bit is set using bitwise AND.
Count the total number of set bits → that's the answer.
"""

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal   # XOR to find differing bits
        count = 0            # Count how many 1s (flips)

        # Check all 32 possible bits (since integer is 32-bit)
        for i in range(0, 32):
            # If i-th bit is set, increment count
            if ans & (1 << i) != 0:
                count += 1

        return count


"""
🧮 Dry Run:
-----------
Input: start = 10, goal = 7
Binary: 10 → 1010, 7 → 0111
XOR → 1101 (13)

i=0: 1101 & 0001 = 0001 → count = 1
i=1: 1101 & 0010 = 0000 → count = 1
i=2: 1101 & 0100 = 0100 → count = 2
i=3: 1101 & 1000 = 1000 → count = 3

Result: 3 flips needed

Time Complexity:
O(1) — always checks 32 bits (fixed)

Space Complexity:
O(1)

Simplified Analogy:
----------------------
XOR gives you a "difference fingerprint" of two numbers.
Counting 1s tells you how many lights (bits) differ.
"""


# ============================================================
# 🧩 Solution 2: Optimal Approach (While Loop Method)
# ============================================================

"""
Intuition:
-------------
Same XOR idea — find bits that differ.
But instead of looping fixed 32 times,
we keep right-shifting XOR result until all bits are processed.

Each time we check the least significant bit (LSB):
- If it’s 1 → it means we need a flip.
- Then divide by 2 (shift right) to move to next bit.

This continues until XOR becomes 0.
"""

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal  # XOR gives differing bits
        count = 0           # To count the 1 bits

        # Keep checking bits until XOR becomes 0
        while ans > 0:
            # If last bit is 1 → increment count
            if ans % 2 == 1:
                count += 1
            # Divide by 2 to move to next bit
            ans = ans // 2

        return count


"""
🧮 Dry Run:
-----------
Input: start = 10, goal = 7
Binary: 1010 vs 0111 → XOR = 1101 (13)

ans = 13 → odd → count=1, ans=6
ans = 6  → even → count=1, ans=3
ans = 3  → odd → count=2, ans=1
ans = 1  → odd → count=3, ans=0 → stop

Result: 3 flips

Time Complexity:
O(log n) — depends on number of bits (≤32)

Space Complexity:
O(1)

Simplified Analogy:
----------------------
We keep peeling off bits from the end,
counting how many 1s we encounter (flips needed).
"""


# ============================================================
# Summary
# ============================================================

"""
Comparison Table:

| Approach | Time Complexity | Space | Difficulty | Best For |
|-----------|-----------------|--------|-------------|-----------|
| Bitwise Shift | O(1) | O(1) | Easy | Fixed 32-bit check |
| While Loop    | O(log n) | O(1) | Easy | Dynamic check |

Both are optimal and rely on XOR — the core logic.
Key Takeaway:
----------------
Always think in terms of *bitwise difference*.
XOR is your best friend for finding differing bits.

Practice writing both approaches — they build solid
bit manipulation intuition for interviews and contests.
"""



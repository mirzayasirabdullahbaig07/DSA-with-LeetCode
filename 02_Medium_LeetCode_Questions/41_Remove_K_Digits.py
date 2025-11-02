"""
PROBLEM: Remove K Digits
--------------------------------------
You are given a string `num` representing a non-negative integer, 
and an integer `k`. You must remove exactly `k` digits from `num`
so that the resulting number is the **smallest possible**.

Return the smallest number as a string (without leading zeros).
If the result is an empty string, return "0".

--------------------------------------
Example 1:
Input:  num = "1432219", k = 3
Output: "1219"

Explanation:
Remove digits 4, 3, and 2 → remaining digits form 1219 which is the smallest possible.

Example 2:
Input:  num = "10200", k = 1
Output: "200"

Explanation:
Remove digit '1' to get "0200", then strip leading zeros → "200".

Example 3:
Input:  num = "10", k = 2
Output: "0"

--------------------------------------
CONSTRAINTS:
1 <= k <= len(num) <= 10^5
num consists of only digits 0–9
num does not have leading zeros (except "0" itself)
--------------------------------------
"""

# =====================================================================
# OPTIMAL APPROACH: Greedy + Monotonic Increasing Stack
# =====================================================================

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
         Intuition:
        -------------
        To get the smallest possible number after removing k digits,
        we should always remove digits that make the number "bigger"
        when a smaller digit appears later.

        So, we process digits **left to right** and:
        - Maintain a stack (monotonic increasing order)
        - Whenever we find a smaller digit than the top of the stack,
          we pop the larger one (if we still have deletions left, k > 0)
        - This ensures that earlier digits stay as small as possible
          → giving us the lexicographically smallest number.

         Key Greedy Idea:
        "Whenever you see a smaller number after a bigger one — 
         remove the bigger one (if you can)."

         Time Complexity:  O(n)
         Space Complexity: O(n)
        (Each digit is pushed & popped at most once)
        """

        stack = []   # This will store digits forming the smallest number

        # Step 1: Traverse each digit in num
        for digit in num:
            # While we can still remove digits (k > 0)
            # and the previous digit in stack is larger than the current digit,
            # pop it (remove it to make the number smaller)
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1

            # Push the current digit into stack
            stack.append(digit)

        # Step 2: If we still have digits to remove (k > 0),
        # remove from the END (because remaining digits are largest)
        while k > 0:
            stack.pop()
            k -= 1

        # Step 3: Convert stack to string and remove leading zeros
        result = "".join(stack).lstrip("0")

        # Step 4: Handle edge case → if result becomes empty, return "0"
        if len(result) == 0:
            return "0"
        return result


# =====================================================================
# DETAILED EXPLANATION (STEP BY STEP DRY RUN)
# =====================================================================

"""
Example 1:
-----------
Input:  num = "1432219", k = 3

Initial: stack = []

Step 1: Read '1' → stack = ['1']      (nothing to remove)
Step 2: Read '4' → stack = ['1', '4'] (non-decreasing so keep)
Step 3: Read '3' → since '4' > '3' and k=3>0 → pop '4', k=2
                     stack = ['1']
                 push '3' → stack = ['1', '3']
Step 4: Read '2' → since '3' > '2' → pop '3', k=1
                     stack = ['1']
                 push '2' → stack = ['1', '2']
Step 5: Read '2' → equal to previous, just push → ['1', '2', '2']
Step 6: Read '1' → since '2' > '1' → pop '2', k=0 (no more removals)
                     stack = ['1', '2']
                 push '1' → stack = ['1', '2', '1']
Step 7: Read '9' → push → ['1', '2', '1', '9']

Now k = 0 → Done!

Final stack = ['1', '2', '1', '9']
Result = "1219"
OUTPUT: "1219"
------------------------------------------

Example 2:
-----------
Input:  num = "10200", k = 1

Traverse:
'1' → stack = ['1']
'0' → '1' > '0' → pop '1', k=0 → stack=[]
Push '0' → ['0']
Push '2' → ['0', '2']
Push '0' → ['0', '2', '0']
Push '0' → ['0', '2', '0', '0']

Join → "0200"
Remove leading zeros → "200"
OUTPUT: "200"
------------------------------------------

Example 3:
-----------
Input: num = "10", k = 2
- Remove '1' when we see '0'
- Then remove '0' (k still remains)
Stack empty → return "0"
OUTPUT: "0"
------------------------------------------
"""

# =====================================================================
# TESTING SECTION
# =====================================================================

if __name__ == "__main__":
    sol = Solution()
    print(" Example 1 Output:", sol.removeKdigits("1432219", 3))  # Expected: "1219"
    print(" Example 2 Output:", sol.removeKdigits("10200", 1))   # Expected: "200"
    print(" Example 3 Output:", sol.removeKdigits("10", 2))      # Expected: "0"
    print(" Example 4 Output:", sol.removeKdigits("112", 1))     # Expected: "11"
    print(" Example 5 Output:", sol.removeKdigits("10001", 4))   # Expected: "0"

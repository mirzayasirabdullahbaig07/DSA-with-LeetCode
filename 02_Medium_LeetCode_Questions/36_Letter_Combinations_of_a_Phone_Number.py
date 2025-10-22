"""
LeetCode 17: Letter Combinations of a Phone Number
-----------------------------------------------------

Problem Statement:
Given a string containing digits from 2–9 inclusive, return all possible letter combinations
that the number could represent (like on an old phone keypad).
Return the answer in any order.

Example:
---------
Input:  digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Constraints:
------------
1 <= digits.length <= 4
digits[i] ∈ ['2'–'9']

Mapping (Traditional Keypad):
-----------------------------
2 → "abc"
3 → "def"
4 → "ghi"
5 → "jkl"
6 → "mno"
7 → "pqrs"
8 → "tuv"
9 → "wxyz"

---------------------------------------------------------------------------
INTUITION

1 Brute Force Intuition:
--------------------------
We can think of this problem as forming all possible words using letters
from each digit — that means we need to pick one letter per digit.

If digits = "23":
   - For '2' → a,b,c
   - For '3' → d,e,f
   → Possible combinations = Cartesian product of ["abc"] × ["def"]
     = [ad, ae, af, bd, be, bf, cd, ce, cf]

So brute force approach is to manually generate all possible combinations
using nested loops — but this doesn’t scale when digits grow.

2 Optimal Intuition (Backtracking):
------------------------------------
This is a *tree exploration problem*.
Each digit expands into multiple possible letters.
We explore each branch recursively and build combinations step by step.

For example, "23":

               ""
           /    |    \
          a     b     c
         /|\   /|\   /|\
        d e f d e f d e f

Every path from root to leaf → one valid combination.

We use recursion to explore all branches until we reach the length of digits.
This avoids manual nested loops and works dynamically for any length.

---------------------------------------------------------------------------
ALGORITHM (Backtracking)

1. Create a dictionary `digits_to_letters` to map digits to corresponding letters.
2. Define a recursive helper function:
    - Base Case → If index == len(digits): add current combination to result.
    - Recursive Step → For current digit, loop over each letter and call recursion
      for next index with updated string.
3. Handle edge case: if digits = "", return [].
4. Start recursion from index = 0 and an empty current string.

---------------------------------------------------------------------------
BRUTE FORCE CODE (Static Loops for Small Inputs)
"""

def letterCombinations_bruteforce(digits):
    if not digits:
        return []
    
    mapping = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    
    # Brute force using nested loops (works only for <=4 digits)
    result = [""]
    for digit in digits:
        letters = mapping[digit]
        new_result = []
        for prefix in result:
            for letter in letters:
                new_result.append(prefix + letter)
        result = new_result
    return result

print(letterCombinations_bruteforce("23"))
# Output: ['ad','ae','af','bd','be','bf','cd','ce','cf']

"""
TIME COMPLEXITY (Brute Force):
---------------------------------
O(4^n * n)
Since each digit can map to at most 4 letters (7 or 9),
and we build all combinations of length n.

🧮 SPACE COMPLEXITY:
--------------------
O(4^n * n) for storing all results
O(n) recursion depth (if implemented recursively)
"""

# -------------------------------------------------------------------------
# OPTIMAL SOLUTION USING BACKTRACKING
# -------------------------------------------------------------------------

class Solution:
    def __init__(self):
        # Mapping digits to letters like a phone keypad
        self.digits_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def helper(self, digits, ans, index, current):
        # Base case: if all digits are processed, add result
        if index == len(digits):
            ans.append(current)
            return

        # Get all possible letters for the current digit
        letters = self.digits_to_letters[digits[index]]
        
        # 🔁 Explore each possibility recursively
        for letter in letters:
            self.helper(digits, ans, index + 1, current + letter)

    def letterCombinations(self, digits):
        ans = []
        if not digits:
            return ans
        
        self.helper(digits, ans, 0, "")
        return ans


# -------------------------------------------------------------------------
# EXAMPLE TEST
solution = Solution()
print(solution.letterCombinations("23"))
# Output: ['ad','ae','af','bd','be','bf','cd','ce','cf']

"""
---------------------------------------------------------------------------
TIME & SPACE COMPLEXITY (Optimal)
-----------------------------------
Time Complexity: O(4^n * n)
   - Each digit maps to up to 4 letters.
   - For n digits, we generate up to 4^n combinations.
   - Each combination takes O(n) to build.

Space Complexity: O(n)
   - Recursion depth = n (number of digits)
   - O(4^n * n) for storing all combinations.

---------------------------------------------------------------------------
TECHNIQUES USED
------------------
1. Backtracking (DFS-style recursion)
2. String building via concatenation
3. Decision tree exploration
4. Recursion + Base/Recursive cases pattern
5. Edge case handling for empty input

---------------------------------------------------------------------------
SUMMARY
----------
✔ The brute force uses nested loops (inefficient & rigid).
✔ The backtracking solution is dynamic, clean, and scalable.
✔ Perfect example of recursion and combinatorial generation.
✔ Common in interviews for recursion, DFS, and backtracking patterns.
✔ Similar to Cartesian Product problems.
✔ You can also solve using itertools.product for one-liner version.

---------------------------------------------------------------------------
ONE-LINE PYTHONIC ALTERNATIVE:
---------------------------------
from itertools import product
def letterCombinations(digits):
    if not digits: return []
    mapping = {"2":"abc","3":"def","4":"ghi","5":"jkl",
               "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    return [''.join(p) for p in product(*(mapping[d] for d in digits))]

---------------------------------------------------------------------------
"""

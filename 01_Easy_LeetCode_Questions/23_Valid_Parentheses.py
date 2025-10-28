"""
========================================================
Problem: Valid Parentheses
========================================================
Given a string `s` containing only the characters `()[]{}`,
determine if the input string is valid.

A string is considered valid if:
1. Every open bracket has a matching close bracket of the same type.
2. Brackets are closed in the correct order.
3. No unmatched or extra closing brackets exist.

--------------------------------------------------------
Example:
--------------------------------------------------------
Input 1: s = "()"
Output: True

Input 2: s = "()[]{}"
Output: True

Input 3: s = "(]"
Output: False

Input 4: s = "([)]"
Output: False

Input 5: s = "([])"
Output: True

--------------------------------------------------------
Constraints:
--------------------------------------------------------
1 <= len(s) <= 10^4
s consists only of characters: (), {}, []

========================================================
Brute Force Intuition:
========================================================
The brute-force approach repeatedly removes valid pairs "()", "{}", "[]"
from the string until no more valid pairs can be removed.

If the final string becomes empty, it means all parentheses were matched.

Otherwise, if any characters remain, the string is invalid.

--------------------------------------------------------
Brute Force Algorithm Steps:
--------------------------------------------------------
1. While any valid pair "()", "{}", or "[]" exists in the string:
   - Replace them with an empty string.
2. After all replacements, check if the string is empty.
   - If empty → valid
   - If not empty → invalid

--------------------------------------------------------
Brute Force Python Code:
--------------------------------------------------------
def isValid_bruteforce(s: str) -> bool:
    while "()" in s or "{}" in s or "[]" in s:
        s = s.replace("()", "")
        s = s.replace("{}", "")
        s = s.replace("[]", "")
    return s == ""

--------------------------------------------------------
Time Complexity (Brute Force):
--------------------------------------------------------
Each replace() call takes O(n), and in the worst case, it can occur O(n/2) times.
=> Overall Time Complexity: O(n^2)
=> Space Complexity: O(1) (if string replacement is in-place, otherwise O(n))

========================================================
Optimal Solution (Using Stack)
========================================================
Intuition:
--------------------------------------------------------
This problem naturally maps to a **stack** data structure.

- Push all opening brackets onto a stack.
- For every closing bracket:
  - If the stack is empty → invalid (no matching opening)
  - Pop the last opening bracket and check if it matches the current closing one.
  - If mismatched → invalid
- After processing all characters:
  - If the stack is empty → valid
  - Else → invalid (some open brackets never closed)

--------------------------------------------------------
Algorithm:
--------------------------------------------------------
1. Initialize an empty stack.
2. Traverse each character in the string:
   - If it’s an opening bracket ('(', '{', '[') → push to stack.
   - If it’s a closing bracket (')', '}', ']'):
       - If the stack is empty → return False
       - Pop top element and check if it matches.
       - If not matching → return False
3. After traversal, if stack is empty → return True else → False

--------------------------------------------------------
Data Structure Used:
--------------------------------------------------------
Stack (LIFO - Last In, First Out)

--------------------------------------------------------
Python Code:
--------------------------------------------------------
def isValid_stack(s: str) -> bool:
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack:
                return False
            top = stack.pop()
            if (ch == ')' and top != '(') or \
               (ch == '}' and top != '{') or \
               (ch == ']' and top != '['):
                return False
    return len(stack) == 0

--------------------------------------------------------
Dry Run Example:
--------------------------------------------------------
Input: s = "([])"
Step 1: '(' → push → stack = ['(']
Step 2: '[' → push → stack = ['(', '[']
Step 3: ']' → pop '[' → match found → stack = ['(']
Step 4: ')' → pop '(' → match found → stack = []
End: stack empty → return True

--------------------------------------------------------
Time and Space Complexity (Optimal Solution):
--------------------------------------------------------
Time Complexity: O(n)
    - Each character is processed once (push or pop)
Space Complexity: O(n)
    - In worst case, all characters are opening brackets and pushed onto stack

--------------------------------------------------------
When to Use Stack Approach:
--------------------------------------------------------
- When order of brackets matters.
- When nested or mixed types of brackets exist.
- For expression validation problems like HTML tags, mathematical expressions, etc.

--------------------------------------------------------
Summary:
--------------------------------------------------------
| Approach        | Time Complexity | Space | Technique Used |
|-----------------|-----------------|--------|----------------|
| Brute Force     | O(n^2)          | O(1)   | String replace |
| Stack (Optimal) | O(n)            | O(n)   | Stack (LIFO)   |

--------------------------------------------------------
Key Takeaway:
--------------------------------------------------------
- The stack-based approach is optimal.
- Brute force works for small strings but becomes inefficient for large inputs.
- Understanding stack behavior is essential for expression parsing and syntax validation.
"""

# ========================================================
# Brute Force Implementation
# ========================================================
def isValid_bruteforce(s: str) -> bool:
    while "()" in s or "{}" in s or "[]" in s:
        s = s.replace("()", "")
        s = s.replace("{}", "")
        s = s.replace("[]", "")
    return s == ""


# ========================================================
# Optimal Stack-Based Implementation
# ========================================================
def isValid_stack(s: str) -> bool:
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack:
                return False
            top = stack.pop()
            if (ch == ')' and top != '(') or \
               (ch == '}' and top != '{') or \
               (ch == ']' and top != '['):
                return False
    return len(stack) == 0


# ========================================================
# Testing Both Approaches
# ========================================================
if __name__ == "__main__":
    test_cases = ["()", "()[]{}", "(]", "([)]", "([])"]
    for case in test_cases:
        print(f"Input: {case}")
        print(f"Brute Force: {isValid_bruteforce(case)}")
        print(f"Stack-Based: {isValid_stack(case)}")
        print("-" * 40)

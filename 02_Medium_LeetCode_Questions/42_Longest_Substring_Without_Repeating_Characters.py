"""
PROBLEM: Longest Substring Without Repeating Characters
------------------------------------------------------------

You are given a string 's', and you must find the length of the
**longest substring** that contains **no repeating characters**.

A substring is a **contiguous sequence** of characters within a string.
(Unlike a subsequence, which can skip characters.)

------------------------------------------------------------
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
("bca" or "cab" are also valid answers.)

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that "pwke" is a subsequence and not a substring.

------------------------------------------------------------
Constraints:
0 <= s.length <= 5 * 10^4
s can contain English letters, digits, symbols, and spaces.
------------------------------------------------------------


=====================================================================
 BRUTE FORCE APPROACH (O(n²))
=====================================================================

INTUITION:
-------------
- For every possible starting point 'i', expand the substring character by character.
- Use a set or dictionary to keep track of seen characters.
- Stop expansion when a duplicate character is found.
- Track the maximum length of all valid substrings.

Although easy to understand, this method has **O(n²)** time complexity
and is inefficient for long strings.

 Time Complexity: O(n²)
 Space Complexity: O(min(n, Σ))   (Σ = total unique characters)


# ------------------------------------------------------------
# BRUTE FORCE IMPLEMENTATION
# ------------------------------------------------------------
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Base case: if empty string, return 0
        if len(s) == 0:
            return 0

        max_length = 0  # Store the longest length found

        # Outer loop: choose every start point
        for i in range(len(s)):
            seen = {}  # Dictionary to track seen characters

            # Inner loop: expand substring
            for j in range(i, len(s)):
                # If character repeats → break
                if s[j] in seen:
                    break

                # Otherwise, mark as seen and update max length
                seen[s[j]] = 1
                max_length = max(max_length, j - i + 1)

        return max_length

"""
 EXPLANATION:
---------------
1 Outer loop fixes a start position.
2 Inner loop expands substring from 'i' to 'j'.
3 When a duplicate character is found, break.
4 Track max length each time.

 Drawback:
------------
- Inefficient (O(n²)) — not suitable for long strings.
- Good for understanding the mechanics.


=====================================================================
 OPTIMAL SOLUTION — SLIDING WINDOW + HASH MAP (O(n))
=====================================================================

 INTUITION:
-------------
We use the **sliding window technique** with two pointers (`left` and `right`)
and a hash map to store the last seen index of every character.

Key idea:
- Expand the window by moving `right`.
- If a duplicate is found (character seen before and still inside window),
  move `left` just after its last occurrence.
- Update the longest valid window length during traversal.

This ensures each character is processed at most twice → O(n) time.


# ------------------------------------------------------------
# OPTIMAL CODE IMPLEMENTATION
# ------------------------------------------------------------
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store last seen index of each character
        hash_map = dict()

        # Initialize window pointers and max length
        left = 0
        right = 0
        length = 0
        n = len(s)

        # Traverse through all characters
        while right < n:
            # If duplicate character exists inside current window
            if s[right] in hash_map:
                # Move left pointer just after last seen duplicate
                left = max(hash_map[s[right]] + 1, left)

            # Update last seen index of current character
            hash_map[s[right]] = right

            # Calculate current valid window length
            length = max(length, right - left + 1)

            # Expand the window
            right += 1

        # Return longest length found
        return length

"""
=====================================================================
 DETAILED DRY RUN EXAMPLE
=====================================================================

Example: s = "abcabcbb"

Step-by-step execution:

Initialize:
hash_map = {}
left = 0
right = 0
length = 0

→ Read 'a' (index 0)
   Not seen before → store {'a': 0}
   length = 1

→ Read 'b' (index 1)
   Not seen → store {'a':0, 'b':1}
   length = 2

→ Read 'c' (index 2)
   Not seen → store {'a':0, 'b':1, 'c':2}
   length = 3

→ Read 'a' (index 3)
   Already seen → move left = max(0+1, 0) = 1
   Update {'a':3, 'b':1, 'c':2}
   length = max(3, 3-1+1) = 3

→ Continue similarly for 'b', 'c', 'b', 'b'...
   Final max length = 3 ("abc")

 OUTPUT: 3


=====================================================================
 TIME AND SPACE COMPLEXITY
=====================================================================

Time Complexity: O(n)
- Each character is visited at most twice (once by right, maybe once by left).

Space Complexity: O(min(n, Σ))
- Hash map stores at most unique characters of current window.


=====================================================================
 COMMON PITFALLS & TIPS
=====================================================================
 Ensure 'left' never moves backward: use `max()` when updating it.  
 Always update last seen index of characters.  
 Remember — substring must be continuous, subsequence is not allowed.  
 Works for all characters: letters, numbers, spaces, and symbols.  
 Sliding window is the standard pattern for “longest substring/window” problems.


=====================================================================
🏁 FINAL NOTES
=====================================================================
 Brute Force → great for understanding.
 Sliding Window → optimal for interviews.
 Core interview pattern for string and hash map problems.
 Used widely in “Longest substring/window with property” type questions.
=====================================================================
"""

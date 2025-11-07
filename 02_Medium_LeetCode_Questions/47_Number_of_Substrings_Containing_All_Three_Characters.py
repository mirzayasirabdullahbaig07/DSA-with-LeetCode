"""
 Problem Statement:
Given a string s consisting only of characters 'a', 'b', and 'c', return the number of substrings that contain at least one occurrence of all three characters 'a', 'b', and 'c'.

---

 Example 1:
Input: s = "abcabc"
Output: 10

 Example 2:
Input: s = "aaacb"
Output: 3

 Example 3:
Input: s = "abc"
Output: 1

---

============================
1 BRUTE FORCE SOLUTION
============================
 Intuition:
We check every possible substring and see if it contains all three characters: 'a', 'b', and 'c'.

 Approach:
- Loop over all start positions i.
- For every i, expand end position j.
- Keep adding characters to a set.
- If set size becomes 3, we found a valid substring → increment count.

 Code:
------------------------------------------------------------
"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            chars = set()
            for j in range(i, n):
                chars.add(s[j])
                if len(chars) == 3:
                    count += 1
        return count
"""
------------------------------------------------------------

 Example Dry Run for s = "abcabc":
All substrings:
"a", "ab", "abc" (1)
"abca"  (2)
"abcab"  (3)
"abcabc"  (4)
"bca" (5)
"bcab"  (6)
"bcabc"  (7)
"cab"  (8)
"cabc"  (9)
"abc"  (10)

Total = 10 substrings contain all 3 characters.

 Complexity:
Time = O(n²)
Space = O(1)
Simple but slow for large inputs.

---

============================
2 IMPROVED (WITH PRUNING)
============================
 Intuition:
Once we find a substring [i..j] that contains all three characters, all longer substrings starting at i and ending at j, j+1, ..., n-1 will also be valid.

So instead of checking beyond j, we can add (n - j) directly to count and break.

 Code:
------------------------------------------------------------
"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            chars = set()
            for j in range(i, n):
                chars.add(s[j])
                if len(chars) == 3:
                    count += n - j
                    break
        return count
"""
------------------------------------------------------------

 Example for s = "aaacb":
Substrings:
- Start i=0 → "a" (not valid), "aa" (not valid), "aaa" (not valid),
  "aaac" (not valid), "aaacb"   contains a, b, c → count += 5 - 4 = 1
- Start i=1 → "a", "ac", "acb"  count += 5 - 4 = 1
- Start i=2 → "a", "ac", "acb"  count += 5 - 4 = 1
Total = 3

So valid substrings: "aaacb", "aacb", "acb".

 Complexity:
Time = O(n²) in worst case, but faster due to early breaks.
Space = O(1)

---

============================
3 OPTIMAL (O(n)) USING LAST-SEEN INDEX
============================
 Intuition:
We only care about where 'a', 'b', and 'c' were last seen.

For each character at index i:
- Update last seen position for s[i].
- If all three characters have been seen at least once,
  we can form substrings that start from any index ≤ the minimum of last seen indices.

So, the number of valid substrings ending at i = min(last_seen.values()) + 1

 Code:
------------------------------------------------------------
"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        last = {'a': -1, 'b': -1, 'c': -1}
        for i in range(n):
            last[s[i]] = i
            if -1 not in last.values():
                count += min(last.values()) + 1
        return count
"""
------------------------------------------------------------

 Dry Run for s = "abcabc":

i=0 → 'a' → last = {a:0, b:-1, c:-1} → not all seen
i=1 → 'b' → last = {a:0, b:1, c:-1} → not all seen
i=2 → 'c' → last = {a:0, b:1, c:2} → all seen → min=0 → add 0+1=1
i=3 → 'a' → last = {a:3, b:1, c:2} → min=1 → add 1+1=2
i=4 → 'b' → last = {a:3, b:4, c:2} → min=2 → add 2+1=3
i=5 → 'c' → last = {a:3, b:4, c:5} → min=3 → add 3+1=4

Total = 1+2+3+4 = 10 

---

 Example for s = "aaacb":

i=0 → 'a' → last = {a:0, b:-1, c:-1} → not valid  
i=1 → 'a' → last = {a:1, b:-1, c:-1} → not valid  
i=2 → 'a' → last = {a:2, b:-1, c:-1} → not valid  
i=3 → 'c' → last = {a:2, b:-1, c:3} → not valid  
i=4 → 'b' → last = {a:2, b:4, c:3} → all seen → min=2 → add 2+1=3  

Total = 3  (substrings = "aaacb", "aacb", "acb")

---

 Example for s = "abc":
i=0 → 'a' → {a:0, b:-1, c:-1}
i=1 → 'b' → {a:0, b:1, c:-1}
i=2 → 'c' → {a:0, b:1, c:2} → min=0 → add 1
Total = 1  ("abc")

---

 Complexity:
Time = O(n)
Space = O(1)

---

 Final Comparison:

| Approach        | Time Complexity | Space | Key Idea |
|-----------------|-----------------|--------|-----------|
| Brute Force     | O(n²)           | O(1)   | Check every substring manually |
| Improved (Prune)| O(n²)           | O(1)   | Count all valid suffixes at once |
| Optimal (O(n))  | O(n)            | O(1)   | Use last seen indices to count valid substrings in one pass |

---

 Final Takeaway:
The optimal approach is elegant and efficient. By tracking the last seen index of 'a', 'b', and 'c', we can compute the count of all substrings containing all three characters in linear time. This pattern generalizes to many problems involving “substrings containing all required characters.”
"""


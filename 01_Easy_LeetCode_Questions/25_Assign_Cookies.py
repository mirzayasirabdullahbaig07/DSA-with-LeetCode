"""
 LeetCode Problem #455 — Assign Cookies
Difficulty: Easy
Topic: Greedy Algorithm
Companies: Amazon, Google, Meta, Microsoft, Bloomberg

---

 Problem Statement:
You are a parent who wants to give cookies to your children.  
Each child has a *greed factor* (minimum cookie size they need to be satisfied).  
Each cookie has a *size value*.  
A child is satisfied if they receive a cookie with a size >= their greed factor.

Goal:  
 Assign cookies such that the maximum number of children are content.  
Each child can receive at most one cookie.

---

 Example 1:
Input: 
g = [1, 2, 3]     # Greed factors of children  
s = [1, 1]        # Sizes of cookies  

Output: 
1

Explanation:  
- There are 3 children (greed factors 1, 2, and 3).  
- There are 2 cookies (both of size 1).  
 The first child (greed = 1) can be satisfied with one cookie of size 1.  
The other two children need bigger cookies.  
 So, only one child is satisfied → Output = 1.

---

 Example 2:
Input: 
g = [1, 2]  
s = [1, 2, 3]

Output: 
2

Explanation:
- Two children have greed factors 1 and 2.
- There are 3 cookies of sizes 1, 2, and 3.
 Assign cookie of size 1 to the child with greed 1.
 Assign cookie of size 2 to the child with greed 2.
 Both children are happy → Output = 2.

---

 Intuition:
This is a **Greedy Algorithm** problem.

We must **maximize the number of satisfied children** — not minimize total cookie usage.  
To do that, we should always give the **smallest possible cookie** that satisfies a child’s greed.

Why Greedy Works:
If we waste a big cookie on a less greedy child, we might run out of cookies for greedier children.  
Thus, we sort both arrays and start from the smallest greed and smallest cookie — pairing them efficiently.

---

 Step-by-Step Approach (Greedy Solution):
1 Sort both arrays:  
   - `g.sort()`  (children by greed)
   - `s.sort()`  (cookies by size)

2 Use two pointers:  
   - `child` → to track current child’s greed.  
   - `cookie` → to track current cookie size.

3 Compare greed vs cookie:
   - If `s[cookie] >= g[child]`: the cookie satisfies the child → move both pointers forward.
   - Else: cookie too small → move only cookie pointer forward.

4 Continue until either:
   - all children are satisfied, or
   - all cookies are used.

---

 Code Implementation (Greedy Approach):

"""
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort both lists
        g.sort()
        s.sort()
        
        child = 0   # Pointer for children
        cookie = 0  # Pointer for cookies
        count = 0   # Number of satisfied children
        
        # Iterate through both lists
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                count += 1      # The child is satisfied
                child += 1      # Move to next child
            cookie += 1         # Move to next cookie
        
        return count
"""
---

 Dry Run Example 1:
g = [1, 2, 3]
s = [1, 1]

Step 1: Sort both → (already sorted)
child=0, cookie=0, count=0

Iteration 1:
  s[0]=1, g[0]=1 → satisfies → count=1 → child=1, cookie=1
Iteration 2:
  s[1]=1, g[1]=2 → not enough → cookie=2 (end)

 Final Output = 1

---

 Dry Run Example 2:
g = [1, 2]
s = [1, 2, 3]

child=0, cookie=0, count=0

Iteration 1:
  s[0]=1, g[0]=1 → satisfies → count=1 → child=1, cookie=1
Iteration 2:
  s[1]=2, g[1]=2 → satisfies → count=2 → child=2, cookie=2 (end)

 Final Output = 2

---

 Alternate Thought (Brute Force - not efficient):
You could try matching every cookie with every child, but that’s O(n*m), too slow for large arrays.
The greedy approach is faster and optimal because sorting gives structure to the pairing.

---

 Time Complexity:
- Sorting children: O(n log n)
- Sorting cookies: O(m log m)
- Single pass pairing: O(n + m)
 Overall: **O(n log n + m log m)**

 Space Complexity:
- Sorting done in-place → O(1) extra space.

---

 Summary:

| Approach | Description | Time Complexity | Space Complexity | Efficient? |
|-----------|--------------|-----------------|------------------|-------------|
| Brute Force | Try all cookie-child matches | O(n*m) | O(1) |  |
| Greedy (Optimal) | Sort + two-pointer matching | O(n log n + m log m) | O(1) | |

---

 Conclusion:
- Always assign the **smallest sufficient cookie** to each child.
- Sorting ensures efficiency.
- Greedy algorithm guarantees the **maximum number of satisfied children**.
- This is a perfect example of how a simple greedy rule can optimize real-world resource allocation.

---
"""

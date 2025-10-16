"""
=========================================================
 LeetCode 136: Single Number
=========================================================

 Problem Statement:
----------------------
Given a non-empty array of integers `nums`, every element appears twice except for one.
Find that single one.

You must implement a solution with:
 Linear runtime complexity → O(n)
 Constant extra space → O(1)

-----------------------------------------------------------
 Examples:
-----------------------------------------------------------
Example 1:
Input:  nums = [2,2,1]
Output: 1

Example 2:
Input:  nums = [4,1,2,1,2]
Output: 4

Example 3:
Input:  nums = [1]
Output: 1

-----------------------------------------------------------
 Constraints:
-----------------------------------------------------------
1 <= nums.length <= 3 * 10⁴  
-3 * 10⁴ <= nums[i] <= 3 * 10⁴  
Each element in the array appears twice except for one element which appears only once.

=========================================================
SOLUTION 1 : Brute Force Approach (Using Hash Map)
=========================================================

 Intuition:
-------------
Imagine you’re counting how many times each person shows up at a party!
If most people come in pairs but one person comes alone, you want to find that lone person.

The simplest way is to keep a tally — count how many times each number appears in the array.
Then, look through your tally and find the number that appears only once. That’s our answer!

-----------------------------------------------------------
 Detailed Approach:
-----------------------------------------------------------
Create a Hash Map: Use a dictionary to store frequency of each number.   CountFrequencies: Loop through the array and increment the count for each number.  
Find Single Occurrence: Loop through the map to find the number with frequency  
Return the Result.

-----------------------------------------------------------
 Code Implementation:
-----------------------------------------------------------
"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        n = len(nums)
        hash_map = dict()

        # First Pass: Count frequency of each number
        for i in range(n):
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1

        # Second Pass: Find the number that appears only once
        for k in hash_map:
            if hash_map[k] == 1:
                return k


"""
-----------------------------------------------------------
 Code Explanation:
-----------------------------------------------------------
- We use a dictionary (hash_map) to track how many times each number appears.
- `.get()` safely increments the count (default 0 if not present).
- Finally, we return the number with frequency == 1.

-----------------------------------------------------------
 Dry Run Example:
-----------------------------------------------------------
nums = [4,1,2,1,2]

First Pass (Count Frequencies):
num=4 → {4:1}
num=1 → {4:1, 1:1}
num=2 → {4:1, 1:1, 2:1}
num=1 → {4:1, 1:2, 2:1}
num=2 → {4:1, 1:2, 2:2}

Second Pass (Find Single):
key=4 → freq=1 → return 4

 Result = 4

-----------------------------------------------------------
Time & Space Complexity:
-----------------------------------------------------------
Time Complexity: O(n)
- We traverse the array once to build the map
- Then another loop to find the single number

Space Complexity: O(n)
- We store up to n/2 + 1 elements in hash_map

-----------------------------------------------------------
 Simplified Intuition:
-----------------------------------------------------------
This approach is like keeping a guest list for a party:
You note down how many times each guest arrives,
and then check who came alone.
Simple and clear, but uses extra memory.
"""



"""
=========================================================
SOLUTION 2 : Optimal Approach (Bitwise XOR)
=========================================================

 Intuition:
-------------
Imagine a *magic trick* — pairs of identical items disappear when combined!
That’s what the XOR (^) operation does:

- XOR of a number with itself → 0
- XOR of a number with 0 → the number itself

If we XOR all numbers together,
pairs cancel out (become 0),
and the single number remains!

-----------------------------------------------------------
 Detailed Approach:
-----------------------------------------------------------
 Initialize a variable `ans = 0`
 Loop through all numbers and XOR each with `ans`
 After all XOR operations, the remaining value is the single number
 Return `ans`

-----------------------------------------------------------
 Code Implementation:
-----------------------------------------------------------
"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            ans = ans ^ nums[i]
        return ans


"""
-----------------------------------------------------------
 Code Explanation:
-----------------------------------------------------------
We use XOR properties:
 a ^ a = 0
 a ^ 0 = a
 XOR is commutative and associative (order doesn’t matter)

Since every element except one appears twice,
all duplicates cancel out, leaving only the single number.

-----------------------------------------------------------
 Dry Run Example:
-----------------------------------------------------------
nums = [4,1,2,1,2]

Step-by-step:
ans = 0
ans = 0 ^ 4 = 4
ans = 4 ^ 1 = 5
ans = 5 ^ 2 = 7
ans = 7 ^ 1 = 6  → (1 cancels with 1)
ans = 6 ^ 2 = 4  → (2 cancels with 2)

 Result = 4

-----------------------------------------------------------
 Binary View:
-----------------------------------------------------------
4 = 0100
1 = 0001
2 = 0010

Step 1: 0000 ^ 0100 = 0100 (4)
Step 2: 0100 ^ 0001 = 0101 (5)
Step 3: 0101 ^ 0010 = 0111 (7)
Step 4: 0111 ^ 0001 = 0110 (6)
Step 5: 0110 ^ 0010 = 0100 (4)

 Final Output = 4

-----------------------------------------------------------
 Time & Space Complexity:
-----------------------------------------------------------
Time Complexity: O(n)  → Single pass through array  
Space Complexity: O(1) → Constant extra space  

-----------------------------------------------------------
 Simplified Intuition:
-----------------------------------------------------------
Think of it like stacking pairs of identical cards.
Every matching pair disappears when stacked (XOR = 0),
and in the end, only one unique card remains in your hand.

-----------------------------------------------------------
 Summary:
-----------------------------------------------------------
| Approach | Time | Space | Difficulty | When to Use |
|-----------|-------|--------|-------------|-------------|
| Hash Map | O(n) | O(n) | Easy | Concept learning |
| XOR Trick | O(n) | O(1) | Medium | Optimal solution |

-----------------------------------------------------------
Key Takeaway:
-----------------------------------------------------------
The XOR approach is elegant and efficient.
It’s a beautiful example of using bitwise logic
to solve real-world problems with no extra memory.

This pattern is frequently used in interviews
and appears in problems like:
- "Find the unique number"
- "Find two numbers appearing once"
- "Missing number" (variation)
"""
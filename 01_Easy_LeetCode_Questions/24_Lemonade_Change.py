"""
 LeetCode 860 — Lemonade Change | Greedy Algorithm Explained
---------------------------------------------------------------

 Problem Statement:
You are running a lemonade stand where each lemonade costs $5.  
Customers come one by one and pay with $5, $10, or $20 bills.  
You must provide the correct change to each customer in order.

Initially, you have **no money** in hand.

Return **True** if you can give change to every customer, otherwise **False**.

---------------------------------------------------------------
 Example 1:
Input: bills = [5,5,5,10,20]
Output: True

 Step-by-step:
1 Customer 1 → pays $5 → no change needed → have: $5×1  
2 Customer 2 → pays $5 → no change needed → have: $5×2  
3 Customer 3 → pays $5 → no change needed → have: $5×3  
4 Customer 4 → pays $10 → give back one $5 → have: $5×2, $10×1  
5 Customer 5 → pays $20 → give back $10 + $5 → have: $5×1, $10×0  

 All customers got correct change → return True

---------------------------------------------------------------
 Example 2:
Input: bills = [5,5,10,10,20]
Output: False

 Step-by-step:
1 Customer 1 → pays $5 → no change needed → have: $5×1  
2 Customer 2 → pays $5 → no change needed → have: $5×2  
3 Customer 3 → pays $10 → give $5 → have: $5×1, $10×1  
4 Customer 4 → pays $10 → give $5 → have: $5×0, $10×2  
5 Customer 5 → pays $20 → need $15 change  
    Try $10 + $5 → not possible (no $5 left)  
    Try $5+$5+$5 → not possible (no $5s left)  
 Cannot give correct change → return False

---------------------------------------------------------------
 Intuition Behind the Solution:
This is a **Greedy Algorithm** problem.  
At each step, make the **locally optimal choice** —  
give change in a way that **preserves smaller bills** for future customers.

Since every lemonade costs $5, the only possible changes are:
- For $10 → need one $5
- For $20 → need $15 (either one $10 + one $5 OR three $5s)

So, to keep future flexibility:
 Always try to give $10 + $5 for $20 payments first  
 Only if not possible, give three $5s  

---------------------------------------------------------------
 Greedy Approach — Step-by-Step Logic:
1 Start with `five = 0` and `ten = 0`  
2 For each bill:
    - If it's 5 → add to `five`
    - If it's 10 → need one 5 as change
    - If it's 20:
          First give one 10 + one 5 if possible
          Else give three 5s
          If neither possible → return False
3 If loop completes → return True

---------------------------------------------------------------
 Code Implementation (Optimal Greedy Solution):
"""
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five = 0
        ten = 0
        
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five >= 1:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:  # bill == 20
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        
        return True
"""
---------------------------------------------------------------
 Step-by-Step Dry Run:

Example: bills = [5,5,5,10,20]
---------------------------------
Start: five=0, ten=0

→ Bill 5 → five=1, ten=0
→ Bill 5 → five=2, ten=0
→ Bill 5 → five=3, ten=0
→ Bill 10 → give $5 → five=2, ten=1
→ Bill 20 → give $10+$5 → five=1, ten=0

 All customers got correct change → return True


Example: bills = [5,5,10,10,20]
---------------------------------
Start: five=0, ten=0

→ Bill 5 → five=1, ten=0
→ Bill 5 → five=2, ten=0
→ Bill 10 → give $5 → five=1, ten=1
→ Bill 10 → give $5 → five=0, ten=2
→ Bill 20 → need $15 → can't give → return False

---------------------------------------------------------------
 Time and Space Complexity:
- Time Complexity: O(n) → we check each customer once
- Space Complexity: O(1) → only two counters (`five`, `ten`)

---------------------------------------------------------------
 Key Takeaways:
- Greedy algorithm works best because each local decision affects future outcomes.
- Always try to give higher denomination first (10 + 5 before 5 + 5 + 5).
- Simulating the process ensures correctness and simplicity.
- This pattern of “track resources + make optimal local choice” is used in many interview problems.

Clean, efficient, and interview-ready solution!
"""


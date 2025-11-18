"""
============================================================
🟦 LeetCode 57 – Insert Interval  
📘 Complete Explanation + All Solutions + Example Walkthrough  
============================================================

The “Insert Interval” problem is a popular interview question that tests your
understanding of interval merging, sorting, and handling boundary conditions.
The challenge is to insert a new interval into an already sorted, non-overlapping
set of intervals and merge if needed.

This problem is frequently asked at:
→ Google → Meta → Amazon → Microsoft → Uber → Adobe and many more.


============================================================
🧩 Problem Statement
============================================================
You are given:
1) A list of non-overlapping intervals, sorted by their start time.
2) A new interval that needs to be inserted into this list.

Your task:
➡️ Insert the new interval into the correct position  
➡️ Merge any intervals that overlap  
➡️ Return the final merged interval list  


------------------------------------------------------------
🔸 Example 1
------------------------------------------------------------
Input:
    intervals = [[1,3], [6,9]]
    newInterval = [2,5]

Output:
    [[1,5], [6,9]]

Explanation:
    The interval [2,5] overlaps with [1,3]
    Merge → [1,5]
    No overlap with [6,9]
    Final result → [[1,5], [6,9]]


------------------------------------------------------------
🔸 Example 2
------------------------------------------------------------
Input:
    intervals = [[1,2], [3,5], [6,7], [8,10], [12,16]]
    newInterval = [4,8]

Output:
    [[1,2], [3,10], [12,16]]

Explanation:
    newInterval [4,8] overlaps with:
        [3,5] → merge → [3,8]
        [6,7] → merge → [3,8]
        [8,10] → merge → [3,10]
    Non-overlapping intervals remain same.


============================================================
📌 IMPORTANT OBSERVATIONS
============================================================

Observation 1:
Intervals are sorted and non-overlapping  
→ This allows us to process from left to right easily.

Observation 2:
There are 3 types of intervals relative to newInterval:

1️⃣ Completely Before (end < newStart)  
2️⃣ Overlapping (start ≤ newEnd)  
3️⃣ Completely After (start > newEnd)

We handle them in this exact order.


============================================================
=========================================
SOLUTION 1 — Brute Force (Insert + Sort + Merge)
=========================================

💡 Intuition:
-------------
1. Insert the new interval into the list.  
2. Sort by start time.  
3. Merge overlapping intervals.

This is not optimal but very easy to understand.


------------------------------------------------------------
💻 Code:
------------------------------------------------------------
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
"""

------------------------------------------------------------
⏱️ Time Complexity:
    Sorting O(n log n)
    Merging O(n)
    Overall → O(n log n)

💾 Space Complexity:
    O(n)


============================================================
=========================================
SOLUTION 2 — Optimal Linear Solution (Most Efficient)
=========================================

💡 Intuition:
-------------
We go through the intervals in order and classify into 3 cases:

CASE 1: Interval ends before newInterval starts  
         → Keep as it is.

CASE 2: Interval overlaps with newInterval  
         → Merge by:
             newStart = min()
             newEnd = max()

CASE 3: Interval starts after newInterval ends  
         → Add newInterval first (if not added), then remaining intervals.


------------------------------------------------------------
💻 Code:
------------------------------------------------------------
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        # 1) Intervals completely before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # 2) Overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # Add merged interval
        res.append(newInterval)

        # 3) Remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res

"""
------------------------------------------------------------
 Time Complexity:
    O(n) — single pass
 Space Complexity:
    O(n) — result list


============================================================
 FULL WALKTHROUGH OF EXAMPLES (Optimal Approach)
============================================================

------------------------------------------------------------
Example 1:
intervals = [[1,3], [6,9]]
newInterval = [2,5]

Step 1: Add intervals ending before 2  
    [1,3] does NOT end before 2 → skip

Step 2: Merge overlaps  
    [1,3] overlaps with [2,5]  
        newInterval = [1,5]

    Next:
    [6,9] does NOT overlap → stop merging

Step 3: Add merged interval  
    res = [[1,5]]

Step 4: Add remaining intervals  
    res = [[1,5], [6,9]]

Final Output:
    [[1,5], [6,9]]


------------------------------------------------------------
Example 2:
intervals = [[1,2], [3,5], [6,7], [8,10], [12,16]]
newInterval = [4,8]

Step 1: Add intervals ending before 4  
    [1,2] → ends before 4 → add  
    [3,5] → does NOT end before → stop

res = [[1,2]]

Step 2: Merge overlaps  
    [3,5] overlaps → merge → [3,8]  
    [6,7] overlaps → merge → [3,8]  
    [8,10] overlaps → merge → [3,10]

Merged interval becomes:
    [3,10]

Step 3: Add merged interval  
    res = [[1,2], [3,10]]

Step 4: Add remaining intervals  
    res = [[1,2], [3,10], [12,16]]

Final Output:
    [[1,2], [3,10], [12,16]]


============================================================
=========================================
SOLUTION 3 — Insert Position + Merge (Alternative Clean Method)
=========================================

 Intuition:
-------------
1. Find position to insert newInterval  
2. Insert it  
3. Merge intervals normally  

Simpler but runs in O(n log n) due to merge step.


------------------------------------------------------------
 Code:
------------------------------------------------------------
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0

        # Add intervals that come before newInterval
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # Insert the new interval
        result.append(newInterval)

        # Add remaining intervals
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        
        # Merge all intervals
        merged = []
        for interval in result:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

"""
============================================================
 Comparison of Approaches
============================================================

| Approach | Time | Space | Notes |
|----------|--------|--------|-----------------------------|
| Brute Force | O(n log n) | O(n) | Easiest but slower |
| Optimal Linear | O(n) | O(n) | Most efficient |
| Insert + Merge | O(n log n) | O(n) | Clean alternative |


============================================================
 Conclusion
============================================================
The Insert Interval problem teaches important concepts:
✔ Interval merging  
✔ Linear scanning  
✔ Boundary conditions  
✔ Merging before and after  

The BEST solution is the **Optimal Linear Solution** because it handles everything in one pass with O(n) complexity.


============================================================
DONE ✓  
============================================================
"""

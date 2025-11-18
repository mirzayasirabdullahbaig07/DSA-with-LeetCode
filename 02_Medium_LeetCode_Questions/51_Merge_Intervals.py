"""
============================================================
 LeetCode 56 – Merge Intervals  
 Complete Explanation + All Solutions + Example Walkthrough  
============================================================

The “Merge Intervals” problem is one of the most classic interval problems
asked in real interviews. The goal is to merge all overlapping intervals and
return a clean, non-overlapping list of intervals.

------------------------------------------------------------
 PROBLEM STATEMENT
------------------------------------------------------------
You are given a list of intervals, each interval represented as:
    [start, end]

Your job:
    Combine (merge) all intervals that overlap
    Return the final list of merged intervals

Important Notes:
✔ Intervals may be unsorted  
✔ Intervals may overlap partially, fully, or not at all  
✔ You must return them in sorted order after merging  


------------------------------------------------------------
 EXAMPLES
------------------------------------------------------------

Example 1:
----------
Input:
    [[1,3], [2,6], [8,10], [15,18]]

Output:
    [[1,6], [8,10], [15,18]]

Explanation:
    [1,3] overlaps with [2,6] → merge → [1,6]
    The others do not overlap.


Example 2:
----------
Input:
    [[1,4], [4,5]]

Output:
    [[1,5]]

Explanation:
    The end of [1,4] touches the start of [4,5]
    This is still considered overlapping.


Example 3:
----------
Input:
    [[4,7], [1,4]]

Output:
    [[1,7]]

Explanation:
    [1,4] overlaps with [4,7]
    Merged into [1,7]


============================================================
============================================================
SOLUTION 1 — SORT + MERGE (Optimal, Most Used)
============================================================

 Intuition:
-------------
1. First sort intervals by their start time.
2. Iterate over sorted intervals:
    - If current interval does NOT overlap with previous → add it
    - If it DOES overlap → merge by updating end boundary

This is the most optimal and widely used solution.

Overlap Rule:
    A and B overlap if:
        A_end >= B_start


------------------------------------------------------------
 Code:
------------------------------------------------------------
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
"""

------------------------------------------------------------
 Time Complexity:
    Sorting → O(n log n)
    Merging → O(n)
    Total → O(n log n)

 Space Complexity:
    O(n)


============================================================
============================================================
SOLUTION 2 — BRUTE FORCE (Check All Pairs)
============================================================
Not efficient, but helpful for understanding.

Steps:
1. Sort intervals
2. Compare every interval with every other
3. Mark ones that should be merged
4. Combine and rebuild the list

But this is:
    Time → O(n²)
    Space → O(n)

Not recommended for interviews but good for learning.

Pseudo-code:
    For each interval:
        Check if it overlaps with another
        Merge if needed


============================================================
============================================================
SOLUTION 3 — SWEEP LINE / TIMELINE METHOD
============================================================

 Intuition:
-------------
1. Convert intervals into +1 / -1 events:
    Start → +1  
    End → -1  

2. Sort all events
3. Sweep through line:
    When active interval count goes from 0→1 → interval start  
    When active interval count goes 1→0 → interval end  

This is useful when:
✔ You want to detect how many intervals overlap at the same time  
✔ When solving advanced scheduling problems  


------------------------------------------------------------
 Time Complexity:
    Sorting events → O(n log n)
    Sweeping → O(n)

Same complexity as optimal but conceptually different.


============================================================
============================================================
DETAILED WALKTHROUGH OF ALL EXAMPLES
============================================================

------------------------------------------------------------
EXAMPLE 1
Input:
    [[1,3], [2,6], [8,10], [15,18]]

Step 1: Sort  
Result:
    [[1,3], [2,6], [8,10], [15,18]]

Step 2: Merge  
Start with [1,3]:

Compare with [2,6]:
    3 >= 2 → overlap  
    Merge → [1,6]

Next: compare [1,6] with [8,10]:
    6 < 8 → no overlap  
    Add [8,10]

Next: compare [8,10] with [15,18]:
    10 < 15 → no overlap  
    Add [15,18]

FINAL RESULT:
    [[1,6], [8,10], [15,18]]


------------------------------------------------------------
EXAMPLE 2
Input:
    [[1,4], [4,5]]

Step 1: Sort → already sorted

Step 2: Merge  
Start with [1,4]
Next interval: [4,5]

Check overlap:
    4 >= 4 → YES

Merge:
    New interval → [1,5]

FINAL RESULT:
    [[1,5]]


------------------------------------------------------------
EXAMPLE 3
Input:
    [[4,7], [1,4]]

Step 1: Sort  
    → [[1,4], [4,7]]

Step 2: Merge  
Start with [1,4]

Check overlap with [4,7]:
    4 >= 4 → YES  
    Merge → [1,7]

FINAL RESULT:
    [[1,7]]


============================================================
📊 COMPARISON OF ALL APPROACHES
============================================================

| Method                | Time           | Space | Notes |
|-----------------------|----------------|--------|-------|
| Brute Force           | O(n²)          | O(n)   | Only good for learning |
| Sort + Merge (Best)   | ⭐ O(n log n)   | O(n)   | Used in real interviews |
| Sweep Line            | O(n log n)     | O(n)   | Advanced interval logic |


============================================================
🏁 FINAL SUMMARY
============================================================
The BEST and simplest solution is:

    Sort intervals by start time  
    Merge overlapping ones using a linear scan  

This works because sorting ensures all potential overlaps are side-by-side.

This problem teaches:
✔ Sorting-based greedy merging  
✔ Overlap detection logic  
✔ Boundary edge cases (touching endpoints)  
✔ Efficient interval management  

Perfect for interviews at FAANG-level companies.

============================================================
DONE ✓
============================================================
"""

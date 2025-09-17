"""
Problem: Merge Intervals
------------------------
You are given an array of intervals where intervals[i] = [starti, endi].
The task is to merge all overlapping intervals and return an array of 
the non-overlapping intervals that cover all the intervals in the input.

Examples:
---------
1. Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
   Output: [[1,6],[8,10],[15,18]]
   Explanation: Intervals [1,3] and [2,6] overlap, so we merge them into [1,6].

2. Input: intervals = [[1,4],[4,5]]
   Output: [[1,5]]
   Explanation: Intervals [1,4] and [4,5] are considered overlapping.

3. Input: intervals = [[4,7],[1,4]]
   Output: [[1,7]]
   Explanation: Intervals [1,4] and [4,7] overlap, merged into [1,7].

-----------------------------------------------------
Techniques Used:
1. Sorting:
   - Sort the intervals by their start time so overlapping intervals appear next to each other.

2. Greedy Merge:
   - Traverse intervals one by one.
   - If the current interval does not overlap with the last merged interval → add it to the result.
   - If it overlaps → merge by updating the end value with max(end).

-----------------------------------------------------
Time Complexity:
- Sorting takes O(n log n), where n = number of intervals.
- Merging intervals takes O(n).
- Overall: O(n log n)

Space Complexity:
- O(n) for storing the merged intervals.
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by starting time
        intervals.sort(key=lambda x: x[0])
        
        merged = []  # result list
        
        # Step 2: Traverse each interval
        for interval in intervals:
            # Case 1: If no overlap → directly add interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Case 2: Overlap → merge by updating end time
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged

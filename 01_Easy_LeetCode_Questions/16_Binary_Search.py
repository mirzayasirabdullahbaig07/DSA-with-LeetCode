"""
🧠 Problem:
Given a sorted array `nums` and a target value `target`,
we need to find the index of `target` using an algorithm with O(log n) time complexity.
If the target does not exist, return -1.

Example:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

--------------------------------------------
💡 Why Binary Search?
--------------------------------------------
Because the array is sorted, we can divide the search space in half each time,
instead of checking elements one by one like linear search (O(n)).

Binary Search reduces the time complexity to O(log n)
by eliminating half of the remaining elements after each comparison.

--------------------------------------------
⚙️ Algorithm Steps (Iterative Approach)
--------------------------------------------
1️⃣ Initialize two pointers:
    - `low = 0`       → Start index of search range
    - `high = len(nums) - 1` → End index of search range

2️⃣ While `low <= high` (valid search range exists):
    - Find the middle index:
        mid = (low + high) // 2
    - Compare nums[mid] with target:
        ✅ If nums[mid] == target → Return mid (found)
        🔼 If nums[mid] < target  → Move to the right half → low = mid + 1
        🔽 If nums[mid] > target  → Move to the left half  → high = mid - 1

3️⃣ If the loop ends, return -1 (target not found).

--------------------------------------------
🧩 Code Implementation
--------------------------------------------
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0                           # start of the array
        high = len(nums) - 1              # end of the array

        while low <= high:                # loop while valid search range exists
            mid = (low + high) // 2       # calculate middle index

            # ✅ Case 1: Target found
            if nums[mid] == target:
                return mid

            # 🔼 Case 2: Target is greater → search right half
            elif nums[mid] < target:
                low = mid + 1

            # 🔽 Case 3: Target is smaller → search left half
            else:
                high = mid - 1

        # 🚫 Target not found
        return -1


"""
--------------------------------------------
🧮 DRY RUN EXAMPLE 1
--------------------------------------------
nums = [-1, 0, 3, 5, 9, 12]
target = 9

Step | low | high | mid | nums[mid] | Action
-----|-----|------|-----|-----------|--------
  1  |  0  |  5   |  2  |     3     | 3 < 9 → move right → low = 3
  2  |  3  |  5   |  4  |     9     | ✅ Found target → return 4

Output: 4

--------------------------------------------
🧮 DRY RUN EXAMPLE 2 (Target Not Found)
--------------------------------------------
nums = [-1, 0, 3, 5, 9, 12]
target = 2

Step | low | high | mid | nums[mid] | Action
-----|-----|------|-----|-----------|--------
  1  |  0  |  5   |  2  |     3     | 3 > 2 → move left → high = 1
  2  |  0  |  1   |  0  |    -1     | -1 < 2 → move right → low = 1
  3  |  1  |  1   |  1  |     0     | 0 < 2 → move right → low = 2
Loop ends (low > high) → return -1

Output: -1

--------------------------------------------
⏱️ TIME COMPLEXITY ANALYSIS
--------------------------------------------
At each step, we divide the array into two halves.
→ Total comparisons needed = log₂(n)

✅ Time Complexity: O(log n)
This is much faster than O(n) for linear search, especially for large datasets.

--------------------------------------------
💾 SPACE COMPLEXITY ANALYSIS
--------------------------------------------
We only use a few variables: low, high, mid
→ No extra data structures are used.

✅ Space Complexity: O(1)

--------------------------------------------
🧠 WHY IT WORKS
--------------------------------------------
Binary Search takes advantage of the sorted nature of the array.
Each iteration removes half of the possible search space.
Hence, it efficiently narrows down the location of the target in logarithmic time.

--------------------------------------------
🧱 EDGE CASES
--------------------------------------------
1️⃣ Target is at the start → nums = [1,2,3], target = 1 → Output: 0
2️⃣ Target is at the end   → nums = [1,2,3], target = 3 → Output: 2
3️⃣ Target not found       → nums = [1,3,5], target = 2 → Output: -1
4️⃣ Empty array            → nums = [], target = 10    → Output: -1
5️⃣ Single element array   → nums = [7], target = 7    → Output: 0

--------------------------------------------
✅ Summary
--------------------------------------------
Approach:       Binary Search (Iterative)
Time Complexity: O(log n)
Space Complexity: O(1)
Best For:        Searching in sorted arrays
--------------------------------------------
"""

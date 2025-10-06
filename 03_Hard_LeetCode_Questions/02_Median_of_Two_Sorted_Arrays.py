"""
LeetCode 4: Median of Two Sorted Arrays
---------------------------------------

Problem Statement:
------------------
You are given two sorted arrays nums1 and nums2 of size m and n respectively. 
Return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
----------
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] → median = 2

Example 2:
----------
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] → median = (2+3)/2 = 2.5

Constraints:
------------
- nums1.length == m
- nums2.length == n
- 0 <= m, n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6
"""

from typing import List

class Solution:
    # ---------------------------------------------------------
    # 🧩 Brute Force Solution: Merge and Find Median
    # ---------------------------------------------------------
    def findMedianSortedArrays_bruteforce(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Approach:
        ---------
        1. Merge the two sorted arrays into a single sorted array.
        2. If total elements are odd → return middle element.
        3. If even → return average of two middle elements.

        Time Complexity: O(m + n)
        Space Complexity: O(m + n)

        Dry Run:
        --------
        nums1 = [1,3], nums2 = [2]
        → merged = [1,2,3]
        → length = 3 (odd)
        → median = merged[1] = 2
        """
        result = []
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        
        # Merge both sorted arrays
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        # Add remaining elements
        while i < n:
            result.append(nums1[i])
            i += 1
        while j < m:
            result.append(nums2[j])
            j += 1
        
        l = len(result)
        if l % 2 == 0:
            return (result[l // 2 - 1] + result[l // 2]) / 2
        return result[l // 2]

    # ---------------------------------------------------------
    # ⚡ Better Solution: Find Median While Merging (No Full Merge)
    # ---------------------------------------------------------
    def findMedianSortedArrays_better(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Approach:
        ---------
        1. Use two pointers to traverse both arrays.
        2. Stop merging once you reach the median index.
        3. Track only the two middle elements required for median.

        Time Complexity: O(m + n)
        Space Complexity: O(1)

        Dry Run:
        --------
        nums1 = [1,2], nums2 = [3,4]
        Total = 4 → middle indices = 1, 2
        Step 1: pick 1
        Step 2: pick 2 (→ index 1)
        Step 3: pick 3 (→ index 2)
        Median = (2 + 3)/2 = 2.5
        """
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2
        ind2 = n // 2
        ind1 = ind2 - 1
        cnt = 0
        ind1el, ind2el = -1, -1
        i, j = 0, 0

        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                val = nums1[i]
                i += 1
            else:
                val = nums2[j]
                j += 1

            if cnt == ind1:
                ind1el = val
            if cnt == ind2:
                ind2el = val
            cnt += 1

        while i < n1:
            val = nums1[i]
            if cnt == ind1:
                ind1el = val
            if cnt == ind2:
                ind2el = val
            cnt += 1
            i += 1

        while j < n2:
            val = nums2[j]
            if cnt == ind1:
                ind1el = val
            if cnt == ind2:
                ind2el = val
            cnt += 1
            j += 1

        if n % 2 == 1:
            return float(ind2el)
        return (ind1el + ind2el) / 2.0

    # ---------------------------------------------------------
    # 🚀 Optimal Solution: Binary Search Partition
    # ---------------------------------------------------------
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Approach (Binary Search on Partition):
        --------------------------------------
        1. Ensure binary search runs on the smaller array.
        2. Partition both arrays so that:
            - left side has same elements as right side (or +1 if odd)
            - all elements in left ≤ all elements in right
        3. Median is then:
            - max(left) if odd total
            - (max(left) + min(right)) / 2 if even total

        Why this works:
        ----------------
        The number of days function is monotonic → suitable for binary search.

        Time Complexity: O(log(min(m, n)))
        Space Complexity: O(1)

        Dry Run:
        --------
        nums1 = [1,3], nums2 = [2]
        total = 3 → left half = 2 elements
        mid1 = 1 → mid2 = 1
        l1=1, l2=2, r1=3, r2=∞
        l1 ≤ r2 and l2 ≤ r1 → perfect partition
        Median = max(l1,l2) = 2
        """
        n1, n2 = len(nums1), len(nums2)

        # Always binary search on smaller array
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        n = n1 + n2
        left = (n + 1) // 2
        low, high = 0, n1

        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1

            l1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            l2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            r1 = float('inf') if mid1 == n1 else nums1[mid1]
            r2 = float('inf') if mid2 == n2 else nums2[mid2]

            # Perfect partition condition
            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return float(max(l1, l2))
                return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0.0


# ---------------------------------------------------------
# ✅ Example Test Cases
# ---------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    nums1 = [1, 3]
    nums2 = [2]
    print("Brute Force:", sol.findMedianSortedArrays_bruteforce(nums1, nums2))  # Expected: 2.0
    print("Better:", sol.findMedianSortedArrays_better(nums1, nums2))           # Expected: 2.0
    print("Binary Search:", sol.findMedianSortedArrays(nums1, nums2))           # Expected: 2.0

    # Example 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    print("Brute Force:", sol.findMedianSortedArrays_bruteforce(nums1, nums2))  # Expected: 2.5
    print("Better:", sol.findMedianSortedArrays_better(nums1, nums2))           # Expected: 2.5
    print("Binary Search:", sol.findMedianSortedArrays(nums1, nums2))           # Expected: 2.5

    # Example 3
    nums1 = [0, 0]
    nums2 = [0, 0]
    print("Binary Search:", sol.findMedianSortedArrays(nums1, nums2))           # Expected: 0.0

    # Example 4
    nums1 = []
    nums2 = [1]
    print("Binary Search:", sol.findMedianSortedArrays(nums1, nums2))           # Expected: 1.0

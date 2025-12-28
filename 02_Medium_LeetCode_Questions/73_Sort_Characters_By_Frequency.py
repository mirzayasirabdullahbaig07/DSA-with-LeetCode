
"""
        PROBLEM:
        --------
        Given a string s, sort its characters in decreasing order
        based on their frequency.

        APPROACH:
        ---------
        1. Count the frequency of each character.
        2. Sort characters by frequency in descending order.
        3. Repeat each character according to its frequency
           and join them into the final string.

        WHY THIS WORKS:
        ---------------
        - Characters with higher frequency appear first.
        - Characters with the same frequency can appear in any order.
        - Grouping is ensured by repeating characters together.

        TIME COMPLEXITY:
        ----------------
        Let n = length of the string
        Let k = number of unique characters

        - Counting frequency: O(n)
        - Sorting unique characters: O(k log k)
        - Building result string: O(n)

        Overall: O(n + k log k)
        Since k ≤ 62 (letters + digits), this is very efficient.

        SPACE COMPLEXITY:
        -----------------
        - Frequency dictionary: O(k)
        - Result list/string: O(n)

        Overall: O(n)
        """
class Solution:
    def frequencySort(self, s: str) -> str:

        # Step 1: Count frequency of each character
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Step 2: Sort characters by frequency (descending)
        # freq.items() -> (character, frequency)
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Step 3: Build the result efficiently using a list
        result = []
        for ch, count in sorted_chars:
            result.append(ch * count)

        # Join list into final string
        return "".join(result)

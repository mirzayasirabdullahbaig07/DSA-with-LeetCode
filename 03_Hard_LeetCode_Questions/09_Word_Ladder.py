"""
Algorithm Used:
---------------
Breadth-First Search (BFS)

Explanation:
------------
This problem can be viewed as finding the shortest path in an unweighted graph.
Each word is treated as a node, and two nodes are connected if their words differ
by exactly one letter. We do NOT build a full adjacency list because that is
expensive. Instead, for each word we generate all possible one-letter
transformations and check if they exist in the word list.

BFS is used because it explores level by level and guarantees finding the
shortest transformation sequence. The moment we reach endWord, the current
BFS level represents the shortest path length.

Approach:
---------
1. Convert wordList to a set for O(1) lookups.
2. If endWord is not in the set, return 0 immediately.
3. Use a BFS queue storing (current_word, current_level).
4. For each word removed from the queue:
    - Change each character position to all 26 possible letters.
    - Generate new words differing by one letter.
    - If the new word is in the set, push it to the BFS queue and remove it
      from the set to avoid revisiting.
5. Return level when endWord is reached.
6. If BFS finishes without finding endWord, return 0.

Time Complexity:
-----------------
O(N × M)
Where:
- N = number of words in the wordList
- M = length of each word

Explanation:
For each word processed by BFS, we try M positions and 26 possible
character substitutions. Checking membership in wordSet is O(1).
In worst case, BFS processes all words.

Space Complexity:
------------------
O(N)
Due to:
- wordSet storing up to N words
- BFS queue storing up to N words
No other large data structures used.

Summary:
--------
- Technique: BFS on implicit graph
- Approach: Generate neighbors by letter substitution
- Guarantees shortest sequence
- Time: O(N × M)
- Space: O(N)
"""
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        # If the endWord is not in dictionary, no possible transformation.
        if endWord not in wordSet:
            return 0

        # BFS queue contains (current_word, current_level)
        queue = deque()
        queue.append((beginWord, 1))

        while queue:
            curr_word, level = queue.popleft()

            # If reached endWord, return the number of words in the path.
            if curr_word == endWord:
                return level

            # Try changing each character of curr_word
            for i in range(len(curr_word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == curr_word[i]:
                        continue

                    # Generate a new word
                    new_word = curr_word[:i] + ch + curr_word[i+1:]

                    # If valid, push to queue and remove from wordSet
                    if new_word in wordSet:
                        queue.append((new_word, level + 1))
                        wordSet.remove(new_word)

        return 0

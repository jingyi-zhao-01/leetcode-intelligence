# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: length-of-the-longest-valid-substring
# source_path: LeetCode-Solutions-master/Python/length-of-the-longest-valid-substring.py
# solution_class: Solution
# submission_id: 5a008707999bf3eb9e235274b049d98daa731753
# seed: 3398574587

# Time:  O((m + n) * l), n = len(word), m = len(forbidden), l = max(len(w) for w in forbidden)
# Space: O(t), t is the size of trie

import collections


# two pointers, sliding window, trie

class Solution(object):
    def longestValidSubstring(self, word, forbidden):
        """
        :type word: str
        :type forbidden: List[str]
        :rtype: int
        """
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for w in forbidden:
            reduce(dict.__getitem__, w, trie)["_end"]
        result = 0
        right = len(word)-1
        for left in reversed(xrange(len(word))):
            node = trie
            for i in xrange(left, right+1):
                if word[i] not in node:  # O(l) times
                    break
                node = node[word[i]]
                if "_end" in node:
                    right = i-1
                    break
            result = max(result, right-left+1)
        return result
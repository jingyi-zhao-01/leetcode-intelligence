# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: top-k-frequent-words
# source_path: LeetCode-Solutions-master/Python/top-k-frequent-words.py
# solution_class: Solution4
# submission_id: bb81ebd90f0c0aae3a21e78106e8470bd42f7b28
# seed: 3122213737

# Time:  O(n + klogk) on average
# Space: O(n)

import collections
import heapq
from random import randint

class Solution4(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = Counter(words)
        candidates = counter.keys()
        candidates.sort(key=lambda w: (-counter[w], w))
        return candidates[:k]
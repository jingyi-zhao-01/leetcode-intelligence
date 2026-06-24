# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: top-k-frequent-words
# source_path: LeetCode-Solutions-master/Python/top-k-frequent-words.py
# solution_class: Solution2
# submission_id: 8c61a360e1d950636353f795e2032f1f44a86fce
# seed: 3853178713

# Time:  O(n + klogk) on average
# Space: O(n)

import collections
import heapq
from random import randint

class Solution2(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        class MinHeapObj(object):
            def __init__(self,val):
                self.val = val
            def __lt__(self,other):
                return self.val[1] > other.val[1] if self.val[0] == other.val[0] else \
                       self.val < other.val
            def __eq__(self,other):
                return self.val == other.val
            def __str__(self):
                return str(self.val)

        counts = collections.Counter(words)
        min_heap = []
        for word, count in counts.iteritems():
            heapq.heappush(min_heap, MinHeapObj((count, word)))
            if len(min_heap) == k+1:
                heapq.heappop(min_heap)
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap).val[1])
        return result[::-1]
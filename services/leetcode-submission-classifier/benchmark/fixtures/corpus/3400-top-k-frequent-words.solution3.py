# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: top-k-frequent-words
# source_path: LeetCode-Solutions-master/Python/top-k-frequent-words.py
# solution_class: Solution3
# submission_id: f909199a6c87b416bc102158a7268e6ec26c7e48
# seed: 2456237156

# Time:  O(n + klogk) on average
# Space: O(n)

import collections
import heapq
from random import randint

class Solution3(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = collections.Counter(words)
        buckets = [[] for _ in xrange(len(words)+1)]
        for word, count in counts.iteritems():
            buckets[count].append(word)
        pairs = []
        for i in reversed(xrange(len(words))):
            for word in buckets[i]:
                pairs.append((-i, word))
            if len(pairs) >= k:
                break
        pairs.sort()
        return [pair[1] for pair in pairs[:k]]
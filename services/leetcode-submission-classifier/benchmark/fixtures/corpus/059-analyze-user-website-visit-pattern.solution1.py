# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: analyze-user-website-visit-pattern
# source_path: LeetCode-Solutions-master/Python/analyze-user-website-visit-pattern.py
# solution_class: Solution
# submission_id: cb83dd5dac951bbe428596d0bde78a9bf53ea124
# seed: 3396871298

# Time:  O(n^3)
# Space: O(n^3)

import collections
import itertools

class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        lookup = collections.defaultdict(list)
        A = zip(timestamp, username, website)
        A.sort()
        for t, u, w in A:
            lookup[u].append(w)
        count = sum([collections.Counter(set(itertools.combinations(lookup[u], 3))) for u in lookup], collections.Counter())
        return list(min(count, key=lambda x: (-count[x], x)))
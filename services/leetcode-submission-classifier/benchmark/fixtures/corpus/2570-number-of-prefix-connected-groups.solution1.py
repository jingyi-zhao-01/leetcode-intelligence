# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-prefix-connected-groups
# source_path: LeetCode-Solutions-master/Python/number-of-prefix-connected-groups.py
# solution_class: Solution
# submission_id: eb212f833961f0457f0128f364d9ed63dc8c722c
# seed: 3581119631

# Time:  O(n * k)
# Space: O(n * k)

import collections


# freq table

class Solution(object):
    def prefixConnected(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: int
        """
        cnt = collections.defaultdict(int)
        for w in words:
            if len(w) < k:
                continue
            cnt[w[:k]] += 1
        return sum(v >= 2 for v in cnt.itervalues())
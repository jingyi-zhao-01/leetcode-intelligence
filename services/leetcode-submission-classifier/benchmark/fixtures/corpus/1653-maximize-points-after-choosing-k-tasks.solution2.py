# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-points-after-choosing-k-tasks
# source_path: LeetCode-Solutions-master/Python/maximize-points-after-choosing-k-tasks.py
# solution_class: Solution2
# submission_id: d706413fdcace7e3b8c96f9ac335193134300fa5
# seed: 1925502797

# Time:  O(n)
# Space: O(n)

import random


# quick select, greedy

class Solution2(object):
    def maxPoints(self, technique1, technique2, k):
        """
        :type technique1: List[int]
        :type technique2: List[int]
        :type k: int
        :rtype: int
        """
        idxs = range(len(technique1))
        idxs.sort(key=lambda i: technique1[i]-technique2[i], reverse=True)
        return sum(technique1[idxs[i]] if i < k else max(technique1[idxs[i]], technique2[idxs[i]]) for i in xrange(len(technique1)))
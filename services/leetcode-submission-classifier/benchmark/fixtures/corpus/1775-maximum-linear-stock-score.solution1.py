# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-linear-stock-score
# source_path: LeetCode-Solutions-master/Python/maximum-linear-stock-score.py
# solution_class: Solution
# submission_id: c0dab039e629658a0a9d405358c6363f6b5d6ade
# seed: 2826555502

# Time:  O(n)
# Space: O(n)

import collections


# math, freq table

class Solution(object):
    def maxScore(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cnt = collections.Counter()
        for i, x in enumerate(prices):
            cnt[x-i] += x
        return max(cnt.itervalues())
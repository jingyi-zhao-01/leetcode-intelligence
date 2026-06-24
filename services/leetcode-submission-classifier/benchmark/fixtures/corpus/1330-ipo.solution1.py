# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: ipo
# source_path: LeetCode-Solutions-master/Python/ipo.py
# solution_class: Solution
# submission_id: 9d25ecd9476e18d4cb9fed365b04bbf0942c11e0
# seed: 1371673267

# Time:  O(nlogn)
# Space: O(n)

import heapq

class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        curr = []
        future = sorted(zip(Capital, Profits), reverse=True)
        for _ in xrange(k):
            while future and future[-1][0] <= W:
                heapq.heappush(curr, -future.pop()[1])
            if curr:
                W -= heapq.heappop(curr)
        return W
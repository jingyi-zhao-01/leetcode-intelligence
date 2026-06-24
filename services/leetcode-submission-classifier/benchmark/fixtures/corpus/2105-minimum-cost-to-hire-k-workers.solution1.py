# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-hire-k-workers
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-hire-k-workers.py
# solution_class: Solution
# submission_id: 0bcaa5dbf788ae527a6bbe3e931c3e233dedcaca
# seed: 4189283670

# Time:   O(nlogn)
# Space : O(n)

import itertools
import heapq

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        result, qsum = float("inf"), 0
        max_heap = []
        for r, q in sorted([float(w)/q, q] for w, q in itertools.izip(wage, quality)):
            qsum += q
            heapq.heappush(max_heap, -q)
            if len(max_heap) > K:
                qsum -= -heapq.heappop(max_heap)
            if len(max_heap) == K:
                result = min(result, qsum*r)
        return result
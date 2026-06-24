# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-spending-after-buying-items
# source_path: LeetCode-Solutions-master/Python/maximum-spending-after-buying-items.py
# solution_class: Solution
# submission_id: 3957c3ef923fcd86223d7459c7d4d4f9dbdfe5cb
# seed: 1980114567

# Time:  O(m * n * logm)
# Space: O(m)

import heapq


# greedy, heap

class Solution(object):
    def maxSpending(self, values):
        """
        :type values: List[List[int]]
        :rtype: int
        """
        m, n = len(values), len(values[0])
        min_heap = [(values[i].pop(), i) for i in xrange(m)]
        heapq.heapify(min_heap)
        result = 0
        for d in xrange(1, m*n+1):
            x, i = heapq.heappop(min_heap)
            result += x*d
            if values[i]:
                heapq.heappush(min_heap, (values[i].pop(), i))
        return result
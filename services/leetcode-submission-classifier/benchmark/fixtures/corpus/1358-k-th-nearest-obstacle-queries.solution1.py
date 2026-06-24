# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: k-th-nearest-obstacle-queries
# source_path: LeetCode-Solutions-master/Python/k-th-nearest-obstacle-queries.py
# solution_class: Solution
# submission_id: db9cea8c3eead59a6b91d23eb9cc0aedc1d91d32
# seed: 3557216411

# Time:  O(qlogk)
# Space: O(k)

import heapq


# heap

class Solution(object):
    def resultsArray(self, queries, k):
        """
        :type queries: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        result = []
        max_heap = []
        for x, y in queries:
            heapq.heappush(max_heap, -(abs(x)+abs(y)))
            if len(max_heap) == k+1:
                heapq.heappop(max_heap)
            result.append(-max_heap[0] if len(max_heap) == k else -1)
        return result
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: last-stone-weight
# source_path: LeetCode-Solutions-master/Python/last-stone-weight.py
# solution_class: Solution
# submission_id: f19401eb743f3b1b784ae45924c1f77f26c5a88d
# seed: 3830473812

# Time:  O(nlogn)
# Space: O(n)

import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        for i in xrange(len(stones)-1):
            x, y = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -abs(x-y))
        return -max_heap[0]
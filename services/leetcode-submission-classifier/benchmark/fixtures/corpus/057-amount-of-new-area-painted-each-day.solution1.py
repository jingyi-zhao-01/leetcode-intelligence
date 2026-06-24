# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: amount-of-new-area-painted-each-day
# source_path: LeetCode-Solutions-master/Python/amount-of-new-area-painted-each-day.py
# solution_class: Solution
# submission_id: 95179de2e8b9682c3397b556e912d6fa544a0da7
# seed: 3648223645

# Time:  O(nlogn)
# Space: O(n)

import collections
import heapq


# line sweep, heap

class Solution(object):
    def amountPainted(self, paint):
        """
        :type paint: List[List[int]]
        :rtype: List[int]
        """
        points = collections.defaultdict(list)
        for i, (s, e) in enumerate(paint):
            points[s].append((True, i))
            points[e].append((False, i))
        min_heap = []
        lookup = [False]*len(paint)
        result = [0]*len(paint)
        prev = -1
        for pos in sorted(points.iterkeys()):
            while min_heap and lookup[min_heap[0]]:
                heapq.heappop(min_heap)
            if min_heap:
                result[min_heap[0]] += pos-prev
            prev = pos
            for t, i in points[pos]:
                if t:
                    heapq.heappush(min_heap, i)
                else:
                    lookup[i] = True
        return result
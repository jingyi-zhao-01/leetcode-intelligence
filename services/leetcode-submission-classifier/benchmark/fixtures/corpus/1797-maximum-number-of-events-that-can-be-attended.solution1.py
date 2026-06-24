# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-events-that-can-be-attended
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-events-that-can-be-attended.py
# solution_class: Solution
# submission_id: f1c890c43d0d13c889cf3d4eb79508e8a7e93139
# seed: 677089304

# Time:  O(r + nlogn), r is the max end day of events
# Space: O(n)

import heapq

class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort(reverse=True)
        min_heap = []
        result = 0
        for d in xrange(1, max(events, key=lambda x:x[1])[1]+1):
            while events and events[-1][0] == d:
                heapq.heappush(min_heap, events.pop()[1])
            while min_heap and min_heap[0] == d-1:
                heapq.heappop(min_heap)
            if not min_heap:
                continue
            heapq.heappop(min_heap)
            result += 1       
        return result
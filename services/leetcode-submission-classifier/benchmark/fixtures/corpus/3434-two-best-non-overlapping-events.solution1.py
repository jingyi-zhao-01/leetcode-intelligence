# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: two-best-non-overlapping-events
# source_path: LeetCode-Solutions-master/Python/two-best-non-overlapping-events.py
# solution_class: Solution
# submission_id: 4bc32fa1144f5ed45e62cbe7cf189655f63b8578
# seed: 2850693393

# Time:  O(nlogn)
# Space: O(n)

import heapq

class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort()
        result = best = 0
        min_heap = []
        for left, right, v in events:
            heapq.heappush(min_heap, (right, v))
            while min_heap and min_heap[0][0] < left:
                best = max(best, heapq.heappop(min_heap)[1])
            result = max(result, best+v)
        return result
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-profit-in-job-scheduling
# source_path: LeetCode-Solutions-master/Python/maximum-profit-in-job-scheduling.py
# solution_class: Solution
# submission_id: e6f26dc09d59a785f7b522b4264036d2b66c1e0c
# seed: 3828914074

# Time:  O(nlogn)
# Space: O(n)

import itertools
import bisect

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        min_heap = zip(startTime, endTime, profit)
        heapq.heapify(min_heap)
        result = 0
        while min_heap:
            s, e, p = heapq.heappop(min_heap)
            if s < e:
                heapq.heappush(min_heap, (e, s, result+p))
            else:
                result = max(result, p)
        return result
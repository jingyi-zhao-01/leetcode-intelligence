# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-time-required-to-eliminate-bacterial-strains
# source_path: LeetCode-Solutions-master/Python/find-time-required-to-eliminate-bacterial-strains.py
# solution_class: Solution
# submission_id: 35a5bec412e94cf82989670ddcd2209a3393b030
# seed: 600343045

# Time:  O(nlogn)
# Space: O(1)

import heapq


# heap, greedy

class Solution(object):
    def minEliminationTime(self, timeReq, splitTime):
        """
        :type timeReq: List[int]
        :type splitTime: int
        :rtype: int
        """
        heapq.heapify(timeReq)
        for _ in xrange(len(timeReq)-1):
            heapq.heappush(timeReq, max(heapq.heappop(timeReq), heapq.heappop(timeReq))+splitTime)
        return timeReq[0]
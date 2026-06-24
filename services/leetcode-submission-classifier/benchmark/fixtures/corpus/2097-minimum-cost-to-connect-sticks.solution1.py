# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-connect-sticks
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-connect-sticks.py
# solution_class: Solution
# submission_id: 4a994c0fd63fd8212d9bcee54606f76e44e08adf
# seed: 475180283

# Time:  O(nlogn)
# Space: O(n)

import heapq

class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        heapq.heapify(sticks)
        result = 0
        while len(sticks) > 1:
            x, y = heapq.heappop(sticks), heapq.heappop(sticks)
            result += x+y
            heapq.heappush(sticks, x+y)
        return result
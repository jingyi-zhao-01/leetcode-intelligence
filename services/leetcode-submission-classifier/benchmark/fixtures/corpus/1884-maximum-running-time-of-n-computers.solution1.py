# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-running-time-of-n-computers
# source_path: LeetCode-Solutions-master/Python/maximum-running-time-of-n-computers.py
# solution_class: Solution
# submission_id: 57de4ff4d048d72117723386557228513d9439e8
# seed: 2246230502

# Time:  O(nlogm)
# Space: O(1)

import heapq


# greedy

class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        total = sum(batteries)
        for i in xrange(len(batteries)):
            batteries[i] = -batteries[i]  # max_heap
        heapq.heapify(batteries)
        while -batteries[0] > total//n:
            n -= 1
            total -= -heapq.heappop(batteries)
        return total//n
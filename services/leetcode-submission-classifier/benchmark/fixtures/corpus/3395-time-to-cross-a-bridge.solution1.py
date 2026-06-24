# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: time-to-cross-a-bridge
# source_path: LeetCode-Solutions-master/Python/time-to-cross-a-bridge.py
# solution_class: Solution
# submission_id: aba8e1cad4a9f6b0715a377593c0508a6e1be8b2
# seed: 1256137634

# Time:  O(k + nlogk)
# Space: O(k)

import heapq


# heap, simulation

class Solution(object):
    def findCrossingTime(self, n, k, time):
        """
        :type n: int
        :type k: int
        :type time: List[List[int]]
        :rtype: int
        """
        left_bridge, right_ware, right_bridge, left_ware = [(-(time[i][0]+time[i][2]), -i) for i in xrange(k)], [], [], []
        heapq.heapify(left_bridge)
        curr = 0
        while n:
            while left_ware and left_ware[0][0] <= curr:
                _, i = heapq.heappop(left_ware)
                heapq.heappush(left_bridge, (-(time[i][0]+time[i][2]), -i))
            while right_ware and right_ware[0][0] <= curr:
                _, i = heapq.heappop(right_ware)
                heapq.heappush(right_bridge, (-(time[i][0]+time[i][2]), -i))
            if right_bridge:
                _, i = heapq.heappop(right_bridge)
                i = -i
                curr += time[i][2]
                heapq.heappush(left_ware, (curr+time[i][3], i))
                n -= 1
            elif left_bridge and n-len(right_ware):
                _, i = heapq.heappop(left_bridge)
                i = -i
                curr += time[i][0]
                heapq.heappush(right_ware, (curr+time[i][1], i))
            else:
                curr = min(left_ware[0][0] if left_ware else float("inf"),
                           right_ware[0][0] if right_ware else float("inf"))
        return curr
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-refueling-stops
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-refueling-stops.py
# solution_class: Solution
# submission_id: 04f81620ccb3224c5d923a288d2abf5fcbf62d44
# seed: 303470321

# Time:  O(nlogn)
# Space: O(n)

import heapq

class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        max_heap = []
        stations.append((target, float("inf")))

        result = prev = 0
        for location, capacity in stations:
            startFuel -= location - prev
            while max_heap and startFuel < 0:
                startFuel += -heapq.heappop(max_heap)
                result += 1
            if startFuel < 0:
                return -1
            heapq.heappush(max_heap, -capacity)
            prev = location

        return result
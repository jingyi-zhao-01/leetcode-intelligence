# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: meeting-scheduler
# source_path: LeetCode-Solutions-master/Python/meeting-scheduler.py
# solution_class: Solution
# submission_id: 1820577607394f93768339924f8e48ac8a9f2d72
# seed: 84151603

# Time:  O(n) ~ O(nlogn)
# Space: O(n)

import heapq

class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        min_heap = list(filter(lambda slot: slot[1] - slot[0] >= duration, slots1 + slots2))
        heapq.heapify(min_heap)  # Time: O(n)
        while len(min_heap) > 1:
            left = heapq.heappop(min_heap)  # Time: O(logn)
            right = min_heap[0]
            if left[1]-right[0] >= duration:
                return [right[0], right[0]+duration] 
        return []   
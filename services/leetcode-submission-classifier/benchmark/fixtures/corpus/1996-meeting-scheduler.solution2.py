# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: meeting-scheduler
# source_path: LeetCode-Solutions-master/Python/meeting-scheduler.py
# solution_class: Solution2
# submission_id: 66f2d5130d8b9779e48ed3df91f11aed2f6aae15
# seed: 1577051497

# Time:  O(n) ~ O(nlogn)
# Space: O(n)

import heapq

class Solution2(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        slots1.sort(key = lambda x: x[0])
        slots2.sort(key = lambda x: x[0])
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            left = max(slots1[i][0], slots2[j][0])
            right = min(slots1[i][1], slots2[j][1])
            if left+duration <= right:
                return [left, left+duration]
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        return []
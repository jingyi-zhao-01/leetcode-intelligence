# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: course-schedule-iii
# source_path: LeetCode-Solutions-master/Python/course-schedule-iii.py
# solution_class: Solution
# submission_id: 34886181ad3fd04e572a6ddea8d8f5a573be1e35
# seed: 2699403838

# Time:  O(nlogn)
# Space: O(k), k is the number of courses you can take

import collections
import heapq

class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key=lambda t_end: t_end[1])
        max_heap = []
        now = 0
        for t, end in courses:
            now += t
            heapq.heappush(max_heap, -t)
            if now > end:
                now += heapq.heappop(max_heap)
        return len(max_heap)
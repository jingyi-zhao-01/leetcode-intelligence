# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-students-doing-homework-at-a-given-time
# source_path: LeetCode-Solutions-master/Python/number-of-students-doing-homework-at-a-given-time.py
# solution_class: Solution
# submission_id: fb0f3286bd81ce4f76f0f4a4ae626ada1e3e0258
# seed: 1579203825

# Time:  O(n)
# Space: O(1)

import itertools

class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        return sum(s <= queryTime <= e for s, e in itertools.izip(startTime, endTime))
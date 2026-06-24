# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-right-interval
# source_path: LeetCode-Solutions-master/Python/find-right-interval.py
# solution_class: Solution
# submission_id: 72342f87725778988f33ded6a592a3e966a40803
# seed: 2673800692

# Time:  O(nlogn)
# Space: O(n)

import bisect

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        sorted_intervals = sorted((interval.start, i) for i, interval in enumerate(intervals))
        result = []
        for interval in intervals:
            idx = bisect.bisect_left(sorted_intervals, (interval.end,))
            result.append(sorted_intervals[idx][1] if idx < len(sorted_intervals) else -1)
        return result
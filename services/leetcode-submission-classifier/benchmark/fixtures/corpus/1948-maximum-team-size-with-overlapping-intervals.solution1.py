# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-team-size-with-overlapping-intervals
# source_path: LeetCode-Solutions-master/Python/maximum-team-size-with-overlapping-intervals.py
# solution_class: Solution
# submission_id: 594b854b70f963ec2cd471ef1ef7329eded2c8cd
# seed: 2022615802

# Time:  O(nlogn)
# Space: O(n)

import bisect


# sort, binary search

class Solution(object):
    def maximumTeamSize(self, startTime, endTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        sorted_start = sorted(startTime)
        sorted_end = sorted(endTime)
        return max(bisect.bisect_right(sorted_start, endTime[i])-bisect.bisect_left(sorted_end, startTime[i]) for i in xrange(len(startTime)))
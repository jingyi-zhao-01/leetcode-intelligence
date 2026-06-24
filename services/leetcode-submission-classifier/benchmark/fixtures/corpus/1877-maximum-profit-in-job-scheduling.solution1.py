# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-profit-in-job-scheduling
# source_path: LeetCode-Solutions-master/Python/maximum-profit-in-job-scheduling.py
# solution_class: Solution
# submission_id: 7b065a85e5a8b99f4c4f5792ceb2375cc75efc08
# seed: 3828914074

# Time:  O(nlogn)
# Space: O(n)

import itertools
import bisect

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        jobs = sorted(itertools.izip(endTime, startTime, profit))
        dp = [(0, 0)]
        for e, s, p in jobs:
            i = bisect.bisect_right(dp, (s+1, 0))-1
            if dp[i][1]+p > dp[-1][1]:
                dp.append((e, dp[i][1]+p))
        return dp[-1][1]
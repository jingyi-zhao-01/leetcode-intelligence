# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-events-that-can-be-attended-ii
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-events-that-can-be-attended-ii.py
# solution_class: Solution2
# submission_id: 8297f1ab368d6f56e1943f232be9c483cff1c977
# seed: 566404212

# Time:  O(nlogn + n * k)
# Space: O(n * k)

import bisect

class Solution2(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        events.sort()
        sorted_starts = [x[0] for x in events]
        dp = [[0]*(k+1) for _ in xrange(len(events)+1)]
        for i in reversed(xrange(len(events))):
            next_i = bisect.bisect_right(sorted_starts, events[i][1])-1
            for j in xrange(1, k+1):
                dp[i][j] = max(dp[i+1][j], dp[next_i+1][j-1]+events[i][2])
        return dp[0][-1]
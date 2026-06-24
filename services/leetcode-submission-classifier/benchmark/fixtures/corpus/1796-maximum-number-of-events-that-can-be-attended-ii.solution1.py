# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-events-that-can-be-attended-ii
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-events-that-can-be-attended-ii.py
# solution_class: Solution
# submission_id: 016fee101ff8003ef11e03a25a5520d9135c0463
# seed: 496183557

# Time:  O(nlogn + n * k)
# Space: O(n * k)

import bisect

class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        events.sort(key=lambda x: x[1])
        sorted_ends = [x[1] for x in events]
        dp = [[0]*(k+1) for _ in xrange(len(events)+1)]
        for i in xrange(1, len(events)+1):
            prev_i_m_1 = bisect.bisect_left(sorted_ends, events[i-1][0])-1
            for j in xrange(1, k+1):
                dp[i][j] = max(dp[i-1][j], dp[prev_i_m_1+1][j-1]+events[i-1][2])
        return dp[-1][-1]
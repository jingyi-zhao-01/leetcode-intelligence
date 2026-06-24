# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-score-of-non-overlapping-intervals
# source_path: LeetCode-Solutions-master/Python/maximum-score-of-non-overlapping-intervals.py
# solution_class: Solution
# submission_id: ee98ba2cbe79e1aa27382a38c8a54dd3160365b0
# seed: 2374148297

# Time:  O(nlogn + n * k^2)
# Space: O(n * k^2)

import bisect


# dp, binary search

class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        K = 4
        lookup = {}
        for i, (l, r, w) in enumerate(intervals):
            if (r, l, w) not in lookup:
                lookup[r, l, w] = i
        sorted_intervals = sorted(lookup.iterkeys(), key=lambda x: x[0])
        dp = [[[0, []] for _ in xrange(K+1)] for _ in xrange(len(sorted_intervals)+1)]
        for i in xrange(len(dp)-1):
            j = bisect.bisect_right(sorted_intervals, (sorted_intervals[i][1], 0, 0))-1
            idx = lookup[sorted_intervals[i]]
            for k in xrange(1, len(dp[i])):
                new_dp = [dp[j+1][k-1][0]-sorted_intervals[i][2], dp[j+1][k-1][1][:]]
                insort(new_dp[1], idx)
                dp[i+1][k] = min(dp[i][k], new_dp)
        return dp[len(sorted_intervals)][K][1]
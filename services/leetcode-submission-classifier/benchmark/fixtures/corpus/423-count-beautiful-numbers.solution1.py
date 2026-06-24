# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-beautiful-numbers
# source_path: LeetCode-Solutions-master/Python/count-beautiful-numbers.py
# solution_class: Solution
# submission_id: 85b4e40b46c22c23186db13eb3bb485e58df2d2e
# seed: 1817078885

# Time:  O(logr * 2 * 10 * s)
# Space: O(s) ~= O(2026), s = len(states)

import collections


# dp

class Solution(object):
    def beautifulNumbers(self, l, r):
        """
        :type l: int
        :type r: int
        :rtype: int
        """
        def count(x):
            s = map(lambda x: ord(x)-ord('0'), str(x))
            dp = [collections.defaultdict(int) for _ in xrange(2)]
            dp[1][1, 0] = 1
            for c in s:
                new_dp = [collections.defaultdict(int) for _ in xrange(2)]
                for b in xrange(2):
                    for (mul, total), cnt in dp[b].iteritems():
                        for x in xrange((c if b else 9)+1):
                            new_dp[b and x == c][mul*(1 if total == 0 == x else x), total+x] += cnt
                dp = new_dp
            result = 0
            for b in xrange(2):
                for (mul, total), cnt in dp[b].iteritems():
                    if total and mul%total == 0:
                        result += cnt
            return result

        return count(r)-count(l-1)
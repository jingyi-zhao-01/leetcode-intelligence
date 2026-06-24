# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-equal-length-runs
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-equal-length-runs.py
# solution_class: Solution
# submission_id: 78047722afccefba9c1b62d699876181fab48ee6
# seed: 1699513706

# Time:  O(n)
# Space: O(sqrt(n))

import collections


# freq table

class Solution(object):
    def maxSameLengthRuns(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = collections.defaultdict(int)
        l = 0
        for i in xrange(len(s)):
            l += 1
            if i+1 == len(s) or s[i+1] != s[i]:
                cnt[l] += 1
                l = 0
        return max(cnt.itervalues())
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-equal-length-runs
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-equal-length-runs.py
# solution_class: Solution2
# submission_id: 1d2268282fde1eff7d98730b9de1acf5ac41da8e
# seed: 1020415578

# Time:  O(n)
# Space: O(sqrt(n))

import collections


# freq table

class Solution2(object):
    def maxSameLengthRuns(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = [0]*(len(s)+1)
        l = 0
        for i in xrange(len(s)):
            l += 1
            if i+1 == len(s) or s[i+1] != s[i]:
                cnt[l] += 1
                l = 0
        return max(cnt)
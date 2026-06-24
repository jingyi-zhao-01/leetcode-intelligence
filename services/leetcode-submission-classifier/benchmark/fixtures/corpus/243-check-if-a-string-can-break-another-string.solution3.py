# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-a-string-can-break-another-string
# source_path: LeetCode-Solutions-master/Python/check-if-a-string-can-break-another-string.py
# solution_class: Solution3
# submission_id: a81dd2e9dfc5162e6d58aff8c0cb863f805df591
# seed: 4233564993

# Time:  O(n)
# Space: O(1)

import collections
import string

class Solution3(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1, s2 = sorted(s1), sorted(s2)
        return all(a >= b for a, b in itertools.izip(s1, s2)) or \
               all(a <= b for a, b in itertools.izip(s1, s2))
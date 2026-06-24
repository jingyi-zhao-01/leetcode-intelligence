# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-a-string-can-break-another-string
# source_path: LeetCode-Solutions-master/Python/check-if-a-string-can-break-another-string.py
# solution_class: Solution2
# submission_id: b215f281c6191409fd5cbeed1d22df68d2c0f2f8
# seed: 162116544

# Time:  O(n)
# Space: O(1)

import collections
import string

class Solution2(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return not {1, -1}.issubset(set(cmp(a, b) for a, b in itertools.izip(sorted(s1), sorted(s2))))
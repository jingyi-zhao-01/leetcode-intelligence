# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: permutation-in-string
# source_path: LeetCode-Solutions-master/Python/permutation-in-string.py
# solution_class: Solution
# submission_id: c1d39def0a025abec9dbf5df1111d12b089d8987
# seed: 919253579

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        counts = collections.Counter(s1)
        l = len(s1)
        for i in xrange(len(s2)):
            if counts[s2[i]] > 0:
                l -= 1
            counts[s2[i]] -= 1
            if l == 0:
                return True
            start = i + 1 - len(s1)
            if start >= 0:
                counts[s2[start]] += 1
                if counts[s2[start]] > 0:
                    l += 1
        return False
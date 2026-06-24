# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-strings-can-be-made-equal-with-operations-ii
# source_path: LeetCode-Solutions-master/Python/check-if-strings-can-be-made-equal-with-operations-ii.py
# solution_class: Solution
# submission_id: 01c83b0a5066d44531f194055451bb04d2244ca9
# seed: 1368037631

# Time:  O(n)
# Space: O(1)

import collections


# freq table

class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return all(collections.Counter(s1[j] for j in xrange(i, len(s1), 2)) == collections.Counter(s2[j] for j in xrange(i, len(s2), 2)) for i in xrange(2))
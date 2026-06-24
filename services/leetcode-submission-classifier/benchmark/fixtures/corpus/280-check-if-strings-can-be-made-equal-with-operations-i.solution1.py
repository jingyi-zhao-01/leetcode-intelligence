# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-strings-can-be-made-equal-with-operations-i
# source_path: LeetCode-Solutions-master/Python/check-if-strings-can-be-made-equal-with-operations-i.py
# solution_class: Solution
# submission_id: a9f967b92de4126f9b54698e4fa2ed8e3b0ff203
# seed: 3094704979

# Time:  O(1)
# Space: O(1)

import collections


# freq table

class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return all(collections.Counter(s1[j] for j in xrange(i, len(s1), 2)) == collections.Counter(s2[j] for j in xrange(i, len(s2), 2)) for i in xrange(2))
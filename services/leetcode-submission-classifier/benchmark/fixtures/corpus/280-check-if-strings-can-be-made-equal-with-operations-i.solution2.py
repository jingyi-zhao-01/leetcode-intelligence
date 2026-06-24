# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-strings-can-be-made-equal-with-operations-i
# source_path: LeetCode-Solutions-master/Python/check-if-strings-can-be-made-equal-with-operations-i.py
# solution_class: Solution2
# submission_id: ce9e054a72f655ae15f913502122f70c3fac1cff
# seed: 691601970

# Time:  O(1)
# Space: O(1)

import collections


# freq table

class Solution2(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return (((s1[0] == s2[0] and s1[2] == s2[2]) or (s1[0] == s2[2] and s1[2] == s2[0])) and
                ((s1[1] == s2[1] and s1[3] == s2[3]) or (s1[1] == s2[3] and s1[3] == s2[1])))
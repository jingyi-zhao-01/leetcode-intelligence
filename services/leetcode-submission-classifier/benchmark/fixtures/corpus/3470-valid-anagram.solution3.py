# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-anagram
# source_path: LeetCode-Solutions-master/Python/valid-anagram.py
# solution_class: Solution3
# submission_id: d8199863daac3186311d2aecd930391e011bcb50
# seed: 1551671197

# Time:  O(n)
# Space: O(1)

import collections

class Solution3(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-steps-to-make-two-strings-anagram
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-steps-to-make-two-strings-anagram.py
# solution_class: Solution
# submission_id: ba593c17d114bf42b949218b5e94ca2c0078d17d
# seed: 1827237546

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        diff = collections.Counter(s) - collections.Counter(t)
        return sum(diff.itervalues())
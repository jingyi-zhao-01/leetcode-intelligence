# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-all-characters-have-equal-number-of-occurrences
# source_path: LeetCode-Solutions-master/Python/check-if-all-characters-have-equal-number-of-occurrences.py
# solution_class: Solution
# submission_id: e077901b04eabac4598bdcfd33d9bbc69a961f53
# seed: 2797624232

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return len(set(collections.Counter(s).itervalues())) == 1
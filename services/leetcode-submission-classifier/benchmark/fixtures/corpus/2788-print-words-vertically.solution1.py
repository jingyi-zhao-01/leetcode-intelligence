# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: print-words-vertically
# source_path: LeetCode-Solutions-master/Python/print-words-vertically.py
# solution_class: Solution
# submission_id: b1d1f1465774c8e56d41d4f833919027866b6524
# seed: 1639568928

# Time:  O(n)
# Space: O(n)

import itertools

class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return ["".join(c).rstrip() for c in itertools.izip_longest(*s.split(), fillvalue=' ')]
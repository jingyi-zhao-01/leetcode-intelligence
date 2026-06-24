# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: string-transforms-into-another-string
# source_path: LeetCode-Solutions-master/Python/string-transforms-into-another-string.py
# solution_class: Solution
# submission_id: 80f8f66502160a85e7669a6cafe33331e728ee87
# seed: 2264620421

# Time:  O(n)
# Space: O(1)

import itertools

class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        if str1 == str2:
            return True
        lookup = {}
        for i, j in itertools.izip(str1, str2):
            if lookup.setdefault(i, j) != j:
                return False
        return len(set(str2)) < 26
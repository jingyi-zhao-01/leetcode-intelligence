# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-common-characters
# source_path: LeetCode-Solutions-master/Python/find-common-characters.py
# solution_class: Solution
# submission_id: 09a9584539006d06cca8375a0b996ea9377625ce
# seed: 1561189159

# Time:  O(n * l)
# Space: O(1)

import collections

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        result = collections.Counter(A[0])
        for a in A:
            result &= collections.Counter(a)
        return list(result.elements())
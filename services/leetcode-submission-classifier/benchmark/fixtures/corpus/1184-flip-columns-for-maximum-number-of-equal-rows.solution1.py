# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: flip-columns-for-maximum-number-of-equal-rows
# source_path: LeetCode-Solutions-master/Python/flip-columns-for-maximum-number-of-equal-rows.py
# solution_class: Solution
# submission_id: c1b2c07a83cfe867b1ed8b273a7f9f003f6998dc
# seed: 2912250938

# Time:  O(m * n)
# Space: O(m * n)

import collections

class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        count = collections.Counter(tuple(x^row[0] for x in row)
                                          for row in matrix)
        return max(count.itervalues())
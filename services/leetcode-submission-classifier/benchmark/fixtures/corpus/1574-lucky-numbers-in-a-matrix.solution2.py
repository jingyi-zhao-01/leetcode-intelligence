# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lucky-numbers-in-a-matrix
# source_path: LeetCode-Solutions-master/Python/lucky-numbers-in-a-matrix.py
# solution_class: Solution2
# submission_id: 942ce8c7cce2281e3e6497d4277cbbd587e03ce1
# seed: 2598385799

# Time:  O(m * n)
# Space: O(m + n)

import itertools

class Solution2(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return list(set(map(min, matrix)) &
                    set(map(max, itertools.izip(*matrix))))
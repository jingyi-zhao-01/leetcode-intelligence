# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: diagonal-traverse-ii
# source_path: LeetCode-Solutions-master/Python/diagonal-traverse-ii.py
# solution_class: Solution2
# submission_id: 7cb6092052ba423c14026ff927520d23b85dd815
# seed: 1936977536

# Time:  O(m * n)
# Space: O(m)

import itertools
import collections

class Solution2(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        result = []
        for r, row in enumerate(nums):
            for c, num in enumerate(row):
                if len(result) <= r+c:
                    result.append([])
                result[r+c].append(num)
        return [num for row in result for num in reversed(row)]
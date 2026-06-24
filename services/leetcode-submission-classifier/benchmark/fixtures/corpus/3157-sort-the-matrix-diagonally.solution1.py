# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-the-matrix-diagonally
# source_path: LeetCode-Solutions-master/Python/sort-the-matrix-diagonally.py
# solution_class: Solution
# submission_id: 406d9cb5a5d696242ddcc58f4fe8bccb4a854400
# seed: 421876118

# Time:  O(m * n * log(min(m, n))
# Space: O(m * n)

import collections

class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        lookup = collections.defaultdict(list)
        for i in xrange(len(mat)):
            for j in xrange(len(mat[0])):
                lookup[i-j].append(mat[i][j])
        for v in lookup.itervalues():
            v.sort()
        for i in reversed(xrange(len(mat))):
            for j in reversed(xrange(len(mat[0]))):
                mat[i][j] = lookup[i-j].pop()
        return mat
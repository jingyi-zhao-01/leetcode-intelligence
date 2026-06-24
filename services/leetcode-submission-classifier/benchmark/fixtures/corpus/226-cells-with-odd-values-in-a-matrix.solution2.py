# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: cells-with-odd-values-in-a-matrix
# source_path: LeetCode-Solutions-master/Python/cells-with-odd-values-in-a-matrix.py
# solution_class: Solution2
# submission_id: 04d460f6785b03923f9f586df90887b1d64e2b41
# seed: 2319438836

# Time:  O(n + m)
# Space: O(n + m)

class Solution2(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        fn = lambda x: sum(count&1 for count in collections.Counter(x).itervalues())
        row_sum, col_sum = map(fn, itertools.izip(*indices))
        return row_sum*m+col_sum*n-2*row_sum*col_sum
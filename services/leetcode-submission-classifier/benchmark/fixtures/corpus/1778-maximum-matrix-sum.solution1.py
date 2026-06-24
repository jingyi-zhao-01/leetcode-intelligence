# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-matrix-sum
# source_path: LeetCode-Solutions-master/Python/maximum-matrix-sum.py
# solution_class: Solution
# submission_id: 35b5da6312c03cb09ea2a05dee8233363c728fe8
# seed: 4085760416

# Time:  O(n^2)
# Space: O(1)

class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        abs_total = sum(abs(x) for row in matrix for x in row)
        min_abs_val = min(abs(x) for row in matrix for x in row)
        neg_cnt = sum(x < 0 for row in matrix for x in row)
        return abs_total if neg_cnt%2 == 0 else abs_total - 2*min_abs_val
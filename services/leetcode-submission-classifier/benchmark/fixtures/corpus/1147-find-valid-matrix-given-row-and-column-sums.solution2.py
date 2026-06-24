# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-valid-matrix-given-row-and-column-sums
# source_path: LeetCode-Solutions-master/Python/find-valid-matrix-given-row-and-column-sums.py
# solution_class: Solution2
# submission_id: 3bc3fe8e695225216a073bea6ab4f312d9a4cba4
# seed: 190669813

# Time:  O(m + n), excluding ctor of result
# Space: O(1)

# optimized from Solution2 since we can find next i, j pair without nested loops

class Solution2(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        matrix = [[0]*len(colSum) for _ in xrange(len(rowSum))]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                matrix[i][j] = min(rowSum[i], colSum[j])  # greedily used
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]
        return matrix
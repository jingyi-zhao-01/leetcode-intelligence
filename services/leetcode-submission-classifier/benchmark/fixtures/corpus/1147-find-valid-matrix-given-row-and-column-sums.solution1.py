# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-valid-matrix-given-row-and-column-sums
# source_path: LeetCode-Solutions-master/Python/find-valid-matrix-given-row-and-column-sums.py
# solution_class: Solution
# submission_id: d64c32ba4a38a5648445a367d48eeeb0959c7339
# seed: 2433045874

# Time:  O(m + n), excluding ctor of result
# Space: O(1)

# optimized from Solution2 since we can find next i, j pair without nested loops

class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        matrix = [[0]*len(colSum) for _ in xrange(len(rowSum))]
        i = j = 0
        while i < len(matrix) and j < len(matrix[0]):
            matrix[i][j] = min(rowSum[i], colSum[j])  # greedily used
            rowSum[i] -= matrix[i][j]
            colSum[j] -= matrix[i][j]
            if not rowSum[i]:  # won't be used in row i, ++i
                i += 1
            if not colSum[j]:  # won't be used in col j, ++j
                j += 1
        return matrix
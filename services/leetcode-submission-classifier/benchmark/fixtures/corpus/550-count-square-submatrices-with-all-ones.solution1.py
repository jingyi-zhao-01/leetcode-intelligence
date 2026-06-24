# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-square-submatrices-with-all-ones
# source_path: LeetCode-Solutions-master/Python/count-square-submatrices-with-all-ones.py
# solution_class: Solution
# submission_id: 0fb076559d3ef679019b2629aed2b2dd63b561b7
# seed: 3529906492

# Time:  O(m * n)
# Space: O(1)

class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        for i in xrange(1, len(matrix)):
            for j in xrange(1, len(matrix[0])):
                if not matrix[i][j]:
                    continue
                l = min(matrix[i-1][j], matrix[i][j-1])
                matrix[i][j] = l+1 if matrix[i-l][j-l] else l
        return sum(x for row in matrix for x in row)
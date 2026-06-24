# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: image-smoother
# source_path: LeetCode-Solutions-master/Python/image-smoother.py
# solution_class: Solution
# submission_id: 1b53b5ad410a775f59c42a7a1edd39a0886daa8b
# seed: 1893793216

# Time:  O(m * n)
# Space: O(1)

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        def getGray(M, i, j):
            total, count = 0, 0.0
            for r in xrange(-1, 2):
                for c in xrange(-1, 2):
                    ii, jj = i + r, j + c
                    if 0 <= ii < len(M) and 0 <= jj < len(M[0]):
                        total += M[ii][jj]
                        count += 1.0
            return int(total / count)

        result = [[0 for _ in xrange(len(M[0]))] for _ in xrange(len(M))]
        for i in xrange(len(M)):
            for j in xrange(len(M[0])):
                result[i][j] = getGray(M, i, j)
        return result
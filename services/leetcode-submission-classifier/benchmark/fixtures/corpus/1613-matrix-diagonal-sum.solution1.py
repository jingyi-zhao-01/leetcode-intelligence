# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: matrix-diagonal-sum
# source_path: LeetCode-Solutions-master/Python/matrix-diagonal-sum.py
# solution_class: Solution
# submission_id: 31d26abc5590f88aaaacc49630f020a23a29abfa
# seed: 254190059

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        return sum(mat[i][i]+mat[~i][i] for i in xrange(len(mat))) - (mat[len(mat)//2][len(mat)//2] if len(mat)%2 == 1 else 0)
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: determine-whether-matrix-can-be-obtained-by-rotation
# source_path: LeetCode-Solutions-master/Python/determine-whether-matrix-can-be-obtained-by-rotation.py
# solution_class: Solution
# submission_id: 312a2968c8d0d01de9366244f9ee64ca4ea15fad
# seed: 1029083441

# Time:  O(m * n)
# Space: O(1)

class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        checks = [lambda i, j: mat[i][j] == target[i][j],
                  lambda i, j: mat[i][j] == target[j][-1-i],
                  lambda i, j: mat[i][j] == target[-1-i][-1-j],
                  lambda i, j: mat[i][j] == target[-1-j][i]]
        traverse = lambda check: all(check(i, j) for i in xrange(len(mat)) for j in xrange(len(mat[0])))
        return any(traverse(check) for check in checks)
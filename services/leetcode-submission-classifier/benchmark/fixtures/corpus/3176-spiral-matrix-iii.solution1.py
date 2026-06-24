# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: spiral-matrix-iii
# source_path: LeetCode-Solutions-master/Python/spiral-matrix-iii.py
# solution_class: Solution
# submission_id: cad05acb9189ee04a8f26d3484afca768b8faab4
# seed: 3599209298

# Time:  O(max(m, n)^2)
# Space: O(1)

class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        r, c = r0, c0
        result = [[r, c]]
        x, y, n, i = 0, 1, 0, 0
        while len(result) < R*C:
            r, c, i = r+x, c+y, i+1
            if 0 <= r < R and 0 <= c < C:
                result.append([r, c])
            if i == n//2+1:
                x, y, n, i = y, -x, n+1, 0
        return result
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-increasing-path-in-a-matrix
# source_path: LeetCode-Solutions-master/Python/longest-increasing-path-in-a-matrix.py
# solution_class: Solution
# submission_id: 63fe18d8a268c89107b2f4a0671eead027182dc9
# seed: 4132732530

# Time:  O(m * n)
# Space: O(m * n)

# topological sort solution

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        if not matrix:
            return 0
        
        in_degree = [[0]*len(matrix[0]) for _ in xrange(len(matrix))]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if not (0 <= ni < len(matrix) and
                            0 <= nj < len(matrix[0]) and
                            matrix[ni][nj] > matrix[i][j]):
                        continue
                    in_degree[i][j] += 1
        q = []
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if not in_degree[i][j]:
                    q.append((i, j))
        result = 0
        while q:
            new_q = []
            for i, j in q:
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if not (0 <= ni < len(matrix) and
                            0 <= nj < len(matrix[0]) and
                            matrix[i][j] > matrix[ni][nj]):
                        continue
                    in_degree[ni][nj] -= 1
                    if not in_degree[ni][nj]:
                        new_q.append((ni, nj))
            q = new_q
            result += 1         
        return result
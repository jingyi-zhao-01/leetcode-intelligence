# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: pacific-atlantic-water-flow
# source_path: LeetCode-Solutions-master/Python/pacific-atlantic-water-flow.py
# solution_class: Solution
# submission_id: 471e4b1507b996acb962319da5d644d414b5ba51
# seed: 2669823989

# Time:  O(m * n)
# Space: O(m * n)

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        PACIFIC, ATLANTIC = 1, 2

        def pacificAtlanticHelper(matrix, x, y, prev_height, prev_val, visited, res):
            if (not 0 <= x < len(matrix)) or \
               (not 0 <= y < len(matrix[0])) or \
               matrix[x][y] < prev_height or \
               (visited[x][y] | prev_val) == visited[x][y]:
                return

            visited[x][y] |= prev_val
            if visited[x][y] == (PACIFIC | ATLANTIC):
                res.append((x, y))

            for d in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                pacificAtlanticHelper(matrix, x + d[0], y + d[1], matrix[x][y], visited[x][y], visited, res)

        if not matrix:
            return []

        res = []
        m, n = len(matrix),len(matrix[0])
        visited = [[0 for _ in xrange(n)] for _ in xrange(m)]

        for i in xrange(m):
            pacificAtlanticHelper(matrix, i, 0, float("-inf"), PACIFIC, visited, res)
            pacificAtlanticHelper(matrix, i, n - 1, float("-inf"), ATLANTIC, visited, res)
        for j in xrange(n):
            pacificAtlanticHelper(matrix, 0, j, float("-inf"), PACIFIC, visited, res)
            pacificAtlanticHelper(matrix, m - 1, j, float("-inf"), ATLANTIC, visited, res)

        return res
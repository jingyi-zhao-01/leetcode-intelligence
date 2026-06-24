# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-increasing-paths-in-a-grid
# source_path: LeetCode-Solutions-master/Python/number-of-increasing-paths-in-a-grid.py
# solution_class: Solution
# submission_id: 0ada2ca1ad33ea925dfa8dc52fa8565da198d2a8
# seed: 4246621847

# Time:  O(m * n)
# Space: O(m * n)

# topological sort, bottom-up dp

class Solution(object):
    def countPaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        in_degree = [[0]*len(grid[0]) for _ in xrange(len(grid))]
        q = []
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[i][j] > grid[ni][nj]:
                        in_degree[i][j] += 1
                if not in_degree[i][j]:
                    q.append((i, j))
        dp = [[1]*len(grid[0]) for _ in xrange(len(grid))]
        result = 0
        while q:
            new_q = []
            for i, j in q:
                result = (result+dp[i][j])%MOD
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if not (0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[i][j] < grid[ni][nj]):
                        continue
                    dp[ni][nj] = (dp[ni][nj]+dp[i][j])%MOD
                    in_degree[ni][nj] -= 1
                    if not in_degree[ni][nj]:
                        new_q.append((ni, nj))
            q = new_q
        return result
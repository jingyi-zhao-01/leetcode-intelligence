# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-increasing-paths-in-a-grid
# source_path: LeetCode-Solutions-master/Python/number-of-increasing-paths-in-a-grid.py
# solution_class: Solution2
# submission_id: e55ce634d963adb4354a8d094a675cf0c29fdda1
# seed: 236036659

# Time:  O(m * n)
# Space: O(m * n)

# topological sort, bottom-up dp

class Solution2(object):
    def countPaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def memoization(grid, i, j, lookup):
            if not lookup[i][j]:
                lookup[i][j] = 1
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[i][j] < grid[ni][nj]:
                        lookup[i][j] = (lookup[i][j]+memoization(grid, ni, nj, lookup)) % MOD
            return lookup[i][j]

        lookup = [[0]*len(grid[0]) for _ in xrange(len(grid))]
        return sum(memoization(grid, i, j, lookup) for i in xrange(len(grid)) for j in xrange(len(grid[0]))) % MOD
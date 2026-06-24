# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-fish-in-a-grid
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-fish-in-a-grid.py
# solution_class: Solution
# submission_id: 21d85e6d8e3b947ac6bf349c88ebce546b29d6bc
# seed: 3797298632

# Time:  O(m * n)
# Space: O(m + n)

# bfs

class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        def bfs(i, j):
            result = grid[i][j]
            grid[i][j] = 0
            q = [(i, j)]
            while q:
                new_q = []
                for i, j in q:
                    for di, dj in DIRECTIONS:
                        ni, nj = i+di, j+dj
                        if not (0 <= ni < len(grid) and
                                0 <= nj < len(grid[0]) and
                                grid[ni][nj]):
                            continue
                        result += grid[ni][nj]
                        grid[ni][nj] = 0
                        new_q.append((ni, nj))
                q = new_q
            return result

        result = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j]:
                    result = max(result, bfs(i, j))
        return result
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-fish-in-a-grid
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-fish-in-a-grid.py
# solution_class: Solution2
# submission_id: 6c588a180ff69a18969a15325a6edb031fbab254
# seed: 2270802633

# Time:  O(m * n)
# Space: O(m + n)

# bfs

class Solution2(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        def dfs(i, j):
            result = grid[i][j]
            grid[i][j] = 0
            stk = [(i, j)]
            while stk:
                i, j = stk.pop()
                for di, dj in reversed(DIRECTIONS):
                    ni, nj = i+di, j+dj
                    if not (0 <= ni < len(grid) and
                            0 <= nj < len(grid[0]) and
                            grid[ni][nj]):
                        continue
                    result += grid[ni][nj]
                    grid[ni][nj] = 0
                    stk.append((ni, nj))
            return result

        result = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j]:
                    result = max(result, dfs(i, j))
        return result
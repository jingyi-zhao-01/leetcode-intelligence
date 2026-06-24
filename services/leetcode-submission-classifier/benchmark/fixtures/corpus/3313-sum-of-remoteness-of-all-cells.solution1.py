# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-remoteness-of-all-cells
# source_path: LeetCode-Solutions-master/Python/sum-of-remoteness-of-all-cells.py
# solution_class: Solution
# submission_id: a49a33fb5a99e9c589734d3b7e6f8e00e28eea15
# seed: 3041818946

# Time:  O(n^2)
# Space: O(n^2)

# flood fill, bfs, math

class Solution(object):
    def sumRemoteness(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        def bfs(i, j):
            total, cnt = grid[i][j], 1
            grid[i][j] = -1
            q = [(i, j)]
            while q:
                new_q = []
                for i, j in q:
                    for di, dj in DIRECTIONS:
                        ni, nj = i+di, j+dj
                        if not (0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] != -1):
                            continue
                        total += grid[ni][nj]
                        cnt += 1
                        grid[ni][nj] = -1
                        new_q.append((ni, nj))
                q = new_q
            return total, cnt
    
        groups = [bfs(i, j) for i in xrange(len(grid)) for j in xrange(len(grid[0])) if grid[i][j] != -1]
        total = sum(t for t, _ in groups)
        return sum((total-t)*c for t, c in groups)
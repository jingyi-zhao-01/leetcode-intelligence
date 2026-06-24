# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-islands-with-total-value-divisible-by-k
# source_path: LeetCode-Solutions-master/Python/count-islands-with-total-value-divisible-by-k.py
# solution_class: Solution
# submission_id: cbaadee222ff0a5a44c94b66b2bfb1a81d829357
# seed: 4149476950

# Time:  O(m * n)
# Space: O(m + n)

# bfs, flood fill

class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        def bfs(i, j):
            if not grid[i][j]:
                return False
            total = grid[i][j]%k
            grid[i][j] = 0
            q = [(i, j)]
            while q:
                new_q = []
                for i, j in q:
                    for di, dj in DIRECTIONS:
                        ni, nj = i+di, j+dj
                        if not (0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj]):
                            continue
                        total = (total+grid[ni][nj])%k
                        grid[ni][nj] = 0
                        new_q.append((ni, nj))
                q = new_q
            return total == 0

        return sum(bfs(i, j) for i in xrange(len(grid)) for j in xrange(len(grid[0])))
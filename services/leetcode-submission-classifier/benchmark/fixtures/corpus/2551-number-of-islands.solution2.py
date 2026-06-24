# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-islands
# source_path: LeetCode-Solutions-master/Python/number-of-islands.py
# solution_class: Solution2
# submission_id: e3e16d375799f097ca252fbbc225a2e8431feccb
# seed: 1087709505

# Time:  O(m * n * α(m * n)) ~= O(m * n)
# Space: O(m * n)

class UnionFind(object):
    def __init__(self, n):
        self.set = range(n)
        self.count = n

    def find_set(self, x):
       if self.set[x] != x:
           self.set[x] = self.find_set(self.set[x])  # path compression.
       return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root != y_root:
            self.set[min(x_root, y_root)] = max(x_root, y_root)
            self.count -= 1

class Solution2(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(grid, i, j):
            if grid[i][j] == '0':
                return False
            grid[i][j] = '0'
            stk = [(i, j)]
            while stk:
                r, c = stk.pop()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if not (0 <= nr < len(grid) and
                            0 <= nc < len(grid[0]) and
                            grid[nr][nc] == '1'):
                        continue
                    grid[nr][nc] = '0'
                    stk.append((nr, nc))
            return True

        count = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if dfs(grid, i, j):
                    count += 1
        return count
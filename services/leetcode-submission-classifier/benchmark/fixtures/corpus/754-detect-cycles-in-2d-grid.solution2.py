# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: detect-cycles-in-2d-grid
# source_path: LeetCode-Solutions-master/Python/detect-cycles-in-2d-grid.py
# solution_class: Solution2
# submission_id: 8b705f80771ab87f8e845d493669bdae6aadc2e3
# seed: 2082065247

# Time:  O(m * n * α(n)) ~= O(m * n)
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
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if not grid[i][j]:
                    continue
                val = grid[i][j]
                q = [(i, j)]
                while q:
                    new_q = []
                    for r, c in q:
                        if not grid[r][c]:
                            return True
                        grid[r][c] = 0
                        for dr, dc in directions:
                            nr, nc = r+dr, c+dc
                            if not (0 <= nr < len(grid) and
                                    0 <= nc < len(grid[0]) and
                                    grid[nr][nc] == val):
                                continue
                            new_q.append((nr, nc))
                    q = new_q
        return False
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-islands
# source_path: LeetCode-Solutions-master/Python/number-of-islands.py
# solution_class: Solution3
# submission_id: 41cf71b19afb20abdce1ee5d0e72f69b9c287d5d
# seed: 296938207

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

class Solution3(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def bfs(grid, i, j):
            if grid[i][j] == '0':
                return False
            grid[i][j] ='0'
            q = collections.deque([(i, j)])
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if not (0 <= nr < len(grid) and
                            0 <= nc < len(grid[0]) and
                            grid[nr][nc] == '1'):
                        continue
                    grid[nr][nc] = '0'
                    q.append((nr, nc))
            return True

        count = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if bfs(grid, i, j):
                    count += 1
        return count
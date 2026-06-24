# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-islands
# source_path: LeetCode-Solutions-master/Python/number-of-islands.py
# solution_class: Solution
# submission_id: f05b7a07c650940827f3a8195f9a716faffbbf46
# seed: 55295086

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

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def index(n, i, j):
            return i*n + j
    
        if not grid:
            return 0

        zero_count = 0
        union_find = UnionFind(len(grid)*len(grid[0]))
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == '1':
                    if i and grid[i-1][j] == '1':
                        union_find.union_set(index(len(grid[0]), i-1, j),
                                             index(len(grid[0]),i, j))
                    if j and grid[i][j-1] == '1':
                        union_find.union_set(index(len(grid[0]), i, j-1),
                                             index(len(grid[0]), i, j))
                else:
                    zero_count += 1        
        return union_find.count-zero_count
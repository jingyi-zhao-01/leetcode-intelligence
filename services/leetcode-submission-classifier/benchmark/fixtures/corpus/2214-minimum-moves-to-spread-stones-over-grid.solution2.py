# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-moves-to-spread-stones-over-grid
# source_path: LeetCode-Solutions-master/Python/minimum-moves-to-spread-stones-over-grid.py
# solution_class: Solution2
# submission_id: 2075811f8b24e5c3e719b14abe3deffa79f71a3f
# seed: 1699505301

# Time:  O(max(x^2 * y)) = O(n^3), n = len(grid)*len(grid[0]), y = len(zero), x = n-y
# Space: O(max(x^2)) = O(n^2)

# weighted bipartite matching solution

class Solution2(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dist(a, b):
            return abs(a[0]-b[0])+abs(a[1]-b[1])

        src, dst = [], []
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j]-1 >= 0:
                    src.extend([(i, j)]*(grid[i][j]-1))
                else:
                    dst.append((i, j))
        adj = [[dist(src[i], dst[j]) for j in xrange(len(dst))] for i in xrange(len(src))]
        return sum(adj[i][j] for i, j in itertools.izip(*hungarian(adj)))    
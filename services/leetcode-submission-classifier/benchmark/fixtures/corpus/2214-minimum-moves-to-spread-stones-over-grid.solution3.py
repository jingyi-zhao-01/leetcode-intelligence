# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-moves-to-spread-stones-over-grid
# source_path: LeetCode-Solutions-master/Python/minimum-moves-to-spread-stones-over-grid.py
# solution_class: Solution3
# submission_id: b5714722d7aec5c0349ee2cfa786465ac953633f
# seed: 3711865782

# Time:  O(max(x^2 * y)) = O(n^3), n = len(grid)*len(grid[0]), y = len(zero), x = n-y
# Space: O(max(x^2)) = O(n^2)

# weighted bipartite matching solution

class Solution3(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dist(a, b):
            return abs(a[0]-b[0])+abs(a[1]-b[1])

        def backtracking(curr):
            if curr == len(zero):
                return 0
            result = float("inf")
            i, j = zero[curr]
            for ni in xrange(len(grid)):
                for nj in xrange(len(grid[0])):
                    if not (grid[ni][nj] >= 2):
                        continue
                    grid[ni][nj] -= 1
                    result = min(result, dist((i, j), (ni, nj))+backtracking(curr+1))
                    grid[ni][nj] += 1
            return result

        zero = [(i, j) for i in xrange(len(grid)) for j in xrange(len(grid[0])) if grid[i][j] == 0]
        return backtracking(0)
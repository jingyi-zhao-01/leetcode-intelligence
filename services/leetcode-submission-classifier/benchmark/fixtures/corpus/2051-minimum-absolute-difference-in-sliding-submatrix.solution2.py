# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-absolute-difference-in-sliding-submatrix
# source_path: LeetCode-Solutions-master/Python/minimum-absolute-difference-in-sliding-submatrix.py
# solution_class: Solution2
# submission_id: 7065c1baf3633b6b2956788715cb422b78e94e13
# seed: 1283486317

# Time:  O(m * n * k^2)
# Space: O(k^2)

from sortedcontainers import SortedList


# two pointers, sliding window, sorted List

class Solution2(object):
    def minAbsDiff(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        result = [[-1]*(len(grid[0])-(k-1)) for _ in xrange(len(grid)-(k-1))]
        for i in xrange(len(grid)-(k-1)):
            for j in xrange(len(grid[0])-(k-1)):
                vals = sorted({grid[i+di][j+dj] for di in xrange(k) for dj in xrange(k)})
                result[i][j] = min(vals[x+1]-vals[x] for x in xrange(len(vals)-1)) if len(vals) != 1 else 0
        return result
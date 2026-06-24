# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: right-triangles
# source_path: LeetCode-Solutions-master/Python/right-triangles.py
# solution_class: Solution
# submission_id: 44c9ffb4dd683a9165c59c8c283eb893295a3094
# seed: 4198780893

# Time:  O(n * m)
# Space: O(min(n, m))

# combinatorics

class Solution(object):
    def numberOfRightTriangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def get(i, j):
            return grid[i][j] if n < m else grid[j][i]

        n, m = len(grid), len(grid[0])
        result = 0
        cnt1 = [sum(get(i, j) for j in xrange(max(n, m))) for i in xrange(min(n, m))]
        for j in xrange(max(n, m)):
            cnt2 = sum(get(i, j) for i in xrange(min(n, m)))
            result += sum((cnt1[i]-1)*(cnt2-1) for i in xrange(min(n, m)) if get(i, j))
        return result
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: right-triangles
# source_path: LeetCode-Solutions-master/Python/right-triangles.py
# solution_class: Solution2
# submission_id: eccf22f3669655ef3f40a07d46779051954fbf91
# seed: 3077604646

# Time:  O(n * m)
# Space: O(min(n, m))

# combinatorics

class Solution2(object):
    def numberOfRightTriangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        cnt1 = [sum(grid[i][j] for j in xrange(m)) for i in xrange(n)]
        cnt2 = [sum(grid[i][j] for i in xrange(n)) for j in xrange(m)]
        return sum((cnt1[i]-1)*(cnt2[j]-1) for i in xrange(n) for j in xrange(m) if grid[i][j])
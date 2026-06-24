# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: where-will-the-ball-fall
# source_path: LeetCode-Solutions-master/Python/where-will-the-ball-fall.py
# solution_class: Solution
# submission_id: aa7ba64e2d97f5cca1fe16b520840e06d5724c75
# seed: 309477908

# Time:  O(m * n)
# Space: O(1)

class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        result = []
        for c in xrange(len(grid[0])):
            for r in xrange(len(grid)):
                nc = c+grid[r][c]
                if not (0 <= nc < len(grid[0]) and grid[r][nc] == grid[r][c]):
                    c = -1
                    break
                c = nc
            result.append(c)
        return result
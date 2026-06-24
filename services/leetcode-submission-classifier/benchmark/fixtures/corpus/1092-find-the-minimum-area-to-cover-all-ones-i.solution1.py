# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-minimum-area-to-cover-all-ones-i
# source_path: LeetCode-Solutions-master/Python/find-the-minimum-area-to-cover-all-ones-i.py
# solution_class: Solution
# submission_id: 8d2b67fb920d2a74f09e1198e1d75b755fbd482a
# seed: 2990395496

# Time:  O(n * m)
# Space: O(1)

# array

class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        min_r, max_r, min_c, max_c = len(grid), -1, len(grid[0]), -1
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                min_r, max_r, min_c, max_c = min(min_r, i), max(max_r, i), min(min_c, j), max(max_c, j)
        return (max_r-min_r+1)*(max_c-min_c+1)
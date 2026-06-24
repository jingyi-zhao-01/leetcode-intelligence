# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-minimum-area-to-cover-all-ones-ii
# source_path: LeetCode-Solutions-master/Python/find-the-minimum-area-to-cover-all-ones-ii.py
# solution_class: Solution6
# submission_id: 3bd77b6fd5b41ce02cfed04e67d82e23e79d02d9
# seed: 2030398388

# Time:  O(max(n, m)^2)
# Space: O(max(n, m)^2)

# dp

class Solution6(object):
    def minimumSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def minimumArea(min_i, max_i, min_j, max_j):
            min_r, max_r, min_c, max_c = max_i+1, min_i-1, max_j+1, min_j-1
            for i in xrange(min_i, max_i+1):
                for j in xrange(min_j, max_j+1):
                    if grid[i][j] == 0:
                        continue
                    min_r, max_r, min_c, max_c = min(min_r, i), max(max_r, i), min(min_c, j), max(max_c, j)
            return (max_r-min_r+1)*(max_c-min_c+1) if min_r <= max_i else 0
    
        result = float("inf")
        for i in xrange(len(grid)-1):
            a = minimumArea(i+1, len(grid)-1, 0, len(grid[0])-1)
            for j in xrange(len(grid[0])-1):
                b = minimumArea(0, i, 0, j)
                c = minimumArea(0, i, j+1, len(grid[0])-1)
                result = min(result, a+b+c)
        for i in xrange(len(grid)-1):
            a = minimumArea(0, i, 0, len(grid[0])-1)
            for j in xrange(len(grid[0])-1):
                b = minimumArea(i+1, len(grid)-1, 0, j)
                c = minimumArea(i+1, len(grid)-1, j+1, len(grid[0])-1)
                result = min(result, a+b+c)
        for j in xrange(len(grid[0])-1):
            a = minimumArea(0, len(grid)-1, j+1, len(grid[0])-1)
            for i in xrange(len(grid)-1):
                b = minimumArea(0, i, 0, j)
                c = minimumArea(i+1, len(grid)-1, 0, j)
                result = min(result, a+b+c)
        for j in xrange(len(grid[0])-1):
            a = minimumArea(0, len(grid)-1, 0, j)
            for i in xrange(len(grid)-1):
                b = minimumArea(0, i, j+1, len(grid[0])-1)
                c = minimumArea(i+1, len(grid)-1, j+1, len(grid[0])-1)
                result = min(result, a+b+c)
        for i in xrange(len(grid)-2):
            a = minimumArea(0, i, 0, len(grid[0])-1)
            for j in xrange(i+1, len(grid)-1):
                b = minimumArea(i+1, j, 0, len(grid[0])-1)
                c = minimumArea(j+1, len(grid)-1, 0, len(grid[0])-1)
                result = min(result, a+b+c)
        for i in xrange(len(grid[0])-2):
            a = minimumArea(0, len(grid)-1, 0, i)
            for j in xrange(i+1, len(grid[0])-1):
                b = minimumArea(0, len(grid)-1, i+1, j)
                c = minimumArea(0, len(grid)-1, j+1, len(grid[0])-1)
                result = min(result, a+b+c)
        return result
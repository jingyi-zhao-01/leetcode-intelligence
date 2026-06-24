# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-maximum-value-in-a-grid
# source_path: LeetCode-Solutions-master/Python/minimize-maximum-value-in-a-grid.py
# solution_class: Solution
# submission_id: dc5560b0b12115b62d8bd7d509adb2c2e705736b
# seed: 2836458764

# Time:  O((m * n) * log(m * n))
# Space: O(m * n)

# sort, greedy

class Solution(object):
    def minScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        idxs = [(i, j) for i in xrange(len(grid)) for j in xrange(len(grid[0]))]
        idxs.sort(key=lambda x: grid[x[0]][x[1]])
        row_max, col_max = [0]*len(grid), [0]*len(grid[0])
        for i, j in idxs:
            grid[i][j] = row_max[i] = col_max[j] = max(row_max[i], col_max[j])+1
        return grid
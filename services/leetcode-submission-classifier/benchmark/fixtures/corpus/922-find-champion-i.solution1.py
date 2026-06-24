# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-champion-i
# source_path: LeetCode-Solutions-master/Python/find-champion-i.py
# solution_class: Solution
# submission_id: a201feae1a0e1780d4d3fd5f53cada7fb7c17a35
# seed: 1199458936

# Time:  O(n^2)
# Space: O(1)

# array

class Solution(object):
    def findChampion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return next(u for u in xrange(len(grid)) if sum(grid[u]) == len(grid)-1)
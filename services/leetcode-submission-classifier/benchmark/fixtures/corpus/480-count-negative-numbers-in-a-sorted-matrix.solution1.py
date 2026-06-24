# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-negative-numbers-in-a-sorted-matrix
# source_path: LeetCode-Solutions-master/Python/count-negative-numbers-in-a-sorted-matrix.py
# solution_class: Solution
# submission_id: 0b0d36a0dbad38420af951deb30e5844e80d0251
# seed: 797958298

# Time:  O(m + n)
# Space: O(1)

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result, c = 0, len(grid[0])-1
        for row in grid:
            while c >= 0 and row[c] < 0:
                c -= 1
            result += len(grid[0])-1-c
        return result
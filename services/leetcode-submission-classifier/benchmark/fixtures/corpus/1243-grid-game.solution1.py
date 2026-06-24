# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: grid-game
# source_path: LeetCode-Solutions-master/Python/grid-game.py
# solution_class: Solution
# submission_id: 50886b8b3915bb952d837f8f8c6b09437d254116
# seed: 73563310

# Time:  O(n)
# Space: O(1)

import itertools

class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = float("inf")
        left, right = 0, sum(grid[0])
        for a, b in itertools.izip(grid[0], grid[1]):
            right -= a
            result = min(result, max(left, right))
            left += b
        return result
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: zigzag-grid-traversal-with-skip
# source_path: LeetCode-Solutions-master/Python/zigzag-grid-traversal-with-skip.py
# solution_class: Solution
# submission_id: 925e42302e53c9f17c33521c0b5d2e3ad0745359
# seed: 3908908412

# Time:  O(n * m)
# Space: O(1)

# array

class Solution(object):
    def zigzagTraversal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        result = []
        for i in xrange(len(grid)):
            if i%2 == 0:
                result.extend(grid[i][j] for j in xrange(0, len(grid[0]), 2))
            else:
                result.extend(grid[i][j] for j in reversed(xrange(1, len(grid[0]), 2)))
        return result
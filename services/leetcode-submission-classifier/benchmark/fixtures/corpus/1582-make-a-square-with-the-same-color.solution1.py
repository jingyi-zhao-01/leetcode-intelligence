# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-a-square-with-the-same-color
# source_path: LeetCode-Solutions-master/Python/make-a-square-with-the-same-color.py
# solution_class: Solution
# submission_id: f063359860705f028e747559ece56d47af3e6211
# seed: 1461787191

# Time:  O((n - w + 1)^2 * w^2)
# Space: O(1)

import collections


# array

class Solution(object):
    def canMakeSquare(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        N, W = 3, 2
        return any(max(collections.Counter(grid[i+h][j+w] for h in xrange(W) for w in xrange(W)).itervalues()) >= W**2-1
                   for i in xrange(N-W+1) for j in xrange(N-W+1))
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-path-in-binary-matrix
# source_path: LeetCode-Solutions-master/Python/shortest-path-in-binary-matrix.py
# solution_class: Solution
# submission_id: 06e0b85c9bab3d7e0c1a553a2f674c7dd4b2f7f6
# seed: 3994315555

# Time:  O(n^2)
# Space: O(n)

import collections

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [(-1, -1), (-1, 0), (-1, 1), \
                      ( 0, -1), ( 0, 1), \
                      ( 1, -1), ( 1, 0), ( 1, 1)]
        result = 0
        q = collections.deque([(0, 0)])
        while q:
            result += 1
            next_depth = collections.deque()
            while q:
                i, j = q.popleft()
                if 0 <= i < len(grid) and \
                   0 <= j < len(grid[0]) and \
                    not grid[i][j]:
                    grid[i][j] = 1
                    if i == len(grid)-1 and j == len(grid)-1:
                        return result
                    for d in directions:
                        next_depth.append((i+d[0], j+d[1]))
            q = next_depth
        return -1
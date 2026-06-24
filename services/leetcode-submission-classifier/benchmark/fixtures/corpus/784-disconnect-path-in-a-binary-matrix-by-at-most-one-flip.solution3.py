# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: disconnect-path-in-a-binary-matrix-by-at-most-one-flip
# source_path: LeetCode-Solutions-master/Python/disconnect-path-in-a-binary-matrix-by-at-most-one-flip.py
# solution_class: Solution3
# submission_id: e3e91ae746b27af9a0e80b01caa85eddd70feec1
# seed: 1173223990

# Time:  O(m * n)
# Space: O(m + n)

# dp

class Solution3(object):
    def isPossibleToCutPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        def dfs(i, j):
            if not (i < len(grid) and j < len(grid[0]) and grid[i][j]):
                return False
            if (i, j) == (len(grid)-1, len(grid[0])-1):
                return True
            if (i, j) != (0, 0):
                grid[i][j] = 0
            return dfs(i+1, j) or dfs(i, j+1)

        return not dfs(0, 0) or not dfs(0, 0)
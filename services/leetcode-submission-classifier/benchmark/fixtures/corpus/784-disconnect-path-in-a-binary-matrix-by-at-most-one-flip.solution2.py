# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: disconnect-path-in-a-binary-matrix-by-at-most-one-flip
# source_path: LeetCode-Solutions-master/Python/disconnect-path-in-a-binary-matrix-by-at-most-one-flip.py
# solution_class: Solution2
# submission_id: 4b944baf42d7d510c2b4317915dfc6f851cf1b0a
# seed: 1016664158

# Time:  O(m * n)
# Space: O(m + n)

# dp

class Solution2(object):
    def isPossibleToCutPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        def iter_dfs():
            stk = [(0, 0)]
            while stk:
                i, j = stk.pop()
                if not (i < len(grid) and j < len(grid[0]) and grid[i][j]):
                    continue
                if (i, j) == (len(grid)-1, len(grid[0])-1):
                    return True
                if (i, j) != (0, 0):
                    grid[i][j] = 0
                stk.append((i, j+1))
                stk.append((i+1, j))  
            return False

        return not iter_dfs() or not iter_dfs()
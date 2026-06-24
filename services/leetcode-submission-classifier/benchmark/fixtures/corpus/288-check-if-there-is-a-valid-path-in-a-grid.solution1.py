# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-there-is-a-valid-path-in-a-grid
# source_path: LeetCode-Solutions-master/Python/check-if-there-is-a-valid-path-in-a-grid.py
# solution_class: Solution
# submission_id: ba5bb4aa441f6b23eaacd7a69ffc72bb0bc267f7
# seed: 3534008322

# Time:  O(m * n)
# Space: O(1)

class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        E, S, W, N = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        directions = [
            [W, E], [N, S],
            [W, S], [S, E],
            [W, N], [N, E]
        ]

        for r, c in directions[grid[0][0]-1]:
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
                continue
            pr, pc = 0, 0
            while r != len(grid)-1 or c != len(grid[0])-1:
                for dx, dy in directions[grid[r][c]-1]:
                    nr, nc = r+dx, c+dy
                    if (nr == pr and nc == pc) or \
                       not(0 <= nr < len(grid) and 0 <= nc < len(grid[0])) or \
                       (-dx, -dy) not in directions[grid[nr][nc]-1]:
                        continue
                    pr, pc, r, c = r, c, nr, nc
                    break
                else:
                    return False
            return True
        return len(grid) == len(grid[0]) == 1 
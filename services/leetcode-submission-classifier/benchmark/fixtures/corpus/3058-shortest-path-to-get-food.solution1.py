# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-path-to-get-food
# source_path: LeetCode-Solutions-master/Python/shortest-path-to-get-food.py
# solution_class: Solution
# submission_id: e6335fd0438d9a0765cb4cb07537a9a07e092b03
# seed: 2153477251

# Time:  O(m * n)
# Space: O(m + n)

class Solution(object):
    def getFood(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        q = []
        for r in xrange(len(grid)):
            for c in xrange(len(grid[0])):
                if grid[r][c] == '*':
                    q.append((r, c))
                    break
        
        result = 0
        while q:
            result += 1
            new_q = []
            for r, c in q:
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if not (0 <= nr < len(grid) and
                            0 <= nc < len(grid[0]) and
                            grid[nr][nc] != 'X'):
                        continue
                    if grid[nr][nc] == '#':
                        return result
                    grid[nr][nc] = 'X'
                    new_q.append((nr, nc))
            q = new_q 
        return -1
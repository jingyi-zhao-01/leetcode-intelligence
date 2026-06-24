# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-make-at-least-one-valid-path-in-a-grid
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-make-at-least-one-valid-path-in-a-grid.py
# solution_class: Solution
# submission_id: f266f4163196b51f810c1bac720f19d324955e56
# seed: 2342834743

# Time:  O(m * n)
# Space: O(m * n)

# A* Search Algorithm without heap

class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def a_star(grid, b, t):
            f, dh = 0, 1
            closer, detour = [b], []
            lookup = set()
            while closer or detour:
                if not closer:
                    f += dh
                    closer, detour = detour, closer
                b = closer.pop()
                if b in lookup:
                    continue
                lookup.add(b)
                if b == t:
                    return f
                for nd, (dr, dc) in enumerate(directions, 1):
                    nb = (b[0]+dr, b[1]+dc)
                    if not (0 <= nb[0] < len(grid) and 0 <= nb[1] < len(grid[0]) and nb not in lookup):
                        continue
                    (closer if nd == grid[b[0]][b[1]] else detour).append(nb)
            return -1

        return a_star(grid, (0, 0), (len(grid)-1, len(grid[0])-1))
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-obstacle-removal-to-reach-corner
# source_path: LeetCode-Solutions-master/Python/minimum-obstacle-removal-to-reach-corner.py
# solution_class: Solution
# submission_id: 314d3925523d6f465e398ae4c499b9fd6bff2764
# seed: 999960810

# Time:  O(m * n)
# Space: O(m * n)

# A* Search Algorithm without heap

class Solution(object):
    def minimumObstacles(self, grid):
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
                for dr, dc in directions:
                    nb = (b[0]+dr, b[1]+dc)
                    if not (0 <= nb[0] < len(grid) and 0 <= nb[1] < len(grid[0]) and nb not in lookup):
                        continue
                    (closer if not grid[nb[0]][nb[1]] else detour).append(nb)
            return -1

        return a_star(grid, (0, 0), (len(grid)-1, len(grid[0])-1))
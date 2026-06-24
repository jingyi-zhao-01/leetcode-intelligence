# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: escape-the-spreading-fire
# source_path: LeetCode-Solutions-master/Python/escape-the-spreading-fire.py
# solution_class: Solution
# submission_id: 119e24ef8b6645d2bcce09922a3c4dee7e60a850
# seed: 2078272240

# Time:  O(m * n)
# Space: O(m * n)

import collections


# bfs

class Solution(object):
    def maximumMinutes(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        GRASS, FIRE, WALL, PERSON = range(4)
        INF = 10**9
        def bfs(grid):
            time = collections.defaultdict(int)
            d = 0
            q = [(r, c, FIRE) for r in xrange(len(grid)) for c in xrange(len(grid[0])) if grid[r][c] == FIRE]
            q.append((0, 0, PERSON))
            while q:
                new_q = []
                for r, c, t in q:
                    for dr, dc in DIRECTIONS:
                        nr, nc = r+dr, c+dc
                        if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and
                                grid[nr][nc] != WALL and
                                ((t == FIRE and grid[nr][nc] != FIRE) or
                                 (t == PERSON and (grid[nr][nc] == GRASS or (grid[nr][nc] == FIRE and (nr, nc) == (len(grid)-1, len(grid[0])-1) and d+1 == time[FIRE, nr, nc]))))):
                            continue
                        if grid[nr][nc] != FIRE:
                            grid[nr][nc] = t
                        if (nr, nc) in ((len(grid)-1, len(grid[0])-1), (len(grid)-1, len(grid[0])-2), (len(grid)-2, len(grid[0])-1)):
                            time[t, nr, nc] = d+1
                        new_q.append((nr, nc, t))
                q = new_q
                d += 1
            return time

        time = bfs(grid)
        if not time[PERSON, len(grid)-1, len(grid[0])-1]:
            return -1
        if not time[FIRE, len(grid)-1, len(grid[0])-1]:
            return INF
        diff = time[FIRE, len(grid)-1, len(grid[0])-1]-time[PERSON, len(grid)-1, len(grid[0])-1]
        return diff if diff+2 in (time[FIRE, len(grid)-1, len(grid[0])-2]-time[PERSON, len(grid)-1, len(grid[0])-2],
                                  time[FIRE, len(grid)-2, len(grid[0])-1]-time[PERSON, len(grid)-2, len(grid[0])-1]) else diff-1
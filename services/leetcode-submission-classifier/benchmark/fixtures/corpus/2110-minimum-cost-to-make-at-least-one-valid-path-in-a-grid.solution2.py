# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-make-at-least-one-valid-path-in-a-grid
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-make-at-least-one-valid-path-in-a-grid.py
# solution_class: Solution2
# submission_id: 6869c2b10990d4a5f5e5531eb11b507666e94f65
# seed: 3281368505

# Time:  O(m * n)
# Space: O(m * n)

# A* Search Algorithm without heap

class Solution2(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        b, t = (0, 0), (len(grid)-1, len(grid[0])-1)
        dq = collections.deque([(b, 0)])
        lookup = set()
        while dq:
            b, d = dq.popleft()
            if b in lookup:
                continue
            lookup.add(b)
            if b == t:
                return d
            for nd, (dr, dc) in enumerate(directions, 1):
                nb = (b[0]+dr, b[1]+dc)
                if not (0 <= nb[0] < len(grid) and 0 <= nb[1] < len(grid[0]) and nb not in lookup):
                    continue
                if nd == grid[b[0]][b[1]]:
                    dq.appendleft((nb, d))
                else:
                    dq.append((nb, d+1))
        return -1  # never reach here
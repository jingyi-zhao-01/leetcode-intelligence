# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-obstacle-removal-to-reach-corner
# source_path: LeetCode-Solutions-master/Python/minimum-obstacle-removal-to-reach-corner.py
# solution_class: Solution2
# submission_id: 3418c38602d4701e556250e7cb12b062bc312bc4
# seed: 3259436980

# Time:  O(m * n)
# Space: O(m * n)

# A* Search Algorithm without heap

class Solution2(object):
    def minimumObstacles(self, grid):
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
            for dr, dc in directions:
                nb = (b[0]+dr, b[1]+dc)
                if not (0 <= nb[0] < len(grid) and 0 <= nb[1] < len(grid[0]) and nb not in lookup):
                    continue
                if not grid[nb[0]][nb[1]]:
                    dq.appendleft((nb, d))
                else:
                    dq.append((nb, d+1))
        return -1  # never reach here
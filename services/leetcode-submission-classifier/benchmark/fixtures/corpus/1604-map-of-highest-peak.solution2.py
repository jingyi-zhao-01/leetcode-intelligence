# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: map-of-highest-peak
# source_path: LeetCode-Solutions-master/Python/map-of-highest-peak.py
# solution_class: Solution2
# submission_id: 5158f742a97365eb982d24cb52a7055172555c7c
# seed: 2326033406

# Time:  O(m * n)
# Space: O(m * n)

class Solution2(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q, heights = [], [[-1]*len(isWater[0]) for _ in xrange(len(isWater))]
        for r, row in enumerate(isWater):
            for c, cell in enumerate(row):
                if not cell:
                    continue
                heights[r][c] = 0
                q.append((r, c))
        while q:
            new_q = []
            for r, c in q:
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc 
                    if not (0 <= nr < len(isWater) and
                            0 <= nc < len(isWater[0]) and
                            heights[nr][nc] == -1):
                        continue
                    heights[nr][nc] = heights[r][c]+1
                    q.append((nr, nc))
            q = new_q
        return heights
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: map-of-highest-peak
# source_path: LeetCode-Solutions-master/Python/map-of-highest-peak.py
# solution_class: Solution
# submission_id: adcd45386af755659f5d259e30088097eee8fd77
# seed: 4105930731

# Time:  O(m * n)
# Space: O(m * n)

class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = []
        for r, row in enumerate(isWater):
            for c, cell in enumerate(row):
                row[c] -= 1
                if not cell:
                    continue
                q.append((r, c))
        while q:
            new_q = []
            for r, c in q:
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc 
                    if not (0 <= nr < len(isWater) and
                            0 <= nc < len(isWater[0]) and
                            isWater[nr][nc] == -1):
                        continue
                    isWater[nr][nc] = isWater[r][c]+1
                    q.append((nr, nc))
            q = new_q
        return isWater
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: multi-source-flood-fill
# source_path: LeetCode-Solutions-master/Python/multi-source-flood-fill.py
# solution_class: Solution
# submission_id: b44eee553ab0259a2c268e99a09e6552789fdc96
# seed: 991594379

# Time:  O(n * m)
# Space: O(n * m)

# bfs, flood fill

class Solution(object):
    def colorGrid(self, n, m, sources):
        """
        :type n: int
        :type m: int
        :type sources: List[List[int]]
        :rtype: List[List[int]]
        """
        DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        result = [[0]*m for _ in xrange(n)]
        q = []
        for r, c, color in sources:
            result[r][c] = color
            q.append((r, c))
        while q:
            new_q = []
            for r, c in q:
                for dr, dc in DIRECTIONS:
                    nr, nc = r+dr, c+dc
                    if not (0 <= nr < n and 0 <= nc < m):
                        continue
                    if result[nr][nc] == 0:
                        result[nr][nc] = -result[r][c]
                        new_q.append((nr, nc))
                    elif result[nr][nc] < 0:
                        result[nr][nc] = min(result[nr][nc], -result[r][c])
            for nr, nc in new_q:
                result[nr][nc] = -result[nr][nc]
            q = new_q
        return result
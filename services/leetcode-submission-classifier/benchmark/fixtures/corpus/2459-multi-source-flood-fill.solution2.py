# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: multi-source-flood-fill
# source_path: LeetCode-Solutions-master/Python/multi-source-flood-fill.py
# solution_class: Solution2
# submission_id: f70c66d469e8a4c0da5f15a14e763e35e1a4b396
# seed: 83122444

# Time:  O(n * m)
# Space: O(n * m)

# bfs, flood fill

class Solution2(object):
    def colorGrid(self, n, m, sources):
        """
        :type n: int
        :type m: int
        :type sources: List[List[int]]
        :rtype: List[List[int]]
        """
        DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        sources.sort(key=lambda x: -x[2])
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
                    if not (0 <= nr < n and 0 <= nc < m and result[nr][nc] == 0):
                        continue
                    result[nr][nc] = result[r][c]
                    new_q.append((nr, nc))
            q = new_q
        return result
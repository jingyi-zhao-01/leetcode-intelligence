# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: path-with-minimum-effort
# source_path: LeetCode-Solutions-master/Python/path-with-minimum-effort.py
# solution_class: Solution
# submission_id: b9e48ffdff1d5d870c97d20a2eb279e3fbcac1a4
# seed: 4281223229

# Time:  O(m * n * log(m * n))
# Space: O(m * n)

import heapq


# Dijkstra algorithm solution

class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dst = (len(heights)-1, len(heights[0])-1)
        dist = [[float("inf")]*len(heights[0]) for _ in xrange(len(heights))]
        dist[0][0] = 0
        min_heap = [(0, 0, 0)]
        lookup = [[False]*len(heights[0]) for _ in xrange(len(heights))]
        while min_heap:
            d, r, c = heapq.heappop(min_heap)
            if lookup[r][c]:
                continue
            lookup[r][c] = True
            if (r, c) == dst:
                return d
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if not (0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and not lookup[nr][nc]):
                    continue
                nd = max(d, abs(heights[nr][nc]-heights[r][c]))
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heapq.heappush(min_heap, (nd, nr, nc))
        return -1
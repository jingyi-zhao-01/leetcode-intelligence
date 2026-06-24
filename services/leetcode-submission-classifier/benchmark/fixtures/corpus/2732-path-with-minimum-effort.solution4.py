# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: path-with-minimum-effort
# source_path: LeetCode-Solutions-master/Python/path-with-minimum-effort.py
# solution_class: Solution4
# submission_id: 01521d6423d148848511520805134da4e6c834d5
# seed: 777082848

# Time:  O(m * n * log(m * n))
# Space: O(m * n)

import heapq


# Dijkstra algorithm solution

class Solution4(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def check(heights, x):
            lookup = [[False]*len(heights[0]) for _ in xrange(len(heights))]
            q = collections.deque([(0, 0)])
            while q:
                r, c = q.popleft()
                if (r, c) == (len(heights)-1, len(heights[0])-1):
                    return True
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if not (0 <= nr < len(heights) and
                                0 <= nc < len(heights[0]) and
                                abs(heights[nr][nc]-heights[r][c]) <= x and
                                not lookup[nr][nc]):
                            continue
                    lookup[nr][nc] = True
                    q.append((nr, nc))
            return False            
        
        left, right = 0, 10**6
        while left <= right:
            mid = left + (right-left)//2
            if check(heights, mid):
                right = mid-1
            else:
                left = mid+1
        return left
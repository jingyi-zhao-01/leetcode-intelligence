# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: path-with-minimum-effort
# source_path: LeetCode-Solutions-master/Python/path-with-minimum-effort.py
# solution_class: Solution3
# submission_id: 53f190cc4ad860880886eb7e4cd19fb9a1e5913f
# seed: 3130774528

# Time:  O(m * n * log(m * n))
# Space: O(m * n)

import heapq


# Dijkstra algorithm solution

class Solution3(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def check(heights, x):  # bi-bfs
            lookup = [[False]*len(heights[0]) for _ in xrange(len(heights))]
            left, right = {(0, 0)}, {(len(heights)-1, len(heights[0])-1)}
            while left:
                for r, c in left:
                    lookup[r][c] = True
                new_left = set()
                for r, c in left:
                    if (r, c) in right: 
                        return True
                    for dr, dc in directions:
                        nr, nc = r+dr, c+dc
                        if not (0 <= nr < len(heights) and
                                0 <= nc < len(heights[0]) and
                                abs(heights[nr][nc]-heights[r][c]) <= x and
                                not lookup[nr][nc]):
                            continue
                        new_left.add((nr, nc))
                left = new_left
                if len(left) > len(right): 
                    left, right = right, left
            return False            
        

        left, right = 0, 10**6
        while left <= right:
            mid = left + (right-left)//2
            if check(heights, mid):
                right = mid-1
            else:
                left = mid+1
        return left
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-minimum-time-to-reach-last-room-ii
# source_path: LeetCode-Solutions-master/Python/find-minimum-time-to-reach-last-room-ii.py
# solution_class: Solution
# submission_id: 6d5a81c356a22c58e6e7c5b6014f0454f638cd16
# seed: 828259357

# Time:  O(n * m * logn(n * m))
# Space: O(n * m)

import heapq


# dijkstra's algorithm

class Solution(object):
    def minTimeToReach(self, moveTime):
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """
        def dijkstra(start, target):
            DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            dist = [[float("inf")]*len(moveTime[0]) for _ in xrange(len(moveTime))]
            dist[start[0]][start[1]] = 0
            min_heap = [(dist[start[0]][start[1]], start[0], start[1])]
            while min_heap:
                curr, i, j = heapq.heappop(min_heap)
                if curr != dist[i][j]:
                    continue
                if (i, j) == target:
                    break
                for di, dj in DIRECTIONS:
                    ni, nj = i+di, j+dj
                    c = (i+j)%2+1
                    if not (0 <= ni < len(moveTime) and 0 <= nj < len(moveTime[0]) and dist[ni][nj] > max(moveTime[ni][nj], curr)+c):
                        continue
                    dist[ni][nj] = max(moveTime[ni][nj], curr)+c
                    heapq.heappush(min_heap, (dist[ni][nj], ni, nj))
            return dist[target[0]][target[1]]
    
        return dijkstra((0, 0), (len(moveTime)-1, len(moveTime[0])-1))
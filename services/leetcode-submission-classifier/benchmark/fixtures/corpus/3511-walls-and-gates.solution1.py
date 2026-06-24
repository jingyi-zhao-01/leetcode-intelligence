# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: walls-and-gates
# source_path: LeetCode-Solutions-master/Python/walls-and-gates.py
# solution_class: Solution
# submission_id: a8bdbecb50c41dbbbd87d84845bd8737d79cce40
# seed: 1641354979

# Time:  O(m * n)
# Space: O(g)

from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        q = deque([(i, j) for i, row in enumerate(rooms) for j, r in enumerate(row) if not r])
        while q:
            (i, j) = q.popleft()
            for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= I < len(rooms) and 0 <= J < len(rooms[0]) and \
                   rooms[I][J] == INF:
                    rooms[I][J] = rooms[i][j] + 1
                    q.append((I, J))
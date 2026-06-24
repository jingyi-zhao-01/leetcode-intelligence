# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-time-takes-to-reach-destination-without-drowning
# source_path: LeetCode-Solutions-master/Python/minimum-time-takes-to-reach-destination-without-drowning.py
# solution_class: Solution2
# submission_id: adbfe266c7ba75d44f6c4913ee40eb9cdcc32fd8
# seed: 386870955

# Time:  O(m * n)
# Space: O(m * n)

# simulation, bfs

class Solution2(object):
    def minimumSeconds(self, land):
        """
        :type land: List[List[str]]
        :rtype: int
        """
        DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        lookup1 = [[0 if land[i][j] == "*" else -1 for j in xrange(len(land[0]))] for i in xrange(len(land))]
        lookup2 = [[-1]*len(land[0]) for _ in xrange(len(land))]
        q1 = [(i, j) for i in xrange(len(land)) for j in xrange(len(land[0])) if land[i][j] == "*"]
        q2 = [next((i, j) for i in xrange(len(land)) for j in xrange(len(land[0])) if land[i][j] == "S")]
        lookup2[q2[0][0]][q2[0][1]] = 0
        while q1 or q2:
            new_q1, new_q2 = [], []
            for i, j in q1:
                for di, dj in DIRECTIONS:
                    ni, nj = i+di, j+dj
                    if not (0 <= ni < len(land) and 0 <= nj < len(land[0]) and land[ni][nj] != "X" and land[ni][nj] != "D" and lookup1[ni][nj] == -1):
                        continue
                    lookup1[ni][nj] = 0
                    new_q1.append((ni, nj))
            for i, j in q2:
                if land[i][j] == "D":
                    return lookup2[i][j]
                for di, dj in DIRECTIONS:
                    ni, nj = i+di, j+dj
                    if not (0 <= ni < len(land) and 0 <= nj < len(land[0]) and land[ni][nj] != "X" and lookup2[ni][nj] == lookup1[ni][nj] == -1):
                        continue
                    lookup2[ni][nj] = lookup2[i][j]+1
                    new_q2.append((ni, nj))
            q1, q2 = new_q1, new_q2
        return -1
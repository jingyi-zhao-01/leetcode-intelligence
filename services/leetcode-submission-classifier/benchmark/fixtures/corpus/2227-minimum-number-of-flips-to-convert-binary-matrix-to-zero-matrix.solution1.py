# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix.py
# solution_class: Solution
# submission_id: f932bb331985d86b6d1e103931719a7913b3d1be
# seed: 29955629

# Time:  O((m * n) * 2^(m * n))
# Space: O((m * n) * 2^(m * n))

import collections

class Solution(object):
    def minFlips(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        directions = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]
        start = sum(val << r*len(mat[0])+c for r, row in enumerate(mat) for c, val in enumerate(row))
        q = collections.deque([(start, 0)])
        lookup = {start}
        while q:
            state, step = q.popleft()
            if not state:
                return step
            for r in xrange(len(mat)):
                for c in xrange(len(mat[0])):
                    new_state = state
                    for dr, dc in directions:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < len(mat) and 0 <= nc < len(mat[0]):
                            new_state ^= 1 << nr*len(mat[0])+nc
                    if new_state in lookup:
                        continue
                    lookup.add(new_state)
                    q.append((new_state, step+1))
        return -1
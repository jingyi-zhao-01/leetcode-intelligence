# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-knights-tour
# source_path: LeetCode-Solutions-master/Python/the-knights-tour.py
# solution_class: Solution2
# submission_id: 3c62322f36338e1147d3e8f5fe44aec7d6356fb7
# seed: 1685857400

# Time:  O(m * n)
# Space: O(1)

# backtracking, greedy, warnsdorff's rule

class Solution2(object):
    def tourOfKnight(self, m, n, r, c):
        """
        :type m: int
        :type n: int
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        DIRECTIONS = ((1, 2), (-1, 2), (1, -2), (-1, -2),
                      (2, 1), (-2, 1), (2, -1), (-2, -1))
        def backtracking(r, c, i):
            if i == m*n:
                return True
            for dr, dc in DIRECTIONS:
                nr, nc = r+dr, c+dc
                if not (0 <= nr < m and 0 <= nc < n and result[nr][nc] == -1):
                    continue
                result[nr][nc] = i
                if backtracking(nr, nc, i+1):
                    return True
                result[nr][nc] = -1
            return False
    
        result = [[-1]*n for _ in xrange(m)]
        result[r][c] = 0
        backtracking(r, c, 1)
        return result
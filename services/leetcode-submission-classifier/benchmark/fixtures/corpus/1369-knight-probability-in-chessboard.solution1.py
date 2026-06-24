# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: knight-probability-in-chessboard
# source_path: LeetCode-Solutions-master/Python/knight-probability-in-chessboard.py
# solution_class: Solution
# submission_id: 3a81b1a40fb807351665db817df8a4a3a521f2e0
# seed: 1498949047

# Time:  O(k * n^2)
# Space: O(n^2)

class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        directions = \
            [[ 1, 2], [ 1, -2], [ 2, 1], [ 2, -1], \
             [-1, 2], [-1, -2], [-2, 1], [-2, -1]]
        dp = [[[1 for _ in xrange(N)] for _ in xrange(N)] for _ in xrange(2)]
        for step in xrange(1, K+1):
            for i in xrange(N):
                for j in xrange(N):
                    dp[step%2][i][j] = 0
                    for direction in directions:
                        rr, cc = i+direction[0], j+direction[1]
                        if 0 <= cc < N and 0 <= rr < N:
                            dp[step%2][i][j] += 0.125 * dp[(step-1)%2][rr][cc]

        return dp[K%2][r][c]
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: knight-dialer
# source_path: LeetCode-Solutions-master/Python/knight-dialer.py
# solution_class: Solution2
# submission_id: 479525ce7fc9f261a38624778bb98267dade0f18
# seed: 773394430

# Time:  O(logn)
# Space: O(1)

import itertools

class Solution2(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        M = 10**9 + 7
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [],
                 [1, 7, 0], [2, 6], [1, 3], [2, 4]]

        dp = [[1 for _ in xrange(10)] for _ in xrange(2)]
        for i in xrange(N-1):
            dp[(i+1) % 2] = [0] * 10
            for j in xrange(10):
                for nei in moves[j]:
                    dp[(i+1) % 2][nei] += dp[i % 2][j]
                    dp[(i+1) % 2][nei] %= M
        return sum(dp[(N-1) % 2]) % M
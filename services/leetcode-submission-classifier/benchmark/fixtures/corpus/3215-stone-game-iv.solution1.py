# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: stone-game-iv
# source_path: LeetCode-Solutions-master/Python/stone-game-iv.py
# solution_class: Solution
# submission_id: 092d2744e4db3d1101a35af32a8885ed374694c8
# seed: 4068133887

# Time:  O(n * sqrt(n))
# Space: O(n)

class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dp = [False]*(n+1)
        for i in xrange(1, n+1):
            j = 1
            while j*j <= i:
                if not dp[i-j*j]:
                    dp[i] = True
                    break
                j += 1
        return dp[-1]
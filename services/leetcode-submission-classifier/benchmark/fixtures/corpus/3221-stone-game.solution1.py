# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: stone-game
# source_path: LeetCode-Solutions-master/Python/stone-game.py
# solution_class: Solution
# submission_id: 5c659b770c62ee11071bccc8ef4b414f254a3524
# seed: 3296778989

# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        if len(piles) % 2 == 0 or len(piles) == 1:
            return True

        dp = [0] * len(piles)
        for i in reversed(xrange(len(piles))):
            dp[i] = piles[i]
            for j in xrange(i+1, len(piles)):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        return dp[-1] >= 0
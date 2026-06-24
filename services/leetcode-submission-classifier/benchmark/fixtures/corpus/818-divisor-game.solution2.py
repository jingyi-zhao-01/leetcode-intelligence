# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divisor-game
# source_path: LeetCode-Solutions-master/Python/divisor-game.py
# solution_class: Solution2
# submission_id: f893ddd5a73090cbb3491eeefc803e13ee44d5b1
# seed: 1047582983

# Time:  O(1)
# Space: O(1)

# math

class Solution2(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def factors(n):
            result = [[] for _ in xrange(n+1)]
            for i in xrange(1, n+1):
                for j in range(i, n+1, i):
                    result[j].append(i)
            return result

        FACTORS = factors(n)
        dp = [False]*(n+1)
        for i in xrange(2, n+1):
            dp[i] = any(not dp[i-j] for j in FACTORS[i] if j != i)
        return dp[-1]
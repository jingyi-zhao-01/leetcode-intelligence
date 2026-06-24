# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-people-aware-of-a-secret
# source_path: LeetCode-Solutions-master/Python/number-of-people-aware-of-a-secret.py
# solution_class: Solution
# submission_id: bbbe58747974f10016033b2ef04636f153af004e
# seed: 2776366830

# Time:  O(n)
# Space: O(f)

# dp

class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [0]*forget
        dp[0] = 1
        for i in xrange(1, n):
            dp[i%forget] = ((dp[(i-1)%forget] if i-1 else 0)-dp[i%forget]+dp[(i-delay)%forget]) % MOD
        return sum(dp)%MOD
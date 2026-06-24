# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-ways-to-stay-in-the-same-place-after-some-steps
# source_path: LeetCode-Solutions-master/Python/number-of-ways-to-stay-in-the-same-place-after-some-steps.py
# solution_class: Solution
# submission_id: 5941ca5e55c77a8125573fa46c4d07a072c21a7a
# seed: 2045655608

# Time:  O(n^2), n is the number of steps
# Space: O(n)
    

class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        MOD = int(1e9+7)
        l = min(1+steps//2, arrLen)
        dp = [0]*(l+2)
        dp[1] = 1
        while steps > 0:
            steps -= 1
            new_dp = [0]*(l+2)
            for i in xrange(1, l+1):
                new_dp[i] = (dp[i] + dp[i-1] + dp[i+1]) % MOD
            dp = new_dp
        return dp[1]
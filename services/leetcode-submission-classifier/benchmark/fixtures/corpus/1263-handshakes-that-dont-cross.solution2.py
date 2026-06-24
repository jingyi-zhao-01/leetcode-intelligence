# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: handshakes-that-dont-cross
# source_path: LeetCode-Solutions-master/Python/handshakes-that-dont-cross.py
# solution_class: Solution2
# submission_id: 007412c124c0d2ddbfb822fa9997f37da54e98f8
# seed: 3650634987

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def numberOfWays(self, num_people):
        """
        :type num_people: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [0]*(num_people//2+1)
        dp[0] = 1
        for k in xrange(1, num_people//2+1):
            for i in xrange(k):
                dp[k] = (dp[k] + dp[i]*dp[k-1-i]) % MOD
        return dp[num_people//2]
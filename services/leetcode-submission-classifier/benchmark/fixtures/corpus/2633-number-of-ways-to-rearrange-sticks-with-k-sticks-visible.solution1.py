# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-ways-to-rearrange-sticks-with-k-sticks-visible
# source_path: LeetCode-Solutions-master/Python/number-of-ways-to-rearrange-sticks-with-k-sticks-visible.py
# solution_class: Solution
# submission_id: c2c3136db73fe80a5b176583e7f4f72756dc9bef
# seed: 3392108653

# Time:  O(n * k)
# Space: O(k)

class Solution(object):
    def rearrangeSticks(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [[0 for _ in xrange(k+1)] for _ in xrange(2)]
        dp[1][1] = 1
        for i in xrange(2, n+1):
            for j in xrange(1, min(i, k)+1):
                # choose the tallest as the last one which would be visible:    dp[i-1][j-1]
                # choose the non-tallest as the last one which would be hidden: (i-1)*dp[i-1][j]
                dp[i%2][j] = (dp[(i-1)%2][j-1]+(i-1)*dp[(i-1)%2][j]) % MOD 
        return dp[n%2][k]
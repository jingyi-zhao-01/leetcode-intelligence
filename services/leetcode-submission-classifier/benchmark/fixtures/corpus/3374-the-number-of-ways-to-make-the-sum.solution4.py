# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-number-of-ways-to-make-the-sum
# source_path: LeetCode-Solutions-master/Python/the-number-of-ways-to-make-the-sum.py
# solution_class: Solution4
# submission_id: 452cb353132e4c4b5b864dc22bc43c39fd914aff
# seed: 3352605018

# Time:  O(1)
# Space: O(1)

# math

class Solution4(object):
    def numberOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [0]*(n+1)
        dp[0] = 1
        for i in (1, 2, 6):
            for j in xrange(i, n+1):
                dp[j] += dp[j-i]
        return reduce(lambda x, y: (x+dp[n-4*y])%MOD, (i for i in xrange(min(n//4, 2)+1)), 0)
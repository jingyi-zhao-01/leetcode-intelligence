# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-zigzag-arrays-i
# source_path: LeetCode-Solutions-master/Python/number-of-zigzag-arrays-i.py
# solution_class: Solution
# submission_id: ab341a7c52b20512a425472064c3f0fb57a5ae81
# seed: 2149873892

# Time:  O(n * (r - l))
# Space: O(r - l)

# prefix sum, dp

class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9+7
        r -= l
        dp = [1]*(r+1)
        for _ in xrange(n-1):
            prefix = 0
            for i in xrange(len(dp)):
                dp[i], prefix = prefix, (prefix+dp[i])%MOD
            dp.reverse()
        return (reduce(lambda accu, x: (accu+x)%MOD, dp, 0)*2)%MOD
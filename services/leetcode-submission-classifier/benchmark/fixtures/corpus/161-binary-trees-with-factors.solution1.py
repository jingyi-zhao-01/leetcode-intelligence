# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-trees-with-factors
# source_path: LeetCode-Solutions-master/Python/binary-trees-with-factors.py
# solution_class: Solution
# submission_id: fe2151fc7e18e1c0015bd2c6985cea74fbdaea13
# seed: 3928835142

# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        M = 10**9 + 7
        A.sort()
        dp = {}
        for i in xrange(len(A)):
            dp[A[i]] = 1
            for j in xrange(i):
                if A[i] % A[j] == 0 and A[i] // A[j] in dp:
                    dp[A[i]] += dp[A[j]] * dp[A[i] // A[j]]
                    dp[A[i]] %= M
        return sum(dp.values()) % M
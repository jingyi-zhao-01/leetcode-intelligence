# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-permutations-for-di-sequence
# source_path: LeetCode-Solutions-master/Python/valid-permutations-for-di-sequence.py
# solution_class: Solution
# submission_id: f56374ed0445068396a9bf3f9a3413e671af8c13
# seed: 756131840

# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        dp = [1]*(len(S)+1)
        for c in S:
            if c == "I":
                dp = dp[:-1]
                for i in xrange(1, len(dp)):
                    dp[i] += dp[i-1]
            else:
                dp = dp[1:]
                for i in reversed(xrange(len(dp)-1)):
                    dp[i] += dp[i+1]
        return dp[0] % (10**9+7)
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: target-sum
# source_path: LeetCode-Solutions-master/Python/target-sum.py
# solution_class: Solution
# submission_id: b289a664113ad4723539a4dc10b38940f85e71cd
# seed: 2274040244

# Time:  O(n * S)
# Space: O(S)

import collections

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def subsetSum(nums, S):
            dp = collections.defaultdict(int)
            dp[0] = 1
            for n in nums:
                for i in reversed(xrange(n, S+1)):
                    if i-n in dp:
                        dp[i] += dp[i-n]
            return dp[S]

        total = sum(nums)
        if total < S or (S + total) % 2: return 0
        P = (S + total) // 2
        return subsetSum(nums, P)
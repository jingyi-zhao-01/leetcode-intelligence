# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-good-subsequences
# source_path: LeetCode-Solutions-master/Python/sum-of-good-subsequences.py
# solution_class: Solution
# submission_id: e6339e16d20b10a3d257d58c9efa9f10c3aed9da
# seed: 692282129

# Time:  O(n)
# Space: O(n)

import collections


# freq table, dp

class Solution(object):
    def sumOfGoodSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        dp = collections.defaultdict(int)
        cnt = collections.defaultdict(int)
        for x in nums:
            c = cnt[x-1]+cnt[x+1]+1
            cnt[x] = (cnt[x]+c)%MOD
            dp[x] = (dp[x]+(dp[x-1]+dp[x+1]+x*c))%MOD
        return reduce(lambda accu, x: (accu+x)%MOD, dp.itervalues())
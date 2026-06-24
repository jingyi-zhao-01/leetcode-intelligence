# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-special-triplets
# source_path: LeetCode-Solutions-master/Python/count-special-triplets.py
# solution_class: Solution
# submission_id: 8eb3c08bafe613bf83481485e5b73aa774686f9e
# seed: 2632153475

# Time:  O(n)
# Space: O(n)

import collections


# dp

class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        result = 0
        dp = [collections.defaultdict(int) for _ in xrange(2)]
        for x in nums:
            if x%2 == 0 and x//2 in dp[1]:
                result = (result+dp[1][x//2])%MOD
            if 2*x in dp[0]:
                dp[1][x] = (dp[1][x]+dp[0][2*x])%MOD
            dp[0][x] = (dp[0][x]+1)%MOD
        return result
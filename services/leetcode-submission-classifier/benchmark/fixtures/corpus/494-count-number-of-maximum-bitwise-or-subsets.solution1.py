# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-number-of-maximum-bitwise-or-subsets
# source_path: LeetCode-Solutions-master/Python/count-number-of-maximum-bitwise-or-subsets.py
# solution_class: Solution
# submission_id: 5cf2aae058d6730d3ea97324c8b34d28128e0c5c
# seed: 2515862463

# Time:  O(min(2^n, m * n)), m is the 'bitwise or' of nums
# Space: O(min(2^n, m))

import collections

class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = collections.Counter([0])
        for x in nums:
            for k, v in dp.items():
                dp[k|x] += v
        return dp[reduce(lambda x, y: x|y, nums)]
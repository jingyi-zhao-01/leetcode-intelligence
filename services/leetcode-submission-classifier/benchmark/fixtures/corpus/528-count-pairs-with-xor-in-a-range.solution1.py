# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-pairs-with-xor-in-a-range
# source_path: LeetCode-Solutions-master/Python/count-pairs-with-xor-in-a-range.py
# solution_class: Solution
# submission_id: 2e6f4a4a70e00d2f6f7d6d91d34ddb70aaf93f14
# seed: 2600259179

# Time:  O(n)
# Space: O(n)

import collections


# dp solution

class Solution(object):
    def countPairs(self, nums, low, high):
        """
        :type nums: List[int]
        :type low: int
        :type high: int
        :rtype: int
        """
        def count(nums, x):
            result = 0
            dp = collections.Counter(nums)
            while x:
                if x&1:
                    result += sum(dp[(x^1)^k]*dp[k] for k in dp.iterkeys())//2  # current limit is xxxxx1*****, count xor pair with xxxxx0***** pattern
                dp = collections.Counter({k>>1: dp[k]+dp[k^1] for k in dp.iterkeys()})
                x >>= 1
            return result
    
        return count(nums, high+1)-count(nums, low)
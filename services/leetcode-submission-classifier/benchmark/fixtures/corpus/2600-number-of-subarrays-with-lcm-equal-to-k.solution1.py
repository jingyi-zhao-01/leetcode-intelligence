# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-subarrays-with-lcm-equal-to-k
# source_path: LeetCode-Solutions-master/Python/number-of-subarrays-with-lcm-equal-to-k.py
# solution_class: Solution
# submission_id: 5713b6d96b677bef34f549b9da148954756fddb2
# seed: 1007343273

# Time:  O(n * sqrt(k) * logk)
# Space: O(sqrt(k))

import collections


# dp

class Solution(object):
    def subarrayLCM(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        def lcm(a, b):
            return a//gcd(a, b)*b

        result = 0
        dp = collections.Counter()
        for x in nums:
            new_dp = collections.Counter()
            if k%x == 0:
                dp[x] += 1
                for l, cnt in dp.iteritems():
                    new_dp[lcm(l, x)] += cnt
            dp = new_dp
            result += dp[k]
        return result
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-product-of-two-integers-with-no-common-bits
# source_path: LeetCode-Solutions-master/Python/maximum-product-of-two-integers-with-no-common-bits.py
# solution_class: Solution
# submission_id: 3478dc1df909391fb0a3e9d021e15b2a612fc307
# seed: 107327490

# Time:  O(n + rlogr), r = max(nums)
# Space: O(r)

# dp, bitmasks

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = max(nums).bit_length()
        dp = [0]*(1<<l)
        for x in nums:
            dp[x] = x
        for i in xrange(l):
            for j in xrange(0, 1<<l, 1<<(i+1)):
                for k in xrange(j, j+(1<<i)):
                    if dp[k] > dp[k+(1<<i)]:
                        dp[k+(1<<i)] = dp[k]
        result = 0
        for x in nums:
            if x*dp[((1<<l)-1)^x] > result:
                result = x*dp[((1<<l)-1)^x]
        return result
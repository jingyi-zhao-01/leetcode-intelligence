# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-product-of-two-integers-with-no-common-bits
# source_path: LeetCode-Solutions-master/Python/maximum-product-of-two-integers-with-no-common-bits.py
# solution_class: Solution2
# submission_id: b561fcfda4d413e41104b218288b086baa2ab0e6
# seed: 2284346055

# Time:  O(n + rlogr), r = max(nums)
# Space: O(r)

# dp, bitmasks

class Solution2(object):
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
            for mask in xrange(1<<l):
                if mask&(1<<i):
                    continue
                if dp[mask] > dp[mask|(1<<i)]:
                    dp[mask|(1<<i)] = dp[mask]
        result = 0
        for x in nums:
            if x*dp[((1<<l)-1)^x] > result:
                result = x*dp[((1<<l)-1)^x]
        return result
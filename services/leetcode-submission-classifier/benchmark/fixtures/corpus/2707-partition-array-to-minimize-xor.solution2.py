# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: partition-array-to-minimize-xor
# source_path: LeetCode-Solutions-master/Python/partition-array-to-minimize-xor.py
# solution_class: Solution2
# submission_id: 080dcce8056999c40c32e30c8095c69c77fa6273
# seed: 942184726

# Time:  O(n^2 * k)
# Space: O(n)

# dp, prefix sum

class Solution2(object):
    def minXor(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        INF = float("inf")
        prefix = [0]*(len(nums)+1)
        for i in xrange(len(nums)):
            prefix[i+1] = prefix[i]^nums[i]
        dp = [INF]*(len(nums)+1)
        dp[0] = 0
        for l in xrange(1, k+1):
            for i in reversed(xrange(l-1, len(dp))):
                dp[i] = INF
                for j in xrange(l-1, i):
                    dp[i] = min(dp[i], max(dp[j], prefix[i]^prefix[j]))
        return dp[-1]
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: partition-array-to-minimize-xor
# source_path: LeetCode-Solutions-master/Python/partition-array-to-minimize-xor.py
# solution_class: Solution
# submission_id: aae27f4b377e4bb83d55151126861ddded4eea41
# seed: 3836723123

# Time:  O(n^2 * k)
# Space: O(n)

# dp, prefix sum

class Solution(object):
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
        dp = prefix[:]
        dp[0] = INF
        for l in xrange(2, k+1):
            for i in reversed(xrange(l-1, len(dp))):
                mn = INF
                for j in xrange(l-1, i):
                    v = prefix[i]^prefix[j]
                    mx = dp[j] if dp[j] > v else v
                    if mx < mn:
                        mn = mx
                dp[i] = mn
        return dp[-1]
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-strength-of-k-disjoint-subarrays
# source_path: LeetCode-Solutions-master/Python/maximum-strength-of-k-disjoint-subarrays.py
# solution_class: Solution2
# submission_id: 99462116eecefcd1fe6ba56ba89b2b6424662ff1
# seed: 2386615056

# Time:  O(k * n)
# Space: O(n)

# dp, greedy, kadane's algorithm

class Solution2(object):
    def maximumStrength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = [[float("-inf")]*(len(nums)+1) for _ in xrange(k+1)]
        dp[0] = [0]*(len(nums)+1)
        for i in xrange(k):
            for j in xrange(len(nums)):
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j])+nums[j]*(k-i)*(1 if i%2 == 0 else -1)
        return max(dp[-1])
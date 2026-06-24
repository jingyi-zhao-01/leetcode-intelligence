# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-great-partitions
# source_path: LeetCode-Solutions-master/Python/number-of-great-partitions.py
# solution_class: Solution
# submission_id: 879c1beed00c5f3151fb0fdd92fc3ff347d0fd3e
# seed: 395809899

# Time:  O(n * k)
# Space: O(k)

# knapsack dp

class Solution(object):
    def countPartitions(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        if sum(nums) < 2*k:
            return 0
        dp = [0]*k
        dp[0] = 1
        for x in nums:
            for i in reversed(xrange(k-x)):
                dp[i+x] = (dp[i+x]+dp[i])%MOD
        return (pow(2, len(nums), MOD)-2*reduce(lambda total, x: (total+x)%MOD, dp, 0))%MOD
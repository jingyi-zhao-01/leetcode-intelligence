# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-make-the-array-beautiful
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-make-the-array-beautiful.py
# solution_class: Solution
# submission_id: a276cfc4f7451fe26cc19848ed5df63267a5787c
# seed: 2763528204

# Time:  O(n * rlogr), r = max(nums)
# Space: O(r)

# dp

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b

        INF = float("inf")
        mx = max(nums)
        if mx == 1:
            return 0
        dp = [INF]*((2*mx-2)+1)
        dp[nums[0]] = 0
        for i in xrange(1, len(nums)):
            new_dp = [INF]*len(dp)
            for x in xrange(1, len(dp)):
                if dp[x] == INF:
                    continue
                for j in xrange(ceil_divide(nums[i], x), (len(dp)-1)//x+1):
                    new_dp[j*x] = min(new_dp[j*x], dp[x]+(j*x-nums[i]))
            dp = new_dp
        return min(dp)
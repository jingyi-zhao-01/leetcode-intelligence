# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-cyclic-partition-score
# source_path: LeetCode-Solutions-master/Python/maximize-cyclic-partition-score.py
# solution_class: Solution
# submission_id: 1ec1cba78f59a5d62a99cb3d81107e6ea40190c7
# seed: 4124301120

# Time:  O(n * k)
# Space: O(k)

# dp

class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def best_time_to_buy_and_sell_stock_v(base):
            dp = [0]*(len(nums)+1)
            result = 0
            for i in xrange(k):
                x, y = float("-inf"), float("-inf")
                new_dp = [float("-inf")]*(len(nums)+1)
                for j in xrange(i, len(nums)):
                    x, y = max(x, dp[j]-nums[(base+j)%len(nums)]), max(y, dp[j]+nums[(base+j)%len(nums)])
                    new_dp[j+1] = max(new_dp[j], x+nums[(base+j)%len(nums)], y-nums[(base+j)%len(nums)])
                dp = new_dp
                result = max(result, dp[-1])
            return result
    
        i = min(xrange(len(nums)), key=lambda x: nums[x])
        return max(best_time_to_buy_and_sell_stock_v(i), best_time_to_buy_and_sell_stock_v(i+1))
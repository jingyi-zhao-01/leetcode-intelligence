# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-sum-after-divisible-sum-deletions
# source_path: LeetCode-Solutions-master/Python/minimum-sum-after-divisible-sum-deletions.py
# solution_class: Solution
# submission_id: d68bb76f25eeee3237b2745c5501478d8571ea8e
# seed: 1601567161

# Time:  O(n + k)
# Space: O(k)

# dp, prefix sum

class Solution(object):
    def minArraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = [float("inf")]*k
        dp[0] = result = 0
        for x in nums:
            result += x
            dp[result%k] = result = min(result, dp[result%k])
        return result
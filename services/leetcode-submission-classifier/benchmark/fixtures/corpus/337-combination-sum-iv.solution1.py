# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: combination-sum-iv
# source_path: LeetCode-Solutions-master/Python/combination-sum-iv.py
# solution_class: Solution
# submission_id: ae0b28a03c5fbc285d71e902bac38d9bb0218012
# seed: 626751932

# Time:  O(nlon + n * t), t is the value of target.
# Space: O(t)

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target+1)
        dp[0] = 1
        nums.sort()

        for i in xrange(1, target+1):
            for j in xrange(len(nums)):
                if nums[j] <= i:
                    dp[i] += dp[i - nums[j]]
                else:
                    break

        return dp[target]
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-consecutive-elements-in-an-array-after-modification
# source_path: LeetCode-Solutions-master/Python/maximize-consecutive-elements-in-an-array-after-modification.py
# solution_class: Solution2
# submission_id: 76ce68808f1b638944e5f148a6e70c575ca69d12
# seed: 3686926117

# Time:  O(nlogn)
# Space: O(1)

# sort, dp

class Solution2(object):
    def maxSelectedElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        dp = collections.defaultdict(int)
        dp[nums[0]] = dp[nums[0]+1] = 1
        for i in xrange(1, len(nums)):
            if nums[i] == nums[i-1]:
                dp[nums[i]+1] = dp[nums[i]]+1
            elif nums[i] == nums[i-1]+1:
                dp[nums[i]+1] = dp[nums[i]]+1
                dp[nums[i]] = dp[nums[i]-1]+1
            elif nums[i] == nums[i-1]+2:
                dp[nums[i]] = dp[nums[i]-1]+1
                dp[nums[i]+1] = 1
            else:
                dp[nums[i]] = dp[nums[i]+1] = 1
        return max(dp.itervalues())
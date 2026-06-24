# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-consecutive-elements-in-an-array-after-modification
# source_path: LeetCode-Solutions-master/Python/maximize-consecutive-elements-in-an-array-after-modification.py
# solution_class: Solution
# submission_id: 7993eb45a333a125b949fb4de6aed4927f6af144
# seed: 485778919

# Time:  O(nlogn)
# Space: O(1)

# sort, dp

class Solution(object):
    def maxSelectedElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 1
        dp = [1]*2  # dp[i]: the maximum length of a consecutive sequence ending with x+i, where x is the last visited value
        for i in xrange(1, len(nums)):
            if nums[i] == nums[i-1]:
                dp[1] = dp[0]+1
            elif nums[i] == nums[i-1]+1:
                dp[0] += 1
                dp[1] += 1
            elif nums[i] == nums[i-1]+2:
                dp[0] = dp[1]+1
                dp[1] = 1
            else:
                dp[0] = dp[1] = 1
            result = max(result, dp[0], dp[1])
        return result
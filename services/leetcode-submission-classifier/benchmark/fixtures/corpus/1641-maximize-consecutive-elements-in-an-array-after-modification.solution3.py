# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-consecutive-elements-in-an-array-after-modification
# source_path: LeetCode-Solutions-master/Python/maximize-consecutive-elements-in-an-array-after-modification.py
# solution_class: Solution3
# submission_id: b69fa6c277870be4c25f7ab9dc74fd46c9d17f15
# seed: 947711009

# Time:  O(nlogn)
# Space: O(1)

# sort, dp

class Solution3(object):
    def maxSelectedElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        dp = collections.defaultdict(int)
        for x in nums:
            dp[x+1] = dp[x]+1
            dp[x] = dp[x-1]+1
        return max(dp.itervalues())
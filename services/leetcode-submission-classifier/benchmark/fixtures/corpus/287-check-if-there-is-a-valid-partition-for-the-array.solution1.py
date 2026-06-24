# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-there-is-a-valid-partition-for-the-array
# source_path: LeetCode-Solutions-master/Python/check-if-there-is-a-valid-partition-for-the-array.py
# solution_class: Solution
# submission_id: 10120c56b41ce0d005659922d3dfae9a77203394
# seed: 3645313063

# Time:  O(n)
# Space: O(1)

# dp

class Solution(object):
    def validPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [False]*4
        dp[0] = True
        for i in xrange(len(nums)):
            dp[(i+1)%4] = False
            if i-1 >= 0 and nums[i] == nums[i-1]:
                dp[(i+1)%4] |= dp[((i+1)-2)%4]
            if i-2 >= 0 and (nums[i] == nums[i-1] == nums[i-2] or
                             nums[i] == nums[i-1]+1 == nums[i-2]+2):
                dp[(i+1)%4] |= dp[((i+1)-3)%4]
        return dp[len(nums)%4]
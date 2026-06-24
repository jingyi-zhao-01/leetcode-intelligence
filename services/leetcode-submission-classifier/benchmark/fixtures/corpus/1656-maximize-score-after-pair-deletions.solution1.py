# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-score-after-pair-deletions
# source_path: LeetCode-Solutions-master/Python/maximize-score-after-pair-deletions.py
# solution_class: Solution
# submission_id: e7f06ab492cf62aebc316c9df13078d2133918b1
# seed: 3446706369

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums)-min(nums) if len(nums)%2 else sum(nums)-min(nums[i]+nums[i+1] for i in xrange(len(nums)-1))
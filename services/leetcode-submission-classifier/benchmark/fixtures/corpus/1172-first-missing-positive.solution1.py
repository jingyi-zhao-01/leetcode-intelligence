# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: first-missing-positive
# source_path: LeetCode-Solutions-master/Python/first-missing-positive.py
# solution_class: Solution
# submission_id: c54c070ce21c80960bc9a6331347dc7fe399d4aa
# seed: 3061723043

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        return next(((i+1) for i, x in enumerate(nums) if x != i+1), len(nums)+1)
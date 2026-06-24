# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-one-element-to-make-the-array-strictly-increasing
# source_path: LeetCode-Solutions-master/Python/remove-one-element-to-make-the-array-strictly-increasing.py
# solution_class: Solution
# submission_id: 84df8059e5929e94dae32ed42d52261d3dac5ec0
# seed: 1586684678

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        deleted = False
        for i in xrange(1, len(nums)):
            if nums[i] > nums[i-1]:
                continue
            if deleted:
                return False
            deleted = True
            if i >= 2 and nums[i-2] > nums[i]:  # delete nums[i] or nums[i-1]
                nums[i] = nums[i-1]
        return True
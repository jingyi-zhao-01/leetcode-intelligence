# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: apply-operations-to-an-array
# source_path: LeetCode-Solutions-master/Python/apply-operations-to-an-array.py
# solution_class: Solution
# submission_id: 9603fe045d8c8a86dd8d9fe74efc7fbf7f8dc699
# seed: 3748223166

# Time:  O(n)
# Space: O(1)

# inplace, array

class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i], nums[i+1] = 2*nums[i], 0
        i = 0
        for x in nums:
            if not x:
                continue
            nums[i] = x
            i += 1
        for i in xrange(i, len(nums)):
            nums[i] = 0
        return nums
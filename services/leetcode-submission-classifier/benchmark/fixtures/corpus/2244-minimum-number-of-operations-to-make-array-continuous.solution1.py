# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-operations-to-make-array-continuous
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-operations-to-make-array-continuous.py
# solution_class: Solution
# submission_id: f06e2896417fe4c9e30aaf00c557ca5496084977
# seed: 787605027

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def unique(nums):
            left = 0
            for right in xrange(1, len(nums)):
                if nums[left] != nums[right]:
                    left += 1
                    nums[left] = nums[right]
            return left

        def erase(nums, i):
            while len(nums) > i+1:
                nums.pop()

        n = len(nums)
        nums.sort()
        erase(nums, unique(nums))
        result = l = 0
        for i in xrange(len(nums)):
            if nums[i] <= nums[i-l]+n-1:
                l += 1
        return n-l
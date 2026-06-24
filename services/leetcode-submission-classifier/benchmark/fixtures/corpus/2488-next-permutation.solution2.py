# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: next-permutation
# source_path: LeetCode-Solutions-master/Python/next-permutation.py
# solution_class: Solution2
# submission_id: 2be48ebc6e452a1c45e17cf43f04aab3abdddd5c
# seed: 67624964

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k, l = -1, 0
        for i in xrange(len(nums)-1):
            if nums[i] < nums[i+1]:
                k = i

        if k == -1:
            nums.reverse()
            return

        for i in xrange(k+1, len(nums)):
            if nums[i] > nums[k]:
                l = i
        nums[k], nums[l] = nums[l], nums[k]
        nums[k+1:] = nums[:k:-1]
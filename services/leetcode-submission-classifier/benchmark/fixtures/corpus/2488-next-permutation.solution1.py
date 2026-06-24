# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: next-permutation
# source_path: LeetCode-Solutions-master/Python/next-permutation.py
# solution_class: Solution
# submission_id: 0495529fe9ad411167df0579a5789918009d766c
# seed: 1391952744

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k, l = -1, 0
        for i in reversed(xrange(len(nums)-1)):
            if nums[i] < nums[i+1]:
                k = i
                break
        else:
            nums.reverse()
            return

        for i in reversed(xrange(k+1, len(nums))):
            if nums[i] > nums[k]:
                l = i
                break
        nums[k], nums[l] = nums[l], nums[k]
        nums[k+1:] = nums[:k:-1]
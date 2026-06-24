# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: kth-largest-element-in-an-array
# source_path: LeetCode-Solutions-master/Python/kth-largest-element-in-an-array.py
# solution_class: Solution2
# submission_id: 1ac1845d003545db16278539ab1add9e8cd8deeb
# seed: 3208571102

# Time:  O(n) on average, using Median of Medians could achieve O(n) (Intro Select)
# Space: O(1)

from random import randint


# optimized for duplicated nums

class Solution2(object):
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_idx = randint(left, right)
            new_pivot_idx = self.PartitionAroundPivot(left, right, pivot_idx, nums)
            if new_pivot_idx == k - 1:
                return nums[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k - 1.
                left = new_pivot_idx + 1

    def PartitionAroundPivot(self, left, right, pivot_idx, nums):
        pivot_value = nums[pivot_idx]
        new_pivot_idx = left
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        for i in xrange(left, right):
            if nums[i] > pivot_value:
                nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                new_pivot_idx += 1

        nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
        return new_pivot_idx
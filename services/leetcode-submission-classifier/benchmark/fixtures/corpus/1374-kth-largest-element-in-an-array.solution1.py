# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: kth-largest-element-in-an-array
# source_path: LeetCode-Solutions-master/Python/kth-largest-element-in-an-array.py
# solution_class: Solution
# submission_id: 3f6bc5dd02ac3e312320a901515eb3df8dc1a678
# seed: 2688593301

# Time:  O(n) on average, using Median of Medians could achieve O(n) (Intro Select)
# Space: O(1)

from random import randint


# optimized for duplicated nums

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def nth_element(nums, n, compare=lambda a, b: a < b):
            def tri_partition(nums, left, right, target, compare):
                mid = left
                while mid <= right:
                    if nums[mid] == target:
                        mid += 1
                    elif compare(nums[mid], target):
                        nums[left], nums[mid] = nums[mid], nums[left]
                        left += 1
                        mid += 1
                    else:
                        nums[mid], nums[right] = nums[right], nums[mid]
                        right -= 1
                return left, right

            left, right = 0, len(nums)-1
            while left <= right:
                pivot_idx = randint(left, right)
                pivot_left, pivot_right = tri_partition(nums, left, right, nums[pivot_idx], compare)
                if pivot_left <= n <= pivot_right:
                    return
                elif pivot_left > n:
                    right = pivot_left-1
                else:  # pivot_right < n.
                    left = pivot_right+1

        nth_element(nums, k-1, compare=lambda a, b: a > b)
        return nums[k-1]
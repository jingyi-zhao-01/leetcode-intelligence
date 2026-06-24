# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: absolute-difference-between-maximum-and-minimum-k-elements
# source_path: LeetCode-Solutions-master/Python/absolute-difference-between-maximum-and-minimum-k-elements.py
# solution_class: Solution
# submission_id: c8ba3fd72ba5a526f2549e93ff5b8ac60d06ba87
# seed: 2197107069

# Time:  O(n)
# Space: O(1)

import random


# quick select

class Solution(object):
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def nth_element(nums, n, left=0, compare=lambda a, b: a < b):
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
            
            right = len(nums)-1
            while left <= right:
                pivot_idx = random.randint(left, right)
                pivot_left, pivot_right = tri_partition(nums, left, right, nums[pivot_idx], compare)
                if pivot_left <= n <= pivot_right:
                    return
                elif pivot_left > n:
                    right = pivot_left-1
                else:  # pivot_right < n.
                    left = pivot_right+1

        nth_element(nums, k-1)
        total1 = sum(nums[i] for i in xrange(k))
        nth_element(nums, k-1, compare=lambda a, b: a > b)
        total2 = sum(nums[i] for i in xrange(k))
        return abs(total1-total2)
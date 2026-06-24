# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-elements-with-at-least-k-greater-values
# source_path: LeetCode-Solutions-master/Python/count-elements-with-at-least-k-greater-values.py
# solution_class: Solution
# submission_id: 292697e87a903ac0cb009872fa79674eedef0378
# seed: 842738770

# Time:  O(n)
# Space: O(1)

import random


# quick select

class Solution(object):
    def countElements(self, nums, k):
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
                pivot_idx = random.randint(left, right)
                pivot_left, pivot_right = tri_partition(nums, left, right, nums[pivot_idx], compare)
                if pivot_left <= n <= pivot_right:
                    return
                elif pivot_left > n:
                    right = pivot_left-1
                else:  # pivot_right < n.
                    left = pivot_right+1

        if not k:
            return len(nums)
        nth_element(nums, len(nums)-k)
        return sum(nums[i] < nums[-k] for i in xrange(len(nums)-k))
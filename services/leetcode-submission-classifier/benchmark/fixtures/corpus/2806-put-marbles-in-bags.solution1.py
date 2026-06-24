# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: put-marbles-in-bags
# source_path: LeetCode-Solutions-master/Python/put-marbles-in-bags.py
# solution_class: Solution
# submission_id: 7df076353dd9a599ca74562ebebb604a6287e236
# seed: 2645675028

# Time:  O(n) on average
# Space: O(1)

import random


# greedy, quick select

class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
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

        for i in xrange(len(weights)-1):
            weights[i] += weights[i+1]
        weights.pop()
        result = 0
        nth_element(weights, (k-1)-1, compare=lambda a, b: a > b)
        result += sum(weights[i] for i in xrange(k-1))
        nth_element(weights, (k-1)-1)
        result -= sum(weights[i] for i in xrange(k-1))
        return result
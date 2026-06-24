# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-sum-with-at-most-k-elements
# source_path: LeetCode-Solutions-master/Python/maximum-sum-with-at-most-k-elements.py
# solution_class: Solution
# submission_id: c42bd178a673dcbaf975e400d5aca6fd96e648b1
# seed: 525470237

# Time:  O(n * m)
# Space: O(1)

import random


# greedy, quick select

class Solution(object):
    def maxSum(self, grid, limits, k):
        """
        :type grid: List[List[int]]
        :type limits: List[int]
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

        candidates = []
        for i in xrange(len(grid)):
            cnt = min(k, limits[i])
            nth_element(grid[i], cnt-1, lambda a, b: a > b)
            for j in xrange(cnt):
                candidates.append(grid[i][j])
        nth_element(candidates, k-1, lambda a, b: a > b)
        return sum(candidates[i] for i in xrange(k))
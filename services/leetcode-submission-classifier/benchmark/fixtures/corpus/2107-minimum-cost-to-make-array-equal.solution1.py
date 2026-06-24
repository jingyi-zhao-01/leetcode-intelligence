# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-make-array-equal
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-make-array-equal.py
# solution_class: Solution
# submission_id: 891818d4592eb24641053565d21264092965261c
# seed: 1166165729

# Time:  O(nlogn)
# Space: O(n)

import itertools


# math, binary search

class Solution(object):
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int
        """
        def f(x):
            return sum(abs(y-x)*c for y, c in itertools.izip(nums, cost))

        def check(x, t):
            return sum(c for y, c in itertools.izip(nums, cost) if y <= x) >= t
    
        idxs = range(len(nums))
        idxs.sort(key=lambda x: nums[x])
        left, right = 0, len(idxs)-1
        total = sum(cost)
        median = (total+1)//2
        while left <= right:
            mid = left+(right-left)//2
            if check(nums[idxs[mid]], median):
                right = mid-1
            else:
                left = mid+1
        return f(nums[idxs[left]])
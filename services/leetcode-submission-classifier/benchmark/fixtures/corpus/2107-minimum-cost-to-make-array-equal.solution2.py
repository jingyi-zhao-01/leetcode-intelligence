# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-make-array-equal
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-make-array-equal.py
# solution_class: Solution2
# submission_id: ab795de811aa31eb99fb3b933ace2f03b13f077e
# seed: 553853539

# Time:  O(nlogn)
# Space: O(n)

import itertools


# math, binary search

class Solution2(object):
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int
        """
        def f(x):
            return sum(abs(y-x)*c for y, c in itertools.izip(nums, cost))
    
        def check(x):
            return x+1 == len(idxs) or f(nums[idxs[x]]) < f(nums[idxs[x+1]])

        idxs = range(len(nums))
        idxs.sort(key=lambda x: nums[x])
        left, right = 0, len(idxs)-1
        while left <= right:
            mid = left+(right-left)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return f(nums[idxs[left]])
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-make-array-equal
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-make-array-equal.py
# solution_class: Solution3
# submission_id: d51b6894c9f9986998e15d42e9dfbeaa80db7513
# seed: 847075851

# Time:  O(nlogn)
# Space: O(n)

import itertools


# math, binary search

class Solution3(object):
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int
        """
        idxs = range(len(nums))
        idxs.sort(key=lambda x: nums[x])
        prefix = [0]*(len(cost)+1)
        left = 0
        for i in xrange(len(cost)):
            if i-1 >= 0:
                left += prefix[i]*(nums[idxs[i]]-nums[idxs[i-1]])
            prefix[i+1] = prefix[i]+cost[idxs[i]]
        result = float("inf")
        suffix = right = 0
        for i in reversed(xrange(len(cost))):
            if i+1 < len(idxs):
                right += suffix*(nums[idxs[i+1]]-nums[idxs[i]])
            result = min(result, left+right)
            if i-1 >= 0:
                left -= prefix[i]*(nums[idxs[i]]-nums[idxs[i-1]])
            suffix += cost[idxs[i]]
        return result
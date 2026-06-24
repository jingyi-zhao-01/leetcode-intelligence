# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-bitwise-and-after-increment-operations
# source_path: LeetCode-Solutions-master/Python/maximum-bitwise-and-after-increment-operations.py
# solution_class: Solution2
# submission_id: 194024b3360e395cd3575a47815d5d3ccb023e25
# seed: 1534271349

# Time:  O(nlogr)
# Space: O(n)

import random


# bitmasks, greedy, quick select

class Solution2(object):
    def maximumAND(self, nums, k, m):
        """
        :type nums: List[int]
        :type k: int
        :type m: int
        :rtype: int
        """
        result = 0
        for i in reversed(xrange((max(nums)+k).bit_length())):
            target = result|(1<<i)
            costs = []
            for x in nums:
                l = (target&~x).bit_length()
                mask = (1<<l)-1
                costs.append((target&mask)-(x&mask))
            costs.sort()
            if sum(costs[i] for i in xrange(m)) <= k:
                result |= 1<<i
        return result
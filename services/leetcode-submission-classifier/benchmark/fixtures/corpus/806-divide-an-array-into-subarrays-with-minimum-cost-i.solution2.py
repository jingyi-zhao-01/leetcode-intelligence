# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divide-an-array-into-subarrays-with-minimum-cost-i
# source_path: LeetCode-Solutions-master/Python/divide-an-array-into-subarrays-with-minimum-cost-i.py
# solution_class: Solution2
# submission_id: 39af5679c68f4d75c56410b7c0bb098c22e5c441
# seed: 2914556704

# Time:  O(n)
# Space: O(1)

import random


# array, quick select

class Solution2(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def topk(a, k):
            result = [float("inf")]*k
            for x in a:
                for i in xrange(len(result)):
                    if x < result[i]:
                        result[i], x = x, result[i]
            return result

        return nums[0]+sum(topk((nums[i] for i in xrange(1, len(nums))), 2))
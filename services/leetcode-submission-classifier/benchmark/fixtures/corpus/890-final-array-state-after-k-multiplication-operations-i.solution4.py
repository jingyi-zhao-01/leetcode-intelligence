# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: final-array-state-after-k-multiplication-operations-i
# source_path: LeetCode-Solutions-master/Python/final-array-state-after-k-multiplication-operations-i.py
# solution_class: Solution4
# submission_id: 2a9a91b05c83780d873844f5c982f0997bea07c9
# seed: 1188029528

# Time:  O(n + (n + logr) + nlog(logr) + nlogn) = O(nlogn), assumed log(x) takes O(1) time
# Space: O(n)

import math


# sort, two pointers, sliding window, fast exponentiation

class Solution4(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        if multiplier == 1:
            return nums
        min_heap = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(min_heap)
        for _ in xrange(k):
            i = heapq.heappop(min_heap)[1]
            nums[i] *= multiplier
            heapq.heappush(min_heap, (nums[i], i))
        return nums
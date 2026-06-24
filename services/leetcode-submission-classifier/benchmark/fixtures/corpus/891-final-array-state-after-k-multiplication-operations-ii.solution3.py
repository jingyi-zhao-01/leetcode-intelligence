# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: final-array-state-after-k-multiplication-operations-ii
# source_path: LeetCode-Solutions-master/Python/final-array-state-after-k-multiplication-operations-ii.py
# solution_class: Solution3
# submission_id: f41828972080ac5352e908e48499a348dfeed9d5
# seed: 4283872248

# Time:  O(n + (n + logr) + nlog(logr) + nlogn) = O(nlogn), assumed log(x) takes O(1) time
# Space: O(n)

import math


# sort, two pointers, sliding window, fast exponentiation

class Solution3(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        MOD = 10**9+7
        if multiplier == 1:
            return nums
        min_heap = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(min_heap)
        mx = max(nums)
        for k in reversed(xrange(1, k+1)):
            if min_heap[0][0]*multiplier > mx:
                break
            x, i = heapq.heappop(min_heap)
            heapq.heappush(min_heap, (x*multiplier, i))
        else:
            k = 0
        vals = sorted(min_heap)
        q, r = divmod(k, len(nums))
        m = pow(multiplier, q, MOD)
        result = [0]*len(nums)
        for idx, (x, i) in enumerate(vals):
            result[i] = x*m*(multiplier if idx < r else 1)%MOD
        return result
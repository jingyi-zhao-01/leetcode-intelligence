# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: final-array-state-after-k-multiplication-operations-ii
# source_path: LeetCode-Solutions-master/Python/final-array-state-after-k-multiplication-operations-ii.py
# solution_class: Solution
# submission_id: 9371329bd0ab35c6df9f88222cb5456ea750f116
# seed: 400283543

# Time:  O(n + (n + logr) + nlog(logr) + nlogn) = O(nlogn), assumed log(x) takes O(1) time
# Space: O(n)

import math


# sort, two pointers, sliding window, fast exponentiation

class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        MOD = 10**9+7
        EPS = 1e-15
        def count(x, target):
            return int(target-x+EPS)

        if multiplier == 1:
            return nums
        vals = sorted((log(x)/log(multiplier), i) for i, x in enumerate(nums))
        left = 0
        for right in xrange(1, (int(vals[-1][0])+1)+1):
            while left < len(vals) and count(vals[left][0], right) >= 1:
                left += 1
            if k-left < 0:
                right -= 1
                break
            k -= left
        for idx, (x, i) in enumerate(vals):
            c = count(x, right)
            if c <= 0:
                break
            nums[i] *= pow(multiplier, c)
        q, r = divmod(k, len(nums))
        m = pow(multiplier, q, MOD)
        result = [0]*len(nums)
        for idx, (x, i) in enumerate(sorted((x, i) for i, x in enumerate(nums))):
            result[i] = x*m*(multiplier if idx < r else 1)%MOD
        return result
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: final-array-state-after-k-multiplication-operations-i
# source_path: LeetCode-Solutions-master/Python/final-array-state-after-k-multiplication-operations-i.py
# solution_class: Solution2
# submission_id: ec8be7689eb61aac8e05baebece02c3ba00ddb2a
# seed: 1346699807

# Time:  O(n + (n + logr) + nlog(logr) + nlogn) = O(nlogn), assumed log(x) takes O(1) time
# Space: O(n)

import math


# sort, two pointers, sliding window, fast exponentiation

class Solution2(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        EPS = 1e-15
        def binary_search_right(left, right, check):
            while left <= right:
                mid = left+(right-left)//2
                if not check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return right

        def count(x, target):
            return int(target-x+EPS)

        def check(target):
            result = 0
            for x, i in vals:
                c = count(x, target)
                if c <= 0:
                    break
                result += c
            return result <= k

        if multiplier == 1:
            return nums
        vals = sorted((log(x)/log(multiplier), i) for i, x in enumerate(nums))
        target = binary_search_right(1, int(vals[-1][0])+1, check)
        for idx, (x, i) in enumerate(vals):
            c = count(x, target)
            if c <= 0:
                break
            k -= c
            nums[i] *= pow(multiplier, c)
        q, r = divmod(k, len(nums))
        m = pow(multiplier, q)
        result = [0]*len(nums)
        for idx, (x, i) in enumerate(sorted((x, i) for i, x in enumerate(nums))):
            result[i] = x*m*(multiplier if idx < r else 1)
        return result
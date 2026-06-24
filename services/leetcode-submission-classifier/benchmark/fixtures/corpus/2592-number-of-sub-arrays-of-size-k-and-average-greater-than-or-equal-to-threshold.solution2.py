# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold
# source_path: LeetCode-Solutions-master/Python/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold.py
# solution_class: Solution2
# submission_id: ee5b8a91c7e4e3d58233d78ee5617fb25b92450c
# seed: 3293662841

# Time:  O(n)
# Space: O(1)

import itertools

class Solution2(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        accu = [0]
        for x in arr:
            accu.append(accu[-1]+x)
        result = 0
        for i in xrange(len(accu)-k):
            if accu[i+k]-accu[i] >= threshold*k:
                result += 1
        return result
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold
# source_path: LeetCode-Solutions-master/Python/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold.py
# solution_class: Solution
# submission_id: 9c4811741c7d34c0a659fbb54d8fd6b79cf789c5
# seed: 3708938435

# Time:  O(n)
# Space: O(1)

import itertools

class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        result, curr = 0, sum(itertools.islice(arr, 0, k-1))
        for i in xrange(k-1, len(arr)):
            curr += arr[i]-(arr[i-k] if i-k >= 0 else 0)
            result += int(curr >= threshold*k)
        return result
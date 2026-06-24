# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-subarray-sum-after-removing-all-occurrences-of-one-element
# source_path: LeetCode-Solutions-master/Python/maximize-subarray-sum-after-removing-all-occurrences-of-one-element.py
# solution_class: Solution2
# submission_id: 1bc84b2fb40c2947e268ba2d955951310dfbdb92
# seed: 2767802630

# Time:  O(n)
# Space: O(n)

import collections


# hash table, greedy, kadane's algorithm

class Solution2(object):
    def maxSubarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = float("-inf")
        curr = mn = mn0 = 0
        mn1 = collections.defaultdict(int)
        for x in nums:
            curr += x
            result = max(result, curr-mn)
            if x < 0:
                mn1[x] = min(mn1[x], mn0)+x
                mn = min(mn, mn1[x])
            mn0 = min(mn0, curr)
            mn = min(mn, mn0)
        return result
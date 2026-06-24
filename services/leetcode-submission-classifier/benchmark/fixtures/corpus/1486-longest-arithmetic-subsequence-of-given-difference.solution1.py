# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-arithmetic-subsequence-of-given-difference
# source_path: LeetCode-Solutions-master/Python/longest-arithmetic-subsequence-of-given-difference.py
# solution_class: Solution
# submission_id: 764403258388330577e40ac1ba16a1cab0564fd7
# seed: 3916187767

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        result = 1
        lookup = collections.defaultdict(int)
        for i in xrange(len(arr)):
            lookup[arr[i]] = lookup[arr[i]-difference] + 1
            result = max(result, lookup[arr[i]])
        return result
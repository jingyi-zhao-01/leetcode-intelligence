# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-strictly-increasing-subsequence-with-non-zero-bitwise-and
# source_path: LeetCode-Solutions-master/Python/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and.py
# solution_class: Solution
# submission_id: ff3958b1dd62ec65b7f1b5e024f0e0c3b4a9a339
# seed: 673166348

# Time:  O(logr * nlogn)
# Space: O(n)

import bisect


# bitmasks, lis, binary search

class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def lis(base):
            result = []
            for x in nums:
                if not x&base:
                    continue
                if not result or result[-1] < x:
                    result.append(x)
                else:
                    result[bisect.bisect_left(result, x)] = x
            return len(result)
    
        mx = max(nums)
        return max(lis(1<<l) for l in xrange(mx.bit_length())) if mx else 0
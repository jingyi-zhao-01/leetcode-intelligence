# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-fixed-points-after-deletions
# source_path: LeetCode-Solutions-master/Python/maximize-fixed-points-after-deletions.py
# solution_class: Solution
# submission_id: 81f0b86a7f2cd93de82b69d8214be33866b5ac8f
# seed: 81839325

# Time:  O(nlogn)
# Space: O(n)

import bisect


# sort, binary search, longest increasing subsequence, lis

class Solution(object):
    def maxFixedPoints(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def longest_increasing_subsequence(arr):
            result = []
            for x in arr:
                i = bisect.bisect_left(result, x)
                if i == len(result):
                    result.append(x)
                else:
                    result[i] = x
            return len(result)

        return longest_increasing_subsequence(x for _, x in sorted((i-x, x) for i, x in enumerate(nums) if i-x >= 0))
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-increasing-subsequence-to-be-removed
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-increasing-subsequence-to-be-removed.py
# solution_class: Solution
# submission_id: d614c61317696a77733ba206a097a6b0783b94ac
# seed: 798434183

# Time:  O(nlogn)
# Space: O(n)

import bisect


# binary search, longest increasing subsequence, lis

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def longest_non_increasing_subsequence(arr):
            result = []
            for x in arr:
                right = bisect.bisect_right(result, -x)
                if right == len(result):
                    result.append(-x)
                else:
                    result[right] = -x
            return len(result)
        
        return longest_non_increasing_subsequence(nums)
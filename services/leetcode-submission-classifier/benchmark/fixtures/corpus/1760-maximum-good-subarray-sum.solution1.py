# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-good-subarray-sum
# source_path: LeetCode-Solutions-master/Python/maximum-good-subarray-sum.py
# solution_class: Solution
# submission_id: d68d06f5b101ad7f9c5749a88fc9c595992a9956
# seed: 2257430356

# Time:  O(n)
# Space: O(n)

import collections


# prefix sum

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = collections.defaultdict(lambda: float("inf"))
        curr = 0
        result = float("-inf")
        for x in nums:
            prefix[x] = min(prefix[x], curr)
            curr += x
            result = max(result, curr-prefix[x-k], curr-prefix[x+k])
        return result if result != float("-inf") else 0
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subarray-sum-equals-k
# source_path: LeetCode-Solutions-master/Python/subarray-sum-equals-k.py
# solution_class: Solution
# submission_id: 51e8e0c14376b9d87ceb95adcd8eaa11569bf78c
# seed: 1414582622

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        accumulated_sum = 0
        lookup = collections.defaultdict(int)
        lookup[0] += 1
        for num in nums:
            accumulated_sum += num
            result += lookup[accumulated_sum - k]
            lookup[accumulated_sum] += 1
        return result
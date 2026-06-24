# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-sum-score-of-array
# source_path: LeetCode-Solutions-master/Python/maximum-sum-score-of-array.py
# solution_class: Solution2
# submission_id: e9fa57d30c251364c840228cb83f91cc9162629b
# seed: 2479471588

# Time:  O(n)
# Space: O(1)

# prefix sum, math

class Solution2(object):
    def maximumSumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        prefix = 0
        result = float("-inf")
        for x in nums:
            prefix += x
            result = max(result, prefix, total-prefix+x)
        return result
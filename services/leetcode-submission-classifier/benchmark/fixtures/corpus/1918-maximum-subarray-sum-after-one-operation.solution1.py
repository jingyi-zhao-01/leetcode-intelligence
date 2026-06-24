# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-subarray-sum-after-one-operation
# source_path: LeetCode-Solutions-master/Python/maximum-subarray-sum-after-one-operation.py
# solution_class: Solution
# submission_id: 9b2b44ea6d1db51f28943efab92279bd7ca1379d
# seed: 3871538318

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxSumAfterOperation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_with_square = prev_without_square = 0
        result = 0
        for num in nums:
            without_square = max(num, num+prev_without_square)
            with_square = max(num*num, num*num+prev_without_square, num+prev_with_square)
            result = max(result, with_square)
            prev_with_square, prev_without_square = with_square, without_square
        return result
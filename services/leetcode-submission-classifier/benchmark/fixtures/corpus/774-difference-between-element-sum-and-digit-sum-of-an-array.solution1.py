# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: difference-between-element-sum-and-digit-sum-of-an-array
# source_path: LeetCode-Solutions-master/Python/difference-between-element-sum-and-digit-sum-of-an-array.py
# solution_class: Solution
# submission_id: 374b371051b5795a12eff1ed9e63c6e0e6d6fefd
# seed: 1478371613

# Time:  O(nlogr), r = max(nums)
# Space: O(1)

# array

class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def total(x):
            result = 0
            while x:
                result += x%10
                x //= 10
            return result

        return abs(sum(nums)-sum(total(x) for x in nums))
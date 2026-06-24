# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-transformed-array
# source_path: LeetCode-Solutions-master/Python/sort-transformed-array.py
# solution_class: Solution
# submission_id: a982d2d80a74e3fa17a30f42e8e06244088346d7
# seed: 4132374388

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        f = lambda x, a, b, c : a * x * x + b * x + c

        result = []
        if not nums:
            return result

        left, right = 0, len(nums) - 1
        d = -1 if a > 0 else 1
        while left <= right:
            if d * f(nums[left], a, b, c) < d * f(nums[right], a, b, c):
                result.append(f(nums[left], a, b, c))
                left += 1
            else:
                result.append(f(nums[right], a, b, c))
                right -= 1

        return result[::d]
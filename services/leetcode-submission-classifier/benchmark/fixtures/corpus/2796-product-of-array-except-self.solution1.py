# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: product-of-array-except-self
# source_path: LeetCode-Solutions-master/Python/product-of-array-except-self.py
# solution_class: Solution
# submission_id: 4f7f37f59f7674fdafbf11ba2d840454f8146afa
# seed: 652268201

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        if not nums:
            return []

        left_product = [1 for _ in xrange(len(nums))]
        for i in xrange(1, len(nums)):
            left_product[i] = left_product[i - 1] * nums[i - 1]

        right_product = 1
        for i in xrange(len(nums) - 2, -1, -1):
            right_product *= nums[i + 1]
            left_product[i] = left_product[i] * right_product

        return left_product
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: single-number-iii
# source_path: LeetCode-Solutions-master/Python/single-number-iii.py
# solution_class: Solution2
# submission_id: 0072b24dde67b45239d832196c9d99616ced3174
# seed: 16258827

# Time:  O(n)
# Space: O(1)

import operator
import collections

class Solution2(object):
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        x_xor_y = 0
        for i in nums:
            x_xor_y ^= i

        bit = x_xor_y & ~(x_xor_y - 1)

        x = 0
        for i in nums:
            if i & bit:
                x ^= i

        return [x, x ^ x_xor_y]
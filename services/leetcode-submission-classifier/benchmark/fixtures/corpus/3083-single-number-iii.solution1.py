# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: single-number-iii
# source_path: LeetCode-Solutions-master/Python/single-number-iii.py
# solution_class: Solution
# submission_id: 38bec12045793524bf033ce35a93b260006ff176
# seed: 1703275066

# Time:  O(n)
# Space: O(1)

import operator
import collections

class Solution(object):
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        x_xor_y = reduce(operator.xor, nums)
        bit =  x_xor_y & -x_xor_y
        result = [0, 0]
        for i in nums:
            result[bool(i & bit)] ^= i
        return result
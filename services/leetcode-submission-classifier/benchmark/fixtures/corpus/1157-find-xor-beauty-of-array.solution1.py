# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-xor-beauty-of-array
# source_path: LeetCode-Solutions-master/Python/find-xor-beauty-of-array.py
# solution_class: Solution
# submission_id: b53830dcb7c44d86bd590599cb2f7d5a91602636
# seed: 2303694181

# Time:  O(n)
# Space: O(1)

import operator


# bit manipulation, math

class Solution(object):
    def xorBeauty(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(operator.xor, nums)
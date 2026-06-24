# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: single-number-ii
# source_path: LeetCode-Solutions-master/Python/single-number-ii.py
# solution_class: Solution2
# submission_id: 84fd2935928853ecb30bb130a99718f6251aa969
# seed: 1707432060

# Time:  O(n)
# Space: O(1)

import collections

class Solution2(object):
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one, two, carry = 0, 0, 0
        for x in A:
            two |= one & x
            one ^= x
            carry = one & two
            one &= ~carry
            two &= ~carry
        return one
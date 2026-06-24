# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: single-number-ii
# source_path: LeetCode-Solutions-master/Python/single-number-ii.py
# solution_class: Solution
# submission_id: 1f1e93171a2df274dd067b80407282be5c3efa04
# seed: 3063228472

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one, two = 0, 0
        for x in A:
            one, two = (~x & one) | (x & ~one & ~two), (~x & two) | (x & one)
        return one
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: single-number
# source_path: LeetCode-Solutions-master/Python/single-number.py
# solution_class: Solution
# submission_id: f1f8b89b6c0d031ab3860cd8dd2c2595c3bd8a32
# seed: 4053778058

# Time:  O(n)
# Space: O(1)

import operator
from functools import reduce

class Solution(object):
    """
    :type nums: List[int]
    :rtype: int
    """
    def singleNumber(self, A):
        return reduce(operator.xor, A)
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-two-sneaky-numbers-of-digitville
# source_path: LeetCode-Solutions-master/Python/the-two-sneaky-numbers-of-digitville.py
# solution_class: Solution
# submission_id: 56e91687cdaa45f6371699d03ba7dc9117a9a51f
# seed: 806955630

# Time:  O(n)
# Space: O(1)

import itertools


# bit manipulation

class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def f(check):
            return reduce(lambda accu, x: accu^x, (x for x in itertools.chain(nums, xrange(n)) if check(x)), 0)

        n = len(nums)-2
        x_xor_y = f(lambda _: True)
        bit = x_xor_y&-x_xor_y
        return [f(lambda x: x&bit == 0), f(lambda x: x&bit != 0)]
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-numbers-with-even-number-of-digits
# source_path: LeetCode-Solutions-master/Python/find-numbers-with-even-number-of-digits.py
# solution_class: Solution
# submission_id: 6f6f0911bae4fdb845687b7ec2c14759b589f2d5
# seed: 351036138

# Time:  O(nlog(logm)), n the length of nums, m is the max value of nums
# Space: O(logm)

import bisect

class Solution(object):
    def __init__(self):
        M = 10**5
        self.__lookup = [0]
        i = 10
        while i < M:
            self.__lookup.append(i)
            i *= 10
        self.__lookup.append(i)

    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def digit_count(n):
            return bisect.bisect_right(self.__lookup, n)

        return sum(digit_count(n) % 2 == 0 for n in nums)
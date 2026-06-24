# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-numbers-with-even-number-of-digits
# source_path: LeetCode-Solutions-master/Python/find-numbers-with-even-number-of-digits.py
# solution_class: Solution2
# submission_id: 05190a7647c44b06f37ef9a837afc2c2f2d0dfc8
# seed: 3610665933

# Time:  O(nlog(logm)), n the length of nums, m is the max value of nums
# Space: O(logm)

import bisect

class Solution2(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def digit_count(n):
            result = 0
            while n:
                n //= 10
                result += 1
            return result

        return sum(digit_count(n) % 2 == 0 for n in nums)
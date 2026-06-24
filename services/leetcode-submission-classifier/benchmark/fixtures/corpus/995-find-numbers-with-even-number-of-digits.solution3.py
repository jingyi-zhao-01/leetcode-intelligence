# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-numbers-with-even-number-of-digits
# source_path: LeetCode-Solutions-master/Python/find-numbers-with-even-number-of-digits.py
# solution_class: Solution3
# submission_id: 020423e8b4f5ae1655849657f0187a6d7f25733b
# seed: 2479411603

# Time:  O(nlog(logm)), n the length of nums, m is the max value of nums
# Space: O(logm)

import bisect

class Solution3(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(len(str(n)) % 2 == 0 for n in nums)
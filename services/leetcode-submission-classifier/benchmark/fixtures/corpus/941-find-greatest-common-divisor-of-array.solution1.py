# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-greatest-common-divisor-of-array
# source_path: LeetCode-Solutions-master/Python/find-greatest-common-divisor-of-array.py
# solution_class: Solution
# submission_id: 1d4fe0c93092ee9fa9150723db73fadfcec2a40e
# seed: 2116397946

# Time:  O(n)
# Space: O(1)

import fractions

class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return fractions.gcd(min(nums), max(nums))
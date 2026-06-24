# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: neither-minimum-nor-maximum
# source_path: LeetCode-Solutions-master/Python/neither-minimum-nor-maximum.py
# solution_class: Solution
# submission_id: 63cd1b8afc654e52ead34fced3e6232cc13275b3
# seed: 2364767672

# Time:  O(n)
# Space: O(1)

# one pass, array

class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx, mn = float("-inf"), float("inf")
        result = -1
        for x in nums:
            if mn < x < mx:
                return x
            if x < mn:
                result = mn
                mn = x
            if x > mx:
                result = mx
                mx = x
        return result if mn < result < mx else -1
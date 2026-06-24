# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-good-integer
# source_path: LeetCode-Solutions-master/Python/check-good-integer.py
# solution_class: Solution
# submission_id: 2d08f24e23f306b008cdc3c60dd3fd07e914f50c
# seed: 2605330913

# Time:  O(logn)
# Space: O(1)

# math

class Solution(object):
    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = 0
        while n:
            n, r = divmod(n, 10)
            result += r*r-r
        return result >= 50
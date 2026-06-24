# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-digit-number
# source_path: LeetCode-Solutions-master/Python/valid-digit-number.py
# solution_class: Solution2
# submission_id: e2bede265db9d574df37c06439a5045868ef447d
# seed: 1159175672

# Time:  O(logn)
# Space: O(1)

# math

class Solution2(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        digits = map(int, str(n))
        return x != digits[0] and x in digits
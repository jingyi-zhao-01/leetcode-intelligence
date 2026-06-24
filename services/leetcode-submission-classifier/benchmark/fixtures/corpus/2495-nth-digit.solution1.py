# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: nth-digit
# source_path: LeetCode-Solutions-master/Python/nth-digit.py
# solution_class: Solution
# submission_id: 20366179e6ea022b89360cafee0e7da18cac1115
# seed: 3309972461

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit_len = 1
        while n > digit_len * 9 * (10 ** (digit_len-1)):
            n -= digit_len  * 9 * (10 ** (digit_len-1))
            digit_len += 1

        num = 10 ** (digit_len-1) + (n-1)/digit_len

        nth_digit = num / (10 ** ((digit_len-1) - ((n-1)%digit_len)))
        nth_digit %= 10

        return nth_digit
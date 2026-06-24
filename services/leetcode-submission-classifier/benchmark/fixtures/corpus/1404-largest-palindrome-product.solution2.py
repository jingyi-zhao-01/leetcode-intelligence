# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-palindrome-product
# source_path: LeetCode-Solutions-master/Python/largest-palindrome-product.py
# solution_class: Solution2
# submission_id: 6a496004d8415c163ff85af14e1db10117b35392
# seed: 2130724819

# Time:  O(n * 10^n)
# Space: O(n)

class Solution2(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        def divide_ceil(a, b):
            return (a+b-1)//b

        if n == 1:
            return 9
        upper, lower = 10**n-1, 10**(n-1)
        for i in reversed(xrange(lower, upper**2//(10**n)+1)):
            candidate = int(str(i) + str(i)[::-1])
            for y in reversed(xrange(divide_ceil(lower, 11)*11, upper+1, 11)):  # y must be divisible by 11 because even-number-length palindrome meets modulo 11 digit check
                if candidate//y > upper:
                    break
                if candidate%y == 0 and lower <= candidate//y:
                    return candidate%1337
        return -1
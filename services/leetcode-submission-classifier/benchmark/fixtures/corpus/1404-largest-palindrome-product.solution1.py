# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-palindrome-product
# source_path: LeetCode-Solutions-master/Python/largest-palindrome-product.py
# solution_class: Solution
# submission_id: 86ccef50d625b9d180322c10326a95915440f009
# seed: 3396684047

# Time:  O(n * 10^n)
# Space: O(n)

class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        # let x = 10^n-i, y = 10^n-j, s.t. palindrome = x*y
        # => (10^n-i)*(10^n-j) = (10^n-i-j)*10^n + i*j
        # assume i*j < 10^n (in fact, it only works for 2 <= n <= 8, not general),
        # let left = (10^n-i-j), right = i*j, k = i+j
        # => left = 10^n-k, right = i*(k-i)
        # => i^2 - k*i + right = 0
        # => i = (k+(k^2-right*4)^(0.5))/2 or (k+(k^2-right*4)^(0.5))/2 where i is a positive integer
        upper = 10**n-1
        for k in xrange(2, upper+1):
            left = 10**n-k
            right = int(str(left)[::-1])
            d = k**2-right*4
            if d < 0:
                continue
            if d**0.5 == int(d**0.5) and k%2 == int(d**0.5)%2:
                return (left*10**n+right)%1337
        return -1
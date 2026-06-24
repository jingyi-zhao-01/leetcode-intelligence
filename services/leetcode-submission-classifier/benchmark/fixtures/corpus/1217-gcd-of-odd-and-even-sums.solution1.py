# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: gcd-of-odd-and-even-sums
# source_path: LeetCode-Solutions-master/Python/gcd-of-odd-and-even-sums.py
# solution_class: Solution
# submission_id: 1fee40690f04021d93022da2a9134e92eeccee74
# seed: 2361446074

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        # gcd((1+(2n-1))*n/2, (2+2n)*n/2) = gcd(n*n, n*(n+1)) = n * gcd(n, n+1) = n
        return n
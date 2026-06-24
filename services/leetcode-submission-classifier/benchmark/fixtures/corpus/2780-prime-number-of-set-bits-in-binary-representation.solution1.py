# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: prime-number-of-set-bits-in-binary-representation
# source_path: LeetCode-Solutions-master/Python/prime-number-of-set-bits-in-binary-representation.py
# solution_class: Solution
# submission_id: e3e992ccc71f4f433c873693d1ba953e62376047
# seed: 3977012021

# Time:  O(log(R - L)) = O(1)
# Space: O(1)

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def bitCount(n):
            result = 0
            while n:
                n &= n-1
                result += 1
            return result

        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bitCount(i) in primes
                   for i in xrange(L, R+1))
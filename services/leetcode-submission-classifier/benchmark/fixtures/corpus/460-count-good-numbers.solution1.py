# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-good-numbers
# source_path: LeetCode-Solutions-master/Python/count-good-numbers.py
# solution_class: Solution
# submission_id: bde3675bc3c499d904404a1ed52e411cbff0b592
# seed: 4149653271

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        def powmod(a, b, mod):
            a %= mod
            result = 1
            while b:
                if b&1:
                    result = (result*a)%mod
                a = (a*a)%mod
                b >>= 1
            return result

        MOD = 10**9 + 7
        return powmod(5, (n+1)//2%(MOD-1), MOD)*powmod(4, n//2%(MOD-1), MOD) % MOD
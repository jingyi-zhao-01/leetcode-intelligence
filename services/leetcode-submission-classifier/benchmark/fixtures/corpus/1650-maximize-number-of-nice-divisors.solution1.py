# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-number-of-nice-divisors
# source_path: LeetCode-Solutions-master/Python/maximize-number-of-nice-divisors.py
# solution_class: Solution
# submission_id: 0e645dcae3b21b1962ed12beadf2fbd031bc833e
# seed: 4017290718

# Time:  O(logn)
# Space: O(1)

# variant of "343. integer break"

class Solution(object):
    def maxNiceDivisors(self, primeFactors):
        """
        :type primeFactors: int
        :rtype: int
        """
        # given a1 + a2 + ... + ak <= n, find max of a1 * a2 * ... * ak 
        # => given a1 + a2 + ... + ak = n, find max of a1 * a2 * ... * ak 
        # => ai is either 3 or 2, see proof in "343. integer break"
        MOD = 10**9 + 7
        if primeFactors <= 3:
            return primeFactors
        if primeFactors % 3 == 0:  # 6 => 3*3
            return pow(3, primeFactors//3, MOD)
        if primeFactors % 3 == 1:  # 4 => 2*2 
            return (2*2*pow(3, (primeFactors-4)//3, MOD)) % MOD
        return (2*pow(3, (primeFactors-2)//3, MOD)) % MOD  # 5 => 2*3
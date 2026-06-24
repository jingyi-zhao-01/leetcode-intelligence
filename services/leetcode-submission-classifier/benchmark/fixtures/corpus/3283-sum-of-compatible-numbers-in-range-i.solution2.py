# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-compatible-numbers-in-range-i
# source_path: LeetCode-Solutions-master/Python/sum-of-compatible-numbers-in-range-i.py
# solution_class: Solution2
# submission_id: a0334077e9c782d731c29e3a756791ba2b2792b6
# seed: 977419251

# Time:  O(log(n + k))
# Space: O(1)

# bitmasks, combinatorics

class Solution2(object):
    def sumOfGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        return sum(i for i in xrange(max(n-k, 1), (n+k)+1) if n&i == 0)
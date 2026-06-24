# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: k-th-symbol-in-grammar
# source_path: LeetCode-Solutions-master/Python/k-th-symbol-in-grammar.py
# solution_class: Solution
# submission_id: c908bcef76184ff1cd9a1bfea1292c2d37761e3e
# seed: 1317750634

# Time:  O(logn) = O(1) because n is 32-bit integer
# Space: O(1)

class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        def bitCount(n):
            result = 0
            while n:
                n &= n - 1
                result += 1
            return result

        return bitCount(K-1) % 2
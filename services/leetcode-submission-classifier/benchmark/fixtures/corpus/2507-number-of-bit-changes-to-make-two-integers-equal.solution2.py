# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-bit-changes-to-make-two-integers-equal
# source_path: LeetCode-Solutions-master/Python/number-of-bit-changes-to-make-two-integers-equal.py
# solution_class: Solution2
# submission_id: 3f86447f4b6ce8eaef53a70ebd6825089aed195d
# seed: 3077278901

# Time:  O(logn)
# Space: O(1)

# bit manipulation

class Solution2(object):
    def minChanges(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def popcount(x):
            return bin(x).count('1')

        return popcount(n^k) if n|(n^k) == n else -1
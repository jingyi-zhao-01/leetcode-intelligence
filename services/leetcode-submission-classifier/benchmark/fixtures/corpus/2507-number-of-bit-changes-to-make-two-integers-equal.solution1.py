# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-bit-changes-to-make-two-integers-equal
# source_path: LeetCode-Solutions-master/Python/number-of-bit-changes-to-make-two-integers-equal.py
# solution_class: Solution
# submission_id: 60312a9a446c120f19c0ebc18bb206126916b527
# seed: 474110301

# Time:  O(logn)
# Space: O(1)

# bit manipulation

class Solution(object):
    def minChanges(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def popcount(x):
            return bin(x).count('1')

        return popcount(n^k) if n&k == k else -1
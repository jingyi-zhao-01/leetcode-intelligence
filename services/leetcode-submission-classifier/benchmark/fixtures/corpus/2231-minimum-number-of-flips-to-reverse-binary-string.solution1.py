# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-flips-to-reverse-binary-string
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-flips-to-reverse-binary-string.py
# solution_class: Solution
# submission_id: d50f3cab7c1803a35980e44276620a549ee63c83
# seed: 2241945848

# Time:  O(logn)
# Space: O(1)

# bitmasks

class Solution(object):
    def minimumFlips(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = n.bit_length()
        return sum(2 for i in xrange(l//2) if (n>>i)&1 != (n>>((l-1)-i))&1)
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-make-the-integer-zero
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-make-the-integer-zero.py
# solution_class: Solution
# submission_id: dbc16ee7ee4a68669fb9bf82bfd68672baa1da1c
# seed: 508130364

# Time:  O(1)
# Space: O(1)

# math, linear search, bit manipulations

class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def popcount(x):
            result = 0
            while x:
                x &= (x-1)
                result += 1
            return result

        for i in xrange(1, 60+1):
            if num1-i*num2 < 0:
                break
            if popcount(num1-i*num2) <= i <= num1-i*num2:
                return i
        return -1
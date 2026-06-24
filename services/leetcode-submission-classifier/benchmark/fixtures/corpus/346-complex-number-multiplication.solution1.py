# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: complex-number-multiplication
# source_path: LeetCode-Solutions-master/Python/complex-number-multiplication.py
# solution_class: Solution
# submission_id: d959a68aa9909735695f2c9c8d781e86e2dfe2e1
# seed: 1873820011

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ra, ia = map(int, a[:-1].split('+'))
        rb, ib = map(int, b[:-1].split('+'))
        return '%d+%di' % (ra * rb - ia * ib, ra * ib + ia * rb)
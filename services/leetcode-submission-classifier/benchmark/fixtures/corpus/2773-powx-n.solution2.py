# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: powx-n
# source_path: LeetCode-Solutions-master/Python/powx-n.py
# solution_class: Solution2
# submission_id: 962b2d73da308084d8adae71a99877638ec14b58
# seed: 3962361442

# Time:  O(logn)
# Space: O(1)

class Solution2(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0 and n != -n:
            return 1.0 / self.myPow(x, -n)
        if n == 0:
            return 1
        v = self.myPow(x, n / 2)
        if n % 2 == 0:
            return v * v
        else:
            return v * v * x
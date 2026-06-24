# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: water-and-jug-problem
# source_path: LeetCode-Solutions-master/Python/water-and-jug-problem.py
# solution_class: Solution
# submission_id: f87dc656c2b05c292bcefc08bb25541a0050553d
# seed: 2091799328

# Time:  O(logn),  n is the max of (x, y)
# Space: O(1)

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        # The problem is to solve:
        # - check z <= x + y
        # - check if there is any (a, b) integers s.t. ax + by = z
        return z == 0 or ((z <= x + y) and (z % gcd(x, y) == 0))
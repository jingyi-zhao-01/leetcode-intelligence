# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-point-is-reachable
# source_path: LeetCode-Solutions-master/Python/check-if-point-is-reachable.py
# solution_class: Solution
# submission_id: 908c98a85384408548eec76186aa4b278cb0342f
# seed: 3946543713

# Time:  O(log(min(a, b)))
# Space: O(1)

# number theory

class Solution(object):
    def isReachable(self, targetX, targetY):
        """
        :type targetX: int
        :type targetY: int
        :rtype: bool
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a
    
        g = gcd(targetX, targetY)
        return g == (g&~(g-1))  # co-prime other than factor 2
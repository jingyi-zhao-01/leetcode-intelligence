# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: mirror-reflection
# source_path: LeetCode-Solutions-master/Python/mirror-reflection.py
# solution_class: Solution2
# submission_id: 31677d1f4330eb2fb5e3a1117d239fc792af6b89
# seed: 717182706

# Time:  O(1)
# Space: O(1)

class Solution2(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        lcm = p*q // gcd(p, q)
        # let a = lcm / p, b = lcm / q
        if lcm // p % 2 == 1:
            if lcm // q % 2 == 1:
                return 1  # a is odd, b is odd <=> (p & -p) == (q & -q)
            return 2  # a is odd, b is even <=> (p & -p) > (q & -q)
        return 0  # a is even, b is odd <=> (p & -p) < (q & -q)
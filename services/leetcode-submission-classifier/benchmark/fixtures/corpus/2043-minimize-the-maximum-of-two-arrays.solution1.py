# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-the-maximum-of-two-arrays
# source_path: LeetCode-Solutions-master/Python/minimize-the-maximum-of-two-arrays.py
# solution_class: Solution
# submission_id: a4be6816efdf907943270e80729c920257fe0d1d
# seed: 2022890209

# Time:  O(log(min(d1, d2)))
# Space: O(1)

# number theory

class Solution(object):
    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):
        """
        :type divisor1: int
        :type divisor2: int
        :type uniqueCnt1: int
        :type uniqueCnt2: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        def lcm(a, b):
            return a//gcd(a, b)*b

        def count(cnt, d1, d2):
            l = lcm(d1, d2)
            return cnt+cnt//(l-1)-int(cnt%(l-1) == 0)
        
        return max(count(uniqueCnt1, divisor1, 1),
                   count(uniqueCnt2, divisor2, 1),
                   count(uniqueCnt1+uniqueCnt2, divisor1, divisor2))
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-the-maximum-of-two-arrays
# source_path: LeetCode-Solutions-master/Python/minimize-the-maximum-of-two-arrays.py
# solution_class: Solution2
# submission_id: 56e1b9a64861b6900c67ccaed996826fe6079ff1
# seed: 652918078

# Time:  O(log(min(d1, d2)))
# Space: O(1)

# number theory

class Solution2(object):
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

        def check(cnt):
            return (cnt-cnt//divisor1 >= uniqueCnt1 and
                    cnt-cnt//divisor2 >= uniqueCnt2 and
                    cnt-cnt//l >= uniqueCnt1+uniqueCnt2)

        l = lcm(divisor1, divisor2)
        left, right = 2, 2**31-1
        while left <= right:
            mid = left+(right-left)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return left
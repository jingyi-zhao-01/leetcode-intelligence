# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: nth-magical-number
# source_path: LeetCode-Solutions-master/Python/nth-magical-number.py
# solution_class: Solution
# submission_id: a0ed83fb29d393784807c1549c3f40aec5928f20
# seed: 1694592418

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def check(A, B, N, lcm, target):
            return target//A + target//B - target//lcm >= N

        lcm = A*B // gcd(A, B)
        left, right = min(A, B), max(A, B)*N
        while left <= right:
            mid = left + (right-left)//2
            if check(A, B, N, lcm, mid):
                right = mid-1
            else:
                left = mid+1
        return left % (10**9 + 7)
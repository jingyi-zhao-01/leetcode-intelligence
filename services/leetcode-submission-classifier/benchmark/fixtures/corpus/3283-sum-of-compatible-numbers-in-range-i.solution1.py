# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-compatible-numbers-in-range-i
# source_path: LeetCode-Solutions-master/Python/sum-of-compatible-numbers-in-range-i.py
# solution_class: Solution
# submission_id: 0c4f3ed6913f354543531c73c9f86483b47a1c3a
# seed: 1113801474

# Time:  O(log(n + k))
# Space: O(1)

# bitmasks, combinatorics

class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def count(x):
            if x <= 0:
                return 0
            l = x.bit_length()
            total, cnt = 0, 1
            for i in xrange(l):
                if n&(1<<i):
                    continue
                total = total*2+(1<<i)*cnt
                cnt *= 2
            result = prefix = 0
            for i in reversed(xrange(l)):
                if not n&(1<<i):
                    cnt //= 2
                    total = (total-(1<<i)*cnt)//2
                if not x&(1<<i):
                    continue
                result += prefix*cnt+total
                if n&(1<<i):
                    return result
                prefix |= 1<<i
            result += prefix
            return result

        return count(n+k)-count((n-k)-1)
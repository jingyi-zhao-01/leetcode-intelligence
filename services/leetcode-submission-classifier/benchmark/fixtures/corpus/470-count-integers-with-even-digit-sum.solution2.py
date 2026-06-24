# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-integers-with-even-digit-sum
# source_path: LeetCode-Solutions-master/Python/count-integers-with-even-digit-sum.py
# solution_class: Solution2
# submission_id: e6da041a2f5ea58216382f7efd435479d0a591f0
# seed: 2029270080

# Time:  O(logn)
# Space: O(1)

# math

class Solution2(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        def parity(x):
            result = 0
            while x:
                result += x%10
                x //= 10
            return result%2

        return sum(parity(x) == 0 for x in xrange(1, num+1))
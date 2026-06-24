# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-beautiful-integers-in-the-range
# source_path: LeetCode-Solutions-master/Python/number-of-beautiful-integers-in-the-range.py
# solution_class: Solution4
# submission_id: a43237b99c54b8b01552e57cfc0a5afd059a7e00
# seed: 4144512773

# Time:  O(n^2 * k), n = len(str(high))
# Space: O(n^2 * k)

# memoization (faster but more space)

class Solution4(object):
    def numberOfBeautifulIntegers(self, low, high, k):
        """
        :type low: int
        :type high: int
        :type k: int
        :rtype: int
        """
        def f(x):
            digits = map(int, str(x))
            dp = [[[[0]*k for _ in xrange(2*len(digits)+1)] for _ in xrange(2)] for _ in xrange(2)]
            for tight in xrange(2):
                dp[0][tight][0][0] = 1
            for i in reversed(xrange(len(digits))):
                new_dp = [[[[0]*k for _ in xrange(2*len(digits)+1)] for _ in xrange(2)] for _ in xrange(2)]
                for zero in xrange(2):
                    for tight in xrange(2):
                        for d in xrange((digits[i] if tight else 9)+1):
                            new_zero = int(zero and d == 0)
                            new_tight = int(tight and d == digits[i])
                            for diff in xrange(-len(digits), len(digits)+1):
                                new_diff = diff+((1 if d%2 == 0 else -1) if new_zero == 0 else 0)
                                for total in xrange(k):
                                    new_total = (total*10+d)%k
                                    new_dp[zero][tight][diff][total] += dp[new_zero][new_tight][new_diff][new_total]
                dp = new_dp
            return dp[1][1][0][0]

        return f(high)-f(low-1)
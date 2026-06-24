# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-beautiful-integers-in-the-range
# source_path: LeetCode-Solutions-master/Python/number-of-beautiful-integers-in-the-range.py
# solution_class: Solution2
# submission_id: 1816aef1160b0de2dd4d0a9aabeead3756c0a174
# seed: 2661803458

# Time:  O(n^2 * k), n = len(str(high))
# Space: O(n^2 * k)

# memoization (faster but more space)

class Solution2(object):
    def numberOfBeautifulIntegers(self, low, high, k):
        """
        :type low: int
        :type high: int
        :type k: int
        :rtype: int
        """
        TIGHT, UNTIGHT, UNBOUND = range(3)
        def f(x):
            digits = map(int, str(x))
            dp = [[[0]*k for _ in xrange(2*len(digits)+1)] for _ in xrange(3)]
            for tight in xrange(2):
                for state in (TIGHT, UNTIGHT):
                    dp[state][0][0] = 1
            for i in reversed(xrange(len(digits))):
                new_dp = [[[0]*k for _ in xrange(2*len(digits)+1)] for _ in xrange(3)]
                for state in (TIGHT, UNTIGHT, UNBOUND):
                    new_dp[state][0][0] = int(i != 0)  # count if the beautiful integer x s.t. len(str(x)) < len(digits)
                    for d in xrange(1 if i == 0 else 0, 10):
                        new_state = state
                        if state == TIGHT and d != digits[i]:
                            new_state = UNTIGHT if d < digits[i] else UNBOUND
                        for diff in xrange(-len(digits), len(digits)+1):
                            new_diff = diff+(1 if d%2 == 0 else -1)
                            for total in xrange(k):
                                new_total = (total*10+d)%k
                                new_dp[state][diff][total] += dp[new_state][new_diff][new_total]
                dp = new_dp
            return dp[TIGHT][0][0]

        return f(high)-f(low-1)
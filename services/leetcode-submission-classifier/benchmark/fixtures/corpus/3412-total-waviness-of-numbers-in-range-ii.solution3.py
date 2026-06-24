# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: total-waviness-of-numbers-in-range-ii
# source_path: LeetCode-Solutions-master/Python/total-waviness-of-numbers-in-range-ii.py
# solution_class: Solution3
# submission_id: 563dc4bc751203c4f660e0805cc0b14e630c0919
# seed: 1263996642

# Time:  O(logn * 11 * 11 * 2 * 2 * 10)
# Space: O(logn * 11 * 11 * 2 * 2)

# memoization by dict

class Solution3(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def count(x):
            s = str(x)
            dp = {}
            for prev in xrange(-1, 10):
                for prev2 in xrange(-1, 10):
                    for zero in xrange(2):
                        for tight in xrange(2):
                            dp[(prev, prev2, zero, tight)] = (1, 0)
            for i in reversed(xrange(len(s))):
                new_dp = {}
                for prev in xrange(-1, 10):
                    for prev2 in xrange(-1, 10):
                        for zero in xrange(2):
                            for tight in xrange(2):
                                cnt = w = 0
                                mx = int(s[i]) if tight else 9
                                for d in xrange(mx+1):
                                    new_tight = tight and (d == int(s[i]))
                                    new_zero = zero and (d == 0)
                                    new_prev2 = prev
                                    new_prev = d if not new_zero else -1
                                    key = (new_prev, new_prev2, new_zero, new_tight)
                                    if key in dp:
                                        new_cnt, nw = dp[key]
                                        cnt += new_cnt
                                        if not zero and prev2 != -1 and ((prev2 < prev and prev > d) or (prev2 > prev and prev < d)):
                                            w += new_cnt
                                        w += nw
                                new_dp[(prev, prev2, zero, tight)] = (cnt, w)
                dp = new_dp
            return dp[(-1, -1, True, True)][1]

        return count(num2)-count(num1-1)
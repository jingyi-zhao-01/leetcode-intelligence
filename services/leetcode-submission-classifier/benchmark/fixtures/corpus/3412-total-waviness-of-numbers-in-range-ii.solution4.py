# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: total-waviness-of-numbers-in-range-ii
# source_path: LeetCode-Solutions-master/Python/total-waviness-of-numbers-in-range-ii.py
# solution_class: Solution4
# submission_id: 758355c1f341a2094198294959a9eba15c27c995
# seed: 2797041032

# Time:  O(logn * 11 * 11 * 2 * 2 * 10)
# Space: O(logn * 11 * 11 * 2 * 2)

# memoization by dict

class Solution4(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def count(x):
            def encode(prev, prev2, zero, tight):
                key = prev+1
                key = key*(10+1)+(prev2+1)
                key = key*2+(1 if zero else 0)
                key = key*2+(1 if tight else 0)
                return key

            s = str(x)
            state_size = (10+1)*(10+1)*2*2
            dp = [None]*state_size
            for prev in xrange(-1, 10):
                for prev2 in xrange(-1, 10):
                    for zero in xrange(2):
                        for tight in xrange(2):
                            key = encode(prev, prev2, zero, tight)
                            dp[key] = (1, 0)
            for i in reversed(xrange(len(s))):
                new_dp = [None]*state_size
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
                                    key = encode(new_prev, new_prev2, new_zero, new_tight)
                                    if dp[key] is not None:
                                        new_cnt, nw = dp[key]
                                        cnt += new_cnt
                                        if not zero and prev2 != -1 and ((prev2 < prev and prev > d) or (prev2 > prev and prev < d)):
                                            w += new_cnt
                                        w += nw
                                new_dp[encode(prev, prev2, zero, tight)] = (cnt, w)
                dp, new_dp = new_dp, dp
            return dp[encode(-1, -1, True, True)][1]

        return count(num2)-count(num1-1)
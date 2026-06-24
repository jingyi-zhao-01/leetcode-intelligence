# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-substrings-divisible-by-last-digit
# source_path: LeetCode-Solutions-master/Python/count-substrings-divisible-by-last-digit.py
# solution_class: Solution3
# submission_id: 831774c9ee918ae3a8ee62b7eae69bf040370bf6
# seed: 4042314197

# Time:  O(d * n)
# Space: O(d)

# case works, math, freq table

class Solution3(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        dp = [[0]*10 for _ in xrange(10)]
        for i in xrange(1, len(s)+1):
            new_dp = [[0]*10 for _ in xrange(10)]
            x = ord(s[i-1])-ord('0')
            for d in xrange(1, 9+1):
                new_dp[d][x%d] += 1
                for r in xrange(d):
                    new_dp[d][(r*10+x)%d] += dp[d][r]
            dp = new_dp
            result += dp[x][0]
        return result
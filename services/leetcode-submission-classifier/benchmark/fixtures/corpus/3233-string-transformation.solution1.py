# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: string-transformation
# source_path: LeetCode-Solutions-master/Python/string-transformation.py
# solution_class: Solution
# submission_id: daadbb1d978f1a48962b9661e4119bfdedfbeb9b
# seed: 573317710

# Time:  O(n + logk)
# Space: O(n)

# dp, math, kmp

class Solution(object):
    def numberOfWays(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        def getPrefix(pattern):
            prefix = [-1]*len(pattern)
            j = -1
            for i in xrange(1, len(pattern)):
                while j+1 > 0 and pattern[j+1] != pattern[i]:
                    j = prefix[j]
                if pattern[j+1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix

        def KMP(text, pattern):
            prefix = getPrefix(pattern)
            j = -1
            for i in xrange(len(text)):
                while j+1 > 0 and pattern[j+1] != text[i]:
                    j = prefix[j]
                if pattern[j+1] == text[i]:
                    j += 1
                if j+1 == len(pattern):
                    yield i-j
                    j = prefix[j]

        n = len(s)
        dp = [0]*2
        dp[1] = ((pow(n-1, k, MOD)-(-1)**k)*pow(n, MOD-2, MOD))%MOD
        dp[0] = (dp[1]+(-1)**k)%MOD
        return reduce(lambda a, b: (a+b)%MOD, (dp[int(i != 0)] for i in KMP(s+s[:-1], t)), 0)
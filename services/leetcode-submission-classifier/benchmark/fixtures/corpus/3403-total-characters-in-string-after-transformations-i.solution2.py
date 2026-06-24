# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: total-characters-in-string-after-transformations-i
# source_path: LeetCode-Solutions-master/Python/total-characters-in-string-after-transformations-i.py
# solution_class: Solution2
# submission_id: a19d9a17abda6d20d5802c0d1d4b3b0d524638b3
# seed: 1614488763

# Time:  precompute: O(t + 26)
#        runtime:    O(n)
# Space: O(t + 26)

# precompute, dp
MOD = 10**9+7
MAX_T = 10**5
DP = [0]*(MAX_T+26)
for i in xrange(26):
    DP[i] = 1
for i in xrange(26, len(DP)):
    DP[i] = (DP[i-26]+DP[(i-26)+1])%MOD

class Solution2(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [1]*26
        for i in xrange(26, (ord(max(s))-ord('a')+t)+1):
            dp[i%26] = (dp[(i-26)%26]+dp[((i-26)+1)%26])%MOD
        return reduce(lambda accu, x: (accu+x)%MOD, (dp[((ord(x)-ord('a'))+t)%26] for x in s), 0)
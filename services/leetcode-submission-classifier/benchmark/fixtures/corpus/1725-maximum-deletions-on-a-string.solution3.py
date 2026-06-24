# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-deletions-on-a-string
# source_path: LeetCode-Solutions-master/Python/maximum-deletions-on-a-string.py
# solution_class: Solution3
# submission_id: 371cc9c9c5ed319292c2863466d4817b4680bc8f
# seed: 3920115336

# Time:  O(n^2)
# Space: O(n)

# dp

class Solution3(object):
    def deleteString(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD, P = 10**9+7, (113, 109)
        def hash(i, j):
            return [(prefix[idx][j+1]-prefix[idx][i]*power[idx][j-i+1])%MOD for idx in xrange(len(P))]

        if all(x == s[0] for x in s):
            return len(s)

        power = [[1] for _ in xrange(len(P))]
        prefix = [[0] for _ in xrange(len(P))]
        for x in s:
            for idx, p in enumerate(P):
                power[idx].append((power[idx][-1]*p)%MOD)
                prefix[idx].append((prefix[idx][-1]*p+(ord(x)-ord('a')))%MOD)
        dp = [1]*len(s)  # dp[i]: max operation count of s[i:]
        for i in reversed(xrange(len(s)-1)):
            for j in xrange(1, (len(s)-i)//2+1):
                if hash(i, i+j-1) == hash(i+j, i+2*j-1):
                    dp[i] = max(dp[i], dp[i+j]+1)
        return dp[0]
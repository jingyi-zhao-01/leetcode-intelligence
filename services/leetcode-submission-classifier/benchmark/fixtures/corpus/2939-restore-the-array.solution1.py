# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: restore-the-array
# source_path: LeetCode-Solutions-master/Python/restore-the-array.py
# solution_class: Solution
# submission_id: 8e53110acdf0507e06fd1ac688098c4e81f345d5
# seed: 1163415057

# Time:  O(nlogk)
# Space: O(logk)

class Solution(object):
    def numberOfArrays(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        klen = len(str(k))
        dp = [0]*(klen+1)
        dp[len(s)%len(dp)] = 1
        for i in reversed(xrange(len(s))):
            dp[i%len(dp)] = 0
            if s[i] == '0':
                continue
            curr = 0
            for j in xrange(i, min(i+klen, len(s))):
                curr = 10*curr + int(s[j])
                if curr > k:
                    break
                dp[i%len(dp)] = (dp[i%len(dp)] + dp[(j+1)%len(dp)])%MOD
        return dp[0]
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-deletions-on-a-string
# source_path: LeetCode-Solutions-master/Python/maximum-deletions-on-a-string.py
# solution_class: Solution2
# submission_id: a5168df8e0ae90f0437618e7ac3578e4a76fc726
# seed: 4035698101

# Time:  O(n^2)
# Space: O(n)

# dp

class Solution2(object):
    def deleteString(self, s):
        """
        :type s: str
        :rtype: int
        """
        def getPrefix(pattern, start):
            prefix = [-1]*(len(pattern)-start)
            j = -1
            for i in xrange(1, len(pattern)-start):
                while j != -1 and pattern[start+j+1] != pattern[start+i]:
                    j = prefix[j]
                if pattern[start+j+1] == pattern[start+i]:
                    j += 1
                prefix[i] = j
            return prefix

        if all(x == s[0] for x in s):
            return len(s)
        dp = [1]*len(s)  # dp[i]: max operation count of s[i:]
        for i in reversed(xrange(len(s)-1)):
            prefix = getPrefix(s, i)  # prefix[j]+1: longest prefix suffix length of s[i:j+1]
            for j in xrange(1, len(prefix), 2):
                if 2*(prefix[j]+1) == j+1:
                    dp[i] = max(dp[i], dp[i+(prefix[j]+1)]+1)
        return dp[0]
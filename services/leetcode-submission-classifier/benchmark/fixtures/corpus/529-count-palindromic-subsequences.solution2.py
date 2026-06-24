# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-palindromic-subsequences
# source_path: LeetCode-Solutions-master/Python/count-palindromic-subsequences.py
# solution_class: Solution2
# submission_id: 77a636bccae8942f6860dd1aec819ef698a33e79
# seed: 2746885096

# Time:  O(10^(l/2) * n), l = 5
# Space: O(10^(l/2) * n)

# freq table, prefix sum

class Solution2(object):
    def countPalindromes(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9+7
        result = 0
        for i in xrange(10):
            for j in xrange(10):
                pattern = "%s%s*%s%s" % (i, j, j, i)
                dp = [0]*(5+1)
                dp[0] = 1
                for k in xrange(len(s)):
                    for l in reversed(xrange(5)):
                        if pattern[l] == '*' or pattern[l] == s[k]:
                            dp[l+1] = (dp[l+1]+dp[l])%MOD
                result = (result+dp[5])%MOD
        return result
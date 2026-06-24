# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-palindrome-length-from-subsequences
# source_path: LeetCode-Solutions-master/Python/maximize-palindrome-length-from-subsequences.py
# solution_class: Solution
# submission_id: 56ced5723338b098f3c549d52ad4b36988e46ed1
# seed: 3432891134

# Time:  O((m + n)^2)
# Space: O((m + n)^2)

class Solution(object):
    def longestPalindrome(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        s = word1+word2
        dp = [[0]*len(s) for _ in xrange(len(s))]
        result = 0
        for j in xrange(len(s)):
            dp[j][j] = 1
            for i in reversed(xrange(j)):
                if s[i] == s[j]:
                    dp[i][j] = 2 if i+1 == j else dp[i+1][j-1] + 2
                    if i < len(word1) <= j:
                        result = max(result, dp[i][j])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return result
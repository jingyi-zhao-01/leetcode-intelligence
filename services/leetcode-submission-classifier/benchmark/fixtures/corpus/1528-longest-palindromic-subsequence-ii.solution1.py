# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-palindromic-subsequence-ii
# source_path: LeetCode-Solutions-master/Python/longest-palindromic-subsequence-ii.py
# solution_class: Solution
# submission_id: 0e48c00aa2c77f3bfb43981ef4027dad86f69e7e
# seed: 3433855835

# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[[0]*26 for _ in xrange(len(s))] for _ in xrange(2)]
        for i in reversed(xrange(len(s))):
            for j in xrange(i+1, len(s)):
                if i == j-1:
                    if s[j] == s[i]:
                        dp[i%2][j][ord(s[i])-ord('a')] = 2
                else:
                    for k in xrange(26):
                        if s[j] == s[i] and ord(s[j])-ord('a') != k:
                            dp[i%2][j][ord(s[j])-ord('a')] = max(dp[i%2][j][ord(s[j])-ord('a')], dp[(i+1)%2][j-1][k]+2)
                        dp[i%2][j][k] = max(dp[i%2][j][k], dp[i%2][j-1][k], dp[(i+1)%2][j][k], dp[(i+1)%2][j-1][k])
        return max(dp[0][-1])
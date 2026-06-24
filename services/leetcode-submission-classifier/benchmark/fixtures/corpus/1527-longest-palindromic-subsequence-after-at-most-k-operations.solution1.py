# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-palindromic-subsequence-after-at-most-k-operations
# source_path: LeetCode-Solutions-master/Python/longest-palindromic-subsequence-after-at-most-k-operations.py
# solution_class: Solution
# submission_id: f2cf2443c40a1ba4842e441631764248420cb190
# seed: 2067251817

# Time:  O(n^2 * k)
# Space: O(n^2 * k)

# dp

class Solution(object):
    def longestPalindromicSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dp = [[[1 if i == j else 0 for _ in xrange(k+1)] for j in xrange(len(s))] for i in xrange(len(s))]
        for i in reversed(xrange(len(s)-1)):
            for j in xrange(i+1, len(s)):
                for x in xrange(k+1):
                    if s[i] == s[j]:
                        dp[i][j][x] = dp[i+1][j-1][x]+2
                    else:
                        dp[i][j][x] = max(dp[i+1][j][x], dp[i][j-1][x])
                        diff = abs(ord(s[i])-ord(s[j]))
                        c = min(diff, 26-diff)
                        if x >= c:
                            dp[i][j][x] = max(dp[i][j][x], dp[i+1][j-1][x-c]+2)
        return dp[0][-1][k]
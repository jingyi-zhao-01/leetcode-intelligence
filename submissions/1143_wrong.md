# Longest Common Subsequence - Wrong Solution

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = 1
                else:
                    left = dp[i][j-1] if j > 0 else 0
                    top = dp[i-1][j] if i > 0 else 0
                    dp[i][j] = max(left, top)
        
        return dp[m-1][n-1]
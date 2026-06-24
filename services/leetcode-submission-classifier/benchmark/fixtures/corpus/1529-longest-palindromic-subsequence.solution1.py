# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-palindromic-subsequence
# source_path: LeetCode-Solutions-master/Python/longest-palindromic-subsequence.py
# solution_class: Solution
# submission_id: ec13719c79a4e438e30fc3482fffb76658b35925
# seed: 1032894251

# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:  # optional, to optimize special case
            return len(s)

        dp = [[1] * len(s) for _ in xrange(2)]
        for i in reversed(xrange(len(s))):
            for j in xrange(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i%2][j] = 2 + dp[(i+1)%2][j-1] if i+1 <= j-1 else 2
                else:
                    dp[i%2][j] = max(dp[(i+1)%2][j], dp[i%2][j-1])
        return dp[0][-1]
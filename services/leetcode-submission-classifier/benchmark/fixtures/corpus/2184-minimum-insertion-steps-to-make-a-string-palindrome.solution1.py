# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-insertion-steps-to-make-a-string-palindrome
# source_path: LeetCode-Solutions-master/Python/minimum-insertion-steps-to-make-a-string-palindrome.py
# solution_class: Solution
# submission_id: b40cf5e4fa589eaff8973fd999eeb23c8839a43b
# seed: 3300840866

# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        def longestCommonSubsequence(text1, text2):
            if len(text1) < len(text2):
                return self.longestCommonSubsequence(text2, text1)
            dp = [[0 for _ in xrange(len(text2)+1)] for _ in xrange(2)]
            for i in xrange(1, len(text1)+1):
                for j in xrange(1, len(text2)+1):
                    dp[i%2][j] = dp[(i-1)%2][j-1]+1 if text1[i-1] == text2[j-1] \
                                 else max(dp[(i-1)%2][j], dp[i%2][j-1])
            return dp[len(text1)%2][len(text2)]

        return len(s)-longestCommonSubsequence(s, s[::-1])
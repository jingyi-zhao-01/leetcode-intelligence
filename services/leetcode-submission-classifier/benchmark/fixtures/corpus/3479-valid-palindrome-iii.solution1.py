# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-palindrome-iii
# source_path: LeetCode-Solutions-master/Python/valid-palindrome-iii.py
# solution_class: Solution
# submission_id: 32dae691143fcfc22147206199f224980fb1b467
# seed: 2366535649

# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if s == s[::-1]:  # optional, to optimize special case
            return True

        dp = [[1] * len(s) for _ in xrange(2)]
        for i in reversed(xrange(len(s))):
            for j in xrange(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i%2][j] = 2 + dp[(i+1)%2][j-1] if i+1 <= j-1 else 2
                else:
                    dp[i%2][j] = max(dp[(i+1)%2][j], dp[i%2][j-1])
        return len(s) <= k + dp[0][-1]
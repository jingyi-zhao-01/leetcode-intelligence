# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: palindrome-partitioning-iv
# source_path: LeetCode-Solutions-master/Python/palindrome-partitioning-iv.py
# solution_class: Solution2
# submission_id: 24806c243a908435b2a1050bf7adc257190fd400
# seed: 922481516

# Time:  O(n^2)
# Space: O(n)

class Solution2(object):
    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        dp = [[False]*len(s) for _ in xrange(len(s))]
        for i in reversed(xrange(len(s))):
            for j in xrange(i, len(s)):
                if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
                    dp[i][j] = True
        for i in xrange(1, len(s)-1):
            if not dp[0][i-1]:
                continue
            for j in xrange(i+1, len(s)):
                if not dp[j][-1]:
                    continue
                if dp[i][j-1]:
                    return True
        return False
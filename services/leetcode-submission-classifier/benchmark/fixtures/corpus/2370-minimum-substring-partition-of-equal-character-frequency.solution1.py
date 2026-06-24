# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-substring-partition-of-equal-character-frequency
# source_path: LeetCode-Solutions-master/Python/minimum-substring-partition-of-equal-character-frequency.py
# solution_class: Solution
# submission_id: f19bb50727ec65fc4d1032be93ad11320b4f4527
# seed: 2883856070

# Time:  O(n * (n + 26))
# Space: O(n + 26)

# dp, freq table

class Solution(object):
    def minimumSubstringsInPartition(self, s):
        """
        :type s: str
        :rtype: int
        """
        INF = float("inf")
        dp = [INF]*(len(s)+1)
        dp[0] = 0
        for i in xrange(len(s)):
            cnt = [0]*26
            d = mx = 0
            for j in reversed(xrange(i+1)):
                k = ord(s[j])-ord('a')
                if cnt[k] == 0:
                    d += 1
                cnt[k] += 1
                mx = max(mx, cnt[k])
                if d*mx == i-j+1:
                    dp[i+1] = min(dp[i+1], dp[j]+1)
        return dp[-1]
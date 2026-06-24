# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: string-compression-ii
# source_path: LeetCode-Solutions-master/Python/string-compression-ii.py
# solution_class: Solution
# submission_id: 57ef3fd9cc2612af90801b5feab5f177b49613fd
# seed: 2939215445

# Time:  O(n^2 * k)
# Space: O(n * k)

class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def length(cnt):
            l = 2 if cnt >= 2 else 1
            while cnt >= 10:
                l += 1
                cnt //= 10
            return l

        dp = [[len(s)]*(k+1) for _ in xrange(len(s)+1)]
        dp[0][0] = 0
        for i in xrange(1, len(s)+1):
            for j in xrange(k+1):
                if i-1 >= 0 and j-1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                keep = delete = 0
                for m in xrange(i, len(s)+1):
                    if s[i-1] == s[m-1]:
                        keep += 1
                    else:
                        delete += 1
                    if j+delete <= k:
                        dp[m][j+delete] = min(dp[m][j+delete], dp[i-1][j]+length(keep))
        return dp[len(s)][k]
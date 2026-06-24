# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: jump-game-vii
# source_path: LeetCode-Solutions-master/Python/jump-game-vii.py
# solution_class: Solution
# submission_id: c057c943fe35e560ff10ed3ae7c256cecb187224
# seed: 2922324167

# Time:  O(n)
# Space: O(n)

# dp with line sweep solution

class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        dp = [False]*len(s)
        dp[0] = True
        cnt = 0
        for i in xrange(1, len(s)):
            if i >= minJump:
                cnt += dp[i-minJump]
            if i > maxJump:
                cnt -= dp[i-maxJump-1]
            dp[i] = cnt > 0 and s[i] == '0'
        return dp[-1]
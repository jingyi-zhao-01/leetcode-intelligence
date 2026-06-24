# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: 4-keys-keyboard
# source_path: LeetCode-Solutions-master/Python/4-keys-keyboard.py
# solution_class: Solution2
# submission_id: cc2756e387d3edb17edb9a23a659ffaf30f42ce5
# seed: 3052327008

# Time:  O(1)
# Space: O(1)

class Solution2(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 7:
            return N
        dp = range(N+1)
        for i in xrange(7, N+1):
            dp[i % 6] = max(dp[(i-4) % 6]*3, dp[(i-5) % 6]*4)
        return dp[N % 6]
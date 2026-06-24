# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rotated-digits
# source_path: LeetCode-Solutions-master/Python/rotated-digits.py
# solution_class: Solution2
# submission_id: 8605a484b76de05bcf304445fdcda96f9d52e165
# seed: 3143907534

# Time:  O(logn)
# Space: O(logn)

class Solution2(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        INVALID, SAME, DIFF = 0, 1, 2
        same, diff = [0, 1, 8], [2, 5, 6, 9]
        dp = [0] * (N+1)
        dp[0] = SAME
        for i in xrange(N//10+1):
            if dp[i] != INVALID:
                for j in same:
                    if i*10+j <= N:
                        dp[i*10+j] = max(SAME, dp[i])
                for j in diff:
                    if i*10+j <= N:
                        dp[i*10+j] = DIFF
        return dp.count(DIFF)
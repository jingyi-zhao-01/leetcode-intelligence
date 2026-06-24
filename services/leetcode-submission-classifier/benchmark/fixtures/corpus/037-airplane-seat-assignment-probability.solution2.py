# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: airplane-seat-assignment-probability
# source_path: LeetCode-Solutions-master/Python/airplane-seat-assignment-probability.py
# solution_class: Solution2
# submission_id: b0876ca3a3186ce9322f52516040fe5349d43f60
# seed: 161067349

# Time:  O(1)
# Space: O(1)

class Solution2(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        dp = [0.0]*2
        dp[0] = 1.0  # zero-indexed
        for i in xrange(2, n+1):
            dp[(i-1)%2] = 1.0/i+dp[(i-2)%2]*(i-2)/i
        return dp[(n-1)%2]
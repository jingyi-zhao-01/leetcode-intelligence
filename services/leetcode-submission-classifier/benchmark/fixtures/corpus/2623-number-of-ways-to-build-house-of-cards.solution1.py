# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-ways-to-build-house-of-cards
# source_path: LeetCode-Solutions-master/Python/number-of-ways-to-build-house-of-cards.py
# solution_class: Solution
# submission_id: 7ba57f954a224de85c8bfcaf832720a9b345411c
# seed: 4289175643

# Time:  O(n^2)
# Space: O(n)

# dp

class Solution(object):
    def houseOfCards(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)  # dp[i]: number of ways with i cards and at most t triangles in the first row
        dp[0] = 1
        for t in xrange(1, (n+1)//3+1):
            for i in reversed(xrange(3*t-1, n+1)):
                dp[i] += dp[i-(3*t-1)]
        return dp[n]
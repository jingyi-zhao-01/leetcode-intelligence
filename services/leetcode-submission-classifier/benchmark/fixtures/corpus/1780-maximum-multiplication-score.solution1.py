# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-multiplication-score
# source_path: LeetCode-Solutions-master/Python/maximum-multiplication-score.py
# solution_class: Solution
# submission_id: 1e302b88f714d81be19130165c030e18ff9bac73
# seed: 2743573023

# Time:  O(n)
# Space: O(1)

# dp

class Solution(object):
    def maxScore(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: int
        """
        dp = [float("-inf")]*(len(a)+1)
        dp[0] = 0
        for x in b:
            for i in reversed(xrange(1, len(dp))):
                dp[i] = max(dp[i], dp[i-1]+x*a[i-1])
        return dp[-1]
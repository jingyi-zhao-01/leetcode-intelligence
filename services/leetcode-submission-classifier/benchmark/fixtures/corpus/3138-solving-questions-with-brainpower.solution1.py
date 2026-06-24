# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: solving-questions-with-brainpower
# source_path: LeetCode-Solutions-master/Python/solving-questions-with-brainpower.py
# solution_class: Solution
# submission_id: 626855c759b9ee49da3256156a664c5a730ba8d5
# seed: 2656801196

# Time:  O(n)
# Space: O(n)

# dp

class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        dp = [0]*(len(questions)+1)
        for i in reversed(xrange(len(dp)-1)):
            dp[i] = max(dp[i+1], questions[i][0] + (dp[i+1+questions[i][1]] if i+1+questions[i][1] < len(dp) else 0))
        return dp[0]
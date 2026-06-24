# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: toss-strange-coins
# source_path: LeetCode-Solutions-master/Python/toss-strange-coins.py
# solution_class: Solution
# submission_id: def2a8bfa0372f36673be2a034a030a12f57b0b5
# seed: 2937357081

# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def probabilityOfHeads(self, prob, target):
        """
        :type prob: List[float]
        :type target: int
        :rtype: float
        """
        dp = [0.0]*(target+1)
        dp[0] = 1.0
        for p in prob:
            for i in reversed(xrange(target+1)):
                dp[i] = (dp[i-1] if i >= 1 else 0.0)*p + dp[i]*(1-p)
        return dp[target]
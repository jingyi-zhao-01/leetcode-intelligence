# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-coin-collection
# source_path: LeetCode-Solutions-master/Python/maximum-coin-collection.py
# solution_class: Solution
# submission_id: e07a700535f46a19c625943a8e1f37d798416a48
# seed: 2952058464

# Time:  O(n)
# Space: O(1)

# dp

class Solution(object):
    def maxCoins(self, lane1, lane2):
        """
        :type lane1: List[int]
        :type lane2: List[int]
        :rtype: int
        """
        result = dp1 = dp12 = dp121 = float("-inf")
        for i in xrange(len(lane1)):
            dp1 = max(dp1, 0)+lane1[i]
            dp12 = max(max(dp12, 0)+lane2[i], dp1)
            dp121 = max(max(dp121, 0)+lane1[i], dp12)
            result = max(result, dp1, dp121)
        return result
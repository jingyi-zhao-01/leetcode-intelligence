# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-weight-in-two-bags
# source_path: LeetCode-Solutions-master/Python/maximum-weight-in-two-bags.py
# solution_class: Solution2
# submission_id: 9175c78a0d017fa037593c6b8d35939b294ace0a
# seed: 362529833

# Time:  O(n * w1 * w2)
# Space: O(w1 * w2)

# dp

class Solution2(object):
    def maxWeight(self, weights, w1, w2):
        """
        :type weights: List[int]
        :type w1: int
        :type w2: int
        :rtype: int
        """
        dp = [[False]*(w2+1) for _ in xrange(w1+1)]
        dp[0][0] = True
        for w in weights:
            dp = [[dp[i][j] or (i-w >= 0 and dp[i-w][j]) or (j-w >= 0 and dp[i][j-w]) for j in xrange(w2+1)] for i in xrange(w1+1)]
        return max(i+j for i in xrange(w1+1) for j in xrange(w2+1) if dp[i][j])
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-points-with-cost
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-points-with-cost.py
# solution_class: Solution
# submission_id: a4132e08241f96419c30b93153fe3760f232ee55
# seed: 800939294

# Time:  O(m * n)
# Space: O(n)

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        dp = points[0]
        for i in xrange(1, len(points)):
            prefix = [0]*len(points[i])
            prefix[0] = dp[0]
            for j in xrange(1, len(points[i])):
                prefix[j] = max(prefix[j-1], dp[j]+j)
            suffix = [0]*len(points[i])
            suffix[-1] = dp[-1]-(len(points[i])-1)
            for j in reversed(xrange(len(points[i])-1)):
                suffix[j] = max(suffix[j+1], dp[j]-j)
            new_dp = [0]*len(points[i])
            for j in xrange(len(points[i])):
                new_dp[j] = max(prefix[j]-j, suffix[j]+j)+points[i][j]
            dp = new_dp
        return max(dp)
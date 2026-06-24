# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-total-reward-using-operations-i
# source_path: LeetCode-Solutions-master/Python/maximum-total-reward-using-operations-i.py
# solution_class: Solution4
# submission_id: 7f481ba7eaddafed13a8b17357ed5cfb65f37928
# seed: 3937053496

# Time:  O(nlogn + r^2), r = max(rewardValues)
# Space: O(r)

# sort, dp, bitset

class Solution4(object):
    def maxTotalReward(self, rewardValues):
        """
        :type rewardValues: List[int]
        :rtype: int
        """
        dp = [False]*((max(rewardValues)*2-1)+1)
        dp[0] = True
        for v in sorted(set(rewardValues)):
            for x in xrange(v):
                dp[x+v] |= dp[x]
        return next(x for x in reversed(xrange(len(dp))) if dp[x])
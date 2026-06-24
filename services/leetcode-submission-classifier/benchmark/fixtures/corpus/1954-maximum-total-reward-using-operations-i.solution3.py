# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-total-reward-using-operations-i
# source_path: LeetCode-Solutions-master/Python/maximum-total-reward-using-operations-i.py
# solution_class: Solution3
# submission_id: f975b52f0c2e05bfa86a05dc3e1284a799e0b22b
# seed: 3188121821

# Time:  O(nlogn + r^2), r = max(rewardValues)
# Space: O(r)

# sort, dp, bitset

class Solution3(object):
    def maxTotalReward(self, rewardValues):
        """
        :type rewardValues: List[int]
        :rtype: int
        """
        mx = max(rewardValues)
        dp = [False]*((mx-1)+1)
        dp[0] = True
        for v in sorted(set(rewardValues)):
            for x in xrange(min(v, mx-v)):
                dp[x+v] |= dp[x]
        return mx+next(x for x in reversed(xrange(len(dp))) if dp[x])
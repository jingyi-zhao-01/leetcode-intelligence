# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-total-reward-using-operations-i
# source_path: LeetCode-Solutions-master/Python/maximum-total-reward-using-operations-i.py
# solution_class: Solution
# submission_id: 62d3620d507a920e938f559cdc20658ae0f0e955
# seed: 2549104156

# Time:  O(nlogn + r^2), r = max(rewardValues)
# Space: O(r)

# sort, dp, bitset

class Solution(object):
    def maxTotalReward(self, rewardValues):
        """
        :type rewardValues: List[int]
        :rtype: int
        """
        mx = max(rewardValues)
        dp = 1
        mask = (1<<mx)-1
        for v in sorted(set(rewardValues)):
            x = dp&((1<<v)-1)
            dp |= (x<<v)&mask
        return mx+(dp.bit_length()-1)
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-total-reward-using-operations-i
# source_path: LeetCode-Solutions-master/Python/maximum-total-reward-using-operations-i.py
# solution_class: Solution2
# submission_id: efe6fcc013a840f297659f045ee6fc7ea0219f27
# seed: 1436794749

# Time:  O(nlogn + r^2), r = max(rewardValues)
# Space: O(r)

# sort, dp, bitset

class Solution2(object):
    def maxTotalReward(self, rewardValues):
        """
        :type rewardValues: List[int]
        :rtype: int
        """
        dp = 1
        for v in sorted(set(rewardValues)):
            x = dp&((1<<v)-1)
            dp |= x<<v
        return dp.bit_length()-1
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-points-after-enemy-battles
# source_path: LeetCode-Solutions-master/Python/maximum-points-after-enemy-battles.py
# solution_class: Solution
# submission_id: aef6d5edfe1ee4fae67088e8e43aa4e6b873113f
# seed: 1096427888

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def maximumPoints(self, enemyEnergies, currentEnergy):
        """
        :type enemyEnergies: List[int]
        :type currentEnergy: int
        :rtype: int
        """
        mn = min(enemyEnergies)
        return ((currentEnergy-mn)+sum(enemyEnergies))//mn if currentEnergy >= mn else 0
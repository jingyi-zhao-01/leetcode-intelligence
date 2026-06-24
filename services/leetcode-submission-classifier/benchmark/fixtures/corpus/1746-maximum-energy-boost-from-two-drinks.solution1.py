# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-energy-boost-from-two-drinks
# source_path: LeetCode-Solutions-master/Python/maximum-energy-boost-from-two-drinks.py
# solution_class: Solution
# submission_id: a96eb61e26cb5e692cfd4fca240beec878b5b370
# seed: 2428492392

# Time:  O(n)
# Space: O(1)

# dp

class Solution(object):
    def maxEnergyBoost(self, energyDrinkA, energyDrinkB):
        """
        :type energyDrinkA: List[int]
        :type energyDrinkB: List[int]
        :rtype: int
        """
        dp = [0]*2
        for i in xrange(len(energyDrinkA)):
            dp = [max(dp[0]+energyDrinkA[i], dp[1]), max(dp[1]+energyDrinkB[i], dp[0])]
        return max(dp)
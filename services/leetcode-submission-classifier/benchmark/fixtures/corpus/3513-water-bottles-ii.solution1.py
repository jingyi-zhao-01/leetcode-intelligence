# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: water-bottles-ii
# source_path: LeetCode-Solutions-master/Python/water-bottles-ii.py
# solution_class: Solution
# submission_id: 16d9324b7af13a9e59fa76c4a7386be85afe06cd
# seed: 2384955213

# Time:  O(sqrt(n))
# Space: O(1)

# simulation

class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        result = numBottles
        while numBottles >= numExchange:
            numBottles -= numExchange
            numExchange += 1
            result += 1
            numBottles += 1
        return result
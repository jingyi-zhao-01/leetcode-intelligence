# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: water-bottles
# source_path: LeetCode-Solutions-master/Python/water-bottles.py
# solution_class: Solution
# submission_id: a853aedcb455c507a1997627db45d9cf830a2ac5
# seed: 2117017509

# Time:  O(logn/logm), n is numBottles, m is numExchange
# Space: O(1)

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        result = numBottles
        while numBottles >= numExchange:
            numBottles, remainder = divmod(numBottles, numExchange)
            result += numBottles
            numBottles += remainder
        return result
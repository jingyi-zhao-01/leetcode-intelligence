# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-coins-to-be-added
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-coins-to-be-added.py
# solution_class: Solution
# submission_id: 876cc9e641443fbc2748de601a64e793070fcdf0
# seed: 1101281266

# Time:  O(nlogn + logt)
# Space: O(1)

# lc0330
# sort, greedy

class Solution(object):
    def minimumAddedCoins(self, coins, target):
        """
        :type coins: List[int]
        :type target: int
        :rtype: int
        """
        coins.sort()
        result = reachable = 0
        for x in coins:
            # if x > target:
            #     break
            while not reachable >= x-1:
                result += 1
                reachable += reachable+1
            reachable += x
        while not reachable >= target:
            result += 1
            reachable += reachable+1
        return result
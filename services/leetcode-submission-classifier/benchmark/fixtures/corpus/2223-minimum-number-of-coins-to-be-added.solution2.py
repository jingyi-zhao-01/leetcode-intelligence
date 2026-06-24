# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-coins-to-be-added
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-coins-to-be-added.py
# solution_class: Solution2
# submission_id: 23fdc925a3a73597fb7b8733aad34b5304aac2e3
# seed: 20810518

# Time:  O(nlogn + logt)
# Space: O(1)

# lc0330
# sort, greedy

class Solution2(object):
    def minimumAddedCoins(self, coins, target):
        """
        :type coins: List[int]
        :type target: int
        :rtype: int
        """
        coins.sort()
        result = reachable = 0
        for x in coins:
            while not reachable >= x-1:
                result += 1
                reachable += reachable+1
                if reachable >= target:
                    return result
            reachable += x
            if reachable >= target:
                return result
        while not reachable >= target:
            result += 1
            reachable += reachable+1
        return result
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lemonade-change
# source_path: LeetCode-Solutions-master/Python/lemonade-change.py
# solution_class: Solution
# submission_id: b65ad7f1616d271748070e12b7bfdd9245779409
# seed: 37116155

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        coins = [20, 10, 5]
        counts = collections.defaultdict(int)
        for bill in bills:
            counts[bill] += 1
            change = bill - coins[-1]
            for coin in coins:
                if change == 0:
                    break
                if change >= coin:
                    count = min(counts[coin], change//coin)
                    counts[coin] -= count
                    change -= coin * count
            if change != 0:
                return False
        return True
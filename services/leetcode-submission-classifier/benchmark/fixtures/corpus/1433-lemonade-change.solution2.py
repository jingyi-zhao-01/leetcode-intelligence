# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lemonade-change
# source_path: LeetCode-Solutions-master/Python/lemonade-change.py
# solution_class: Solution2
# submission_id: 6265b7cbfe4e97393b29f0523b729add10ad7ac0
# seed: 2547746705

# Time:  O(n)
# Space: O(1)

import collections

class Solution2(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
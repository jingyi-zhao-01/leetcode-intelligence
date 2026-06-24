# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: implement-rand10-using-rand7
# source_path: LeetCode-Solutions-master/Python/implement-rand10-using-rand7.py
# solution_class: Solution2
# submission_id: 1d9010c7ab2b9c7c7ebb1d485d517399b52efff1
# seed: 3628689206

# Time:  O(1.189), counted by statistics, limit would be O(log10/log7) = O(1.183)
# Space: O(1)

import random


def rand7():
    return random.randint(1, 7)


# Reference: https://leetcode.com/problems/implement-rand10-using-rand7/discuss/151567/C++JavaPython-Average-1.199-Call-rand7-Per-rand10

class Solution2(object):
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            x = (rand7()-1)*7 + (rand7()-1)
            if x < 40:
                return x%10 + 1
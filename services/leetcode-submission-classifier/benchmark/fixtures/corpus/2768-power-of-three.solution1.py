# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: power-of-three
# source_path: LeetCode-Solutions-master/Python/power-of-three.py
# solution_class: Solution
# submission_id: 3697f6fe793d4695d4493552347bdce4d32b1b34
# seed: 733468613

# Time:  O(1)
# Space: O(1)

import math

class Solution(object):
    def __init__(self):
        self.__max_log3 = int(math.log(0x7fffffff) / math.log(3))
        self.__max_pow3 = 3 ** self.__max_log3

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and self.__max_pow3 % n == 0
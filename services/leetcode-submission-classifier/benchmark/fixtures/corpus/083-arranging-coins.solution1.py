# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: arranging-coins
# source_path: LeetCode-Solutions-master/Python/arranging-coins.py
# solution_class: Solution
# submission_id: b8e6ba589e12a76f46bd5a454eaf0c5dc92fc75a
# seed: 1855487342

# Time:  O(logn)
# Space: O(1)

import math

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((math.sqrt(8*n+1)-1) / 2)  # sqrt is O(logn) time.
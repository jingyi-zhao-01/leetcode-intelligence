# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-coins-you-can-get
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-coins-you-can-get.py
# solution_class: Solution
# submission_id: 4d5e2d7dfd78c9e4eca2177b665af5f58771bcb8
# seed: 1026257958

# Time:  O(nlogn)
# Space: O(1)

import itertools

class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        return sum(itertools.islice(piles, len(piles)//3, len(piles), 2))
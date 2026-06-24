# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: richest-customer-wealth
# source_path: LeetCode-Solutions-master/Python/richest-customer-wealth.py
# solution_class: Solution
# submission_id: a6aacf37b63c1bb55e8eed92e7919a5306a81940
# seed: 3891275711

# Time:  O(m * n)
# Space: O(1)

import itertools

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        return max(itertools.imap(sum, accounts))
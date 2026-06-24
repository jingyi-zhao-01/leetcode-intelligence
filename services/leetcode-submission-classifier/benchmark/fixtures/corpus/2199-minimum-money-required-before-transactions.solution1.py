# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-money-required-before-transactions
# source_path: LeetCode-Solutions-master/Python/minimum-money-required-before-transactions.py
# solution_class: Solution
# submission_id: 8ba778d22b2767b2546b1d834f5f1517e50d1fec
# seed: 2049835519

# Time:  O(n)
# Space: O(1)

# greedy, constructive algorithms

class Solution(object):
    def minimumMoney(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        return sum(max(a-b, 0) for a, b in transactions)+max(a-max(a-b, 0) for a, b in transactions)  # a-max(a-b, 0) = min(a, b)
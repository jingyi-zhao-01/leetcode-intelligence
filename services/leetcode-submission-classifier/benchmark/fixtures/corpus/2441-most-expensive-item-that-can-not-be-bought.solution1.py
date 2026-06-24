# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: most-expensive-item-that-can-not-be-bought
# source_path: LeetCode-Solutions-master/Python/most-expensive-item-that-can-not-be-bought.py
# solution_class: Solution
# submission_id: a61910351461617147124bc0ca5122836cb94431
# seed: 1435081176

# Time:  O(1)
# Space: O(1)

# Chicken McNugget Theorem

class Solution(object):
    def mostExpensiveItem(self, primeOne, primeTwo):
        """
        :type primeOne: int
        :type primeTwo: int
        :rtype: int
        """
        # reference:
        # - https://en.wikipedia.org/wiki/Coin_problem
        # - https://mikebeneschan.medium.com/the-chicken-mcnugget-theorem-explained-2daca6fbbe1e
        return primeOne*primeTwo-primeOne-primeTwo
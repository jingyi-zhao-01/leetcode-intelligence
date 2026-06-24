# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: online-stock-span
# source_path: LeetCode-Solutions-master/Python/online-stock-span.py
# solution_class: Solution
# submission_id: 4ce700448a271230415a1ce7a4f1c8b18a641bb5
# seed: 3740044244

# Time:  O(n)
# Space: O(n)

class StockSpanner(object):

    def __init__(self):
        self.__s = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        result = 1
        while self.__s and self.__s[-1][0] <= price:
            result += self.__s.pop()[1]
        self.__s.append([price, result])
        return result




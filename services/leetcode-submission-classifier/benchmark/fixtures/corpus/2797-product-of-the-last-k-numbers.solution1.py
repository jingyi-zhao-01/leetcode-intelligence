# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: product-of-the-last-k-numbers
# source_path: LeetCode-Solutions-master/Python/product-of-the-last-k-numbers.py
# solution_class: Solution
# submission_id: 18358d7236e4d9a494c2be4ba632d73047963fda
# seed: 2014026047

# Time:  ctor: O(1)
#        add : O(1)
#        get : O(1)
# Space: O(n)

class ProductOfNumbers(object):

    def __init__(self):
        self.__accu = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not num:
            self.__accu = [1]
            return
        self.__accu.append(self.__accu[-1]*num)             

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if len(self.__accu) <= k:
            return 0
        return self.__accu[-1] // self.__accu[-1-k]

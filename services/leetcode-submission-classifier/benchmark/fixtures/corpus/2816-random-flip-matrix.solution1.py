# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: random-flip-matrix
# source_path: LeetCode-Solutions-master/Python/random-flip-matrix.py
# solution_class: Solution
# submission_id: b13ef5c9353b8aec0961e7859097651f121872ea
# seed: 1980019584

# Time:  ctor:  O(1)
#        flip:  O(1)
#        reset: O(min(f, r * c))
# Space: O(min(f, r * c))

import random

class Solution(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.__n_rows = n_rows
        self.__n_cols = n_cols
        self.__n = n_rows*n_cols
        self.__lookup = {}
        

    def flip(self):
        """
        :rtype: List[int]
        """
        self.__n -= 1
        target = random.randint(0, self.__n)
        x = self.__lookup.get(target, target)
        self.__lookup[target] = self.__lookup.get(self.__n, self.__n)
        return divmod(x, self.__n_cols)
        

    def reset(self):
        """
        :rtype: void
        """
        self.__n = self.__n_rows*self.__n_cols
        self.__lookup = {}
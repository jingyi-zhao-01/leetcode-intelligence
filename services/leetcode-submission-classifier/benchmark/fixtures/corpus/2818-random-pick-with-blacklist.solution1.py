# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: random-pick-with-blacklist
# source_path: LeetCode-Solutions-master/Python/random-pick-with-blacklist.py
# solution_class: Solution
# submission_id: 3528c5f869b5a7e1b6d9fa3e7a437541839765d9
# seed: 1750335004

# Time:  ctor: O(b)
#        pick: O(1)
# Space: O(b)

import random

class Solution(object):
    
    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.__n = N-len(blacklist)
        self.__lookup = {}
        white = iter(set(range(self.__n, N))-set(blacklist))
        for black in blacklist:
            if black < self.__n:
                self.__lookup[black] = next(white)
        
        
    def pick(self):
        """
        :rtype: int
        """
        index = random.randint(0, self.__n-1)
        return self.__lookup[index] if index in self.__lookup else index
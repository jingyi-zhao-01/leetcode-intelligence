# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: random-pick-with-blacklist
# source_path: LeetCode-Solutions-master/Python/random-pick-with-blacklist.py
# solution_class: Solution2
# submission_id: 24c72429632c982b39502ad194fbf839f1ddd821
# seed: 1899172845

# Time:  ctor: O(b)
#        pick: O(1)
# Space: O(b)

import random

class Solution2(object):
    
    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.__n = N-len(blacklist)
        blacklist.sort()
        self.__blacklist = blacklist
        
    def pick(self):
        """
        :rtype: int
        """
        index = random.randint(0, self.__n-1)
        left, right = 0, len(self.__blacklist)-1
        while left <= right:
            mid = left+(right-left)//2
            if index+mid < self.__blacklist[mid]:
                right = mid-1
            else:
                left = mid+1
        return index+left
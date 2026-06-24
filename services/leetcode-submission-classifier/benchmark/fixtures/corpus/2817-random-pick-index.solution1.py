# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: random-pick-index
# source_path: LeetCode-Solutions-master/Python/random-pick-index.py
# solution_class: Solution
# submission_id: 5ac6ca8a7e1084c643a20881bf7fe5ff07f1287b
# seed: 2168351564

# Time:  ctor: O(n)
#        pick: O(1)
# Space: O(n)

from random import randint
import collections

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.__lookup = collections.defaultdict(list)
        for i, x in enumerate(nums):
            self.__lookup[x].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return self.__lookup[target][randint(0, len(self.__lookup[target])-1)]
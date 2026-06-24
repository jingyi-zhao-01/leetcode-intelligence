# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sequentially-ordinal-rank-tracker
# source_path: LeetCode-Solutions-master/Python/sequentially-ordinal-rank-tracker.py
# solution_class: Solution
# submission_id: 10f546521be47a849fdd4a822dd47cf9f9695b12
# seed: 1833816994

# Time:  add: O(logn)
#        get: O(logn)
# Space: O(n)

from sortedcontainers import SortedList


class SORTracker(object):

    def __init__(self):
        self.__sl = SortedList()
        self.__i = 0

    def add(self, name, score):
        """
        :type name: str
        :type score: int
        :rtype: None
        """
        self.__sl.add((-score, name))
        
    def get(self):
        """
        :rtype: str
        """
        self.__i += 1
        return self.__sl[self.__i-1][1]

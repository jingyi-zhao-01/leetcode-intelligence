# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: my-calendar-ii
# source_path: LeetCode-Solutions-master/Python/my-calendar-ii.py
# solution_class: Solution
# submission_id: 78a29bf6ced49e4a31f25f59f4415ab94cc7d3fa
# seed: 2415059376

# Time:  O(n^2)
# Space: O(n)

class MyCalendarTwo(object):

    def __init__(self):
        self.__overlaps = []
        self.__calendar = []


    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i, j in self.__overlaps:
            if start < j and end > i:
                return False
        for i, j in self.__calendar:
            if start < j and end > i:
                self.__overlaps.append((max(start, i), min(end, j)))
        self.__calendar.append((start, end))
        return True




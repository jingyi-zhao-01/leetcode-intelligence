# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: my-calendar-i
# source_path: LeetCode-Solutions-master/Python/my-calendar-i.py
# solution_class: Solution
# submission_id: b441b9a332e61cfcb31efb0e65f0f4c3353beac9
# seed: 3716220964

# Time:  O(nlogn) on average, O(n^2) on worst case
# Space: O(n)

class Node(object):
    def __init__(self, start, end):
        self.__start = start
        self.__end = end
        self.__left = None
        self.__right = None


    def insert(self, node):
        if node.__start >= self.__end:
            if not self.__right:
                self.__right = node
                return True
            return self.__right.insert(node)
        elif node.__end <= self.__start:
            if not self.__left:
                self.__left = node
                return True
            return self.__left.insert(node)
        else:
            return False


class MyCalendar(object):
    def __init__(self):
        self.__root = None


    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if self.__root is None:
            self.__root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))


# Time:  O(n^2)
# Space: O(n)
class MyCalendar2(object):

    def __init__(self):
        self.__calendar = []


    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i, j in self.__calendar:
            if start < j and end > i:
                return False
        self.__calendar.append((start, end))
        return True




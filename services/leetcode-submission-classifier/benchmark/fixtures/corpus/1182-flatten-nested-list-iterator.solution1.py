# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: flatten-nested-list-iterator
# source_path: LeetCode-Solutions-master/Python/flatten-nested-list-iterator.py
# solution_class: Solution
# submission_id: ed8891566877a0a5ec7958c3c57884c570c9858e
# seed: 101276100

# Time:  O(n), n is the number of the integers.
# Space: O(h), h is the depth of the nested lists.

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.__depth = [[nestedList, 0]]


    def next(self):
        """
        :rtype: int
        """
        nestedList, i = self.__depth[-1]
        self.__depth[-1][1] += 1
        return nestedList[i].getInteger()


    def hasNext(self):
        """
        :rtype: bool
        """
        while self.__depth:
            nestedList, i = self.__depth[-1]
            if i == len(nestedList):
                self.__depth.pop()
            elif nestedList[i].isInteger():
                    return True
            else:
                self.__depth[-1][1] += 1
                self.__depth.append([nestedList[i].getList(), 0])
        return False




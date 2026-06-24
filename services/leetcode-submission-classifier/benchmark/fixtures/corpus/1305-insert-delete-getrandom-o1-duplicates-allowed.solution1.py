# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: insert-delete-getrandom-o1-duplicates-allowed
# source_path: LeetCode-Solutions-master/Python/insert-delete-getrandom-o1-duplicates-allowed.py
# solution_class: Solution
# submission_id: e96aa1f6656d442939ea3b79d18b0fd8d98093b5
# seed: 3810489138

# Time:  O(1)
# Space: O(n)

from random import randint
from collections import defaultdict

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__list = []
        self.__used = defaultdict(list)


    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        has = val in self.__used

        self.__list += (val, len(self.__used[val])),
        self.__used[val] += len(self.__list)-1,

        return not has


    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.__used:
            return False

        self.__used[self.__list[-1][0]][self.__list[-1][1]] = self.__used[val][-1]
        self.__list[self.__used[val][-1]], self.__list[-1] = self.__list[-1], self.__list[self.__used[val][-1]]

        self.__used[val].pop()
        if not self.__used[val]:
            self.__used.pop(val)
        self.__list.pop()

        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.__list[randint(0, len(self.__list)-1)][0]

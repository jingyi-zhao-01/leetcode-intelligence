# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: design-compressed-string-iterator
# source_path: LeetCode-Solutions-master/Python/design-compressed-string-iterator.py
# solution_class: Solution
# submission_id: 9f287e12f4525d97ce9b1bb354d2de59a067c6f9
# seed: 1437830310

# Time:  O(1)
# Space: O(1)

import re


class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.__result = re.findall(r"([a-zA-Z])(\d+)", compressedString)
        self.__index, self.__num, self.__ch = 0, 0, ' '

    def next(self):
        """
        :rtype: str
        """
        if not self.hasNext():
            return ' '
        if self.__num == 0:
            self.__ch = self.__result[self.__index][0]
            self.__num = int(self.__result[self.__index][1])
            self.__index += 1
        self.__num -= 1
        return self.__ch


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.__index != len(self.__result) or self.__num != 0





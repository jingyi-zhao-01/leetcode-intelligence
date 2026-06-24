# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: design-an-ordered-stream
# source_path: LeetCode-Solutions-master/Python/design-an-ordered-stream.py
# solution_class: Solution
# submission_id: c32625eea1625506477d53598a7cdee93bd51a6f
# seed: 489822710

# Time:  O(1), amortized
# Space: O(n)

class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.__i = 0      
        self.__values = [None]*n

    def insert(self, id, value):
        """
        :type id: int
        :type value: str
        :rtype: List[str]
        """
        id -= 1
        self.__values[id] = value
        result = []
        if self.__i != id:
            return result
        while self.__i < len(self.__values) and self.__values[self.__i]:
            result.append(self.__values[self.__i])
            self.__i += 1
        return result

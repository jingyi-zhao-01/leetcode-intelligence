# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: design-file-system
# source_path: LeetCode-Solutions-master/Python/design-file-system.py
# solution_class: Solution
# submission_id: 477188118780811862de5444dfd9aed783bb52cc
# seed: 3474065672

# Time:  create: O(n)
#        get:    O(n)
# Space: O(n)

class FileSystem(object):

    def __init__(self):
        self.__lookup = {"": -1}

    def create(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        if path[:path.rfind('/')] not in self.__lookup:
            return False
        self.__lookup[path] = value
        return True
        
    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        if path not in self.__lookup:
            return -1
        return self.__lookup[path]

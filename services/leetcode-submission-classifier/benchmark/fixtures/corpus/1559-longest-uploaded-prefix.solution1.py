# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-uploaded-prefix
# source_path: LeetCode-Solutions-master/Python/longest-uploaded-prefix.py
# solution_class: Solution
# submission_id: 67068af7171c4475783f9debed3df57fe934fbb6
# seed: 3803646824

# Time:  ctor:    O(1)
#        upload:  O(1), amortized
#        longest: O(1)
# Space: O(n)

# hash table
class LUPrefix(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.__lookup = set()
        self.__curr = 0

    def upload(self, video):
        """
        :type video: int
        :rtype: None
        """
        self.__lookup.add(video-1)
        while self.__curr in self.__lookup:
            self.__lookup.remove(self.__curr)
            self.__curr += 1

    def longest(self):
        """
        :rtype: int
        """
        return self.__curr

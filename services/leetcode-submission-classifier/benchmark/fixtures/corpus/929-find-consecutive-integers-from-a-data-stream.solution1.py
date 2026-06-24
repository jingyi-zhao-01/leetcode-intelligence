# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-consecutive-integers-from-a-data-stream
# source_path: LeetCode-Solutions-master/Python/find-consecutive-integers-from-a-data-stream.py
# solution_class: Solution
# submission_id: 7b0664f34c92af10c8bf7a8c6aa389174be4c54d
# seed: 152291675

# Time:  O(1)
# Space: O(1)

# array
class DataStream(object):

    def __init__(self, value, k):
        """
        :type value: int
        :type k: int
        """
        self.__value = value
        self.__k = k
        self.__cnt = 0

    def consec(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == self.__value:
            self.__cnt += 1
        else:
            self.__cnt = 0
        return self.__cnt >= self.__k

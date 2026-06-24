# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rle-iterator
# source_path: LeetCode-Solutions-master/Python/rle-iterator.py
# solution_class: Solution
# submission_id: f6ff6fe54522c899f2b5e82713e2ec0d8d4ecf23
# seed: 3118569840

# Time:  O(n)
# Space: O(1)

class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.__A = A
        self.__i = 0
        self.__cnt = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.__i < len(self.__A):
            if  n > self.__A[self.__i] - self.__cnt:
                n -= self.__A[self.__i] - self.__cnt
                self.__cnt = 0
                self.__i += 2
            else:
                self.__cnt += n
                return self.__A[self.__i+1]
        return -1




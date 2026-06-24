# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: building-h2o
# source_path: LeetCode-Solutions-master/Python/building-h2o.py
# solution_class: Solution
# submission_id: 8c01d8a97c56356579e500e8bcd4175dd138ce17
# seed: 2607416870

# Time:  O(n)
# Space: O(1)

import threading


class H2O(object):
    def __init__(self):
        self.__l = threading.Lock()
        self.__nH = 0
        self.__nO = 0
        self.__releaseHydrogen = None
        self.__releaseOxygen = None

    def hydrogen(self, releaseHydrogen):
        with self.__l:
            self.__releaseHydrogen = releaseHydrogen
            self.__nH += 1
            self.__output()

    def oxygen(self, releaseOxygen):
        with self.__l:
            self.__releaseOxygen = releaseOxygen
            self.__nO += 1
            self.__output()

    def __output(self):
        while self.__nH >= 2 and \
              self.__nO >= 1:
            self.__nH -= 2
            self.__nO -= 1
            self.__releaseHydrogen()
            self.__releaseHydrogen()
            self.__releaseOxygen()


# Time:  O(n)
# Space: O(1)
# TLE
class H2O2(object):
    def __init__(self):
        self.__nH = 0
        self.__nO = 0
        self.__cv = threading.Condition()

    def hydrogen(self, releaseHydrogen):
        """
        :type releaseHydrogen: method
        :rtype: void
        """
        with self.__cv:
            while (self.__nH+1) - 2*self.__nO > 2:
                self.__cv.wait()
            self.__nH += 1
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()
            self.__cv.notifyAll()

    def oxygen(self, releaseOxygen):
        """
        :type releaseOxygen: method
        :rtype: void
        """
        with self.__cv:
            while 2*(self.__nO+1) - self.__nH > 2:
                self.__cv.wait()
            self.__nO += 1
            # releaseOxygen() outputs "O". Do not change or remove this line.
            releaseOxygen()
            self.__cv.notifyAll()

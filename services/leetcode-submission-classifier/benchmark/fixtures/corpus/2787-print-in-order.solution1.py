# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: print-in-order
# source_path: LeetCode-Solutions-master/Python/print-in-order.py
# solution_class: Solution
# submission_id: 655aa65fb22f0d27aaa5b660b74d84943d1aba60
# seed: 1995255628

# Time:  O(n)
# Space: O(1)

import threading


class Foo(object):
    def __init__(self):
        self.__cv = threading.Condition()
        self.__has_first = False
        self.__has_second = False

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        with self.__cv:
            # printFirst() outputs "first". Do not change or remove this line.
            printFirst()            
            self.__has_first = True
            self.__cv.notifyAll()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        with self.__cv:
            while not self.__has_first:
                self.__cv.wait()
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.__has_second = True
            self.__cv.notifyAll()
              
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        with self.__cv:
            while not self.__has_second:
                self.__cv.wait()
            # printThird() outputs "third". Do not change or remove this line.
            printThird()
            self.__cv.notifyAll()
        

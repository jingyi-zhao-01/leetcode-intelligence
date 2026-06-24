# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: design-phone-directory
# source_path: LeetCode-Solutions-master/Python/design-phone-directory.py
# solution_class: Solution
# submission_id: b8e608388b307c710a150edf088c9cd1c3f70b8e
# seed: 781410326

# init:     Time: O(n), Space: O(n)
# get:      Time: O(1), Space: O(1)
# check:    Time: O(1), Space: O(1)
# release:  Time: O(1), Space: O(1)

class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.__curr = 0
        self.__numbers = range(maxNumbers)
        self.__used = [False] * maxNumbers


    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if self.__curr == len(self.__numbers):
            return -1
        number = self.__numbers[self.__curr]
        self.__curr += 1
        self.__used[number] = True
        return number


    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return 0 <= number < len(self.__numbers) and \
               not self.__used[number]


    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if not 0 <= number < len(self.__numbers) or \
           not self.__used[number]:
            return
        self.__used[number] = False
        self.__curr -= 1
        self.__numbers[self.__curr] = number




# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: happy-number
# source_path: LeetCode-Solutions-master/Python/happy-number.py
# solution_class: Solution
# submission_id: 87eb6340221d683e673260c05b4807fe4dcb82ee
# seed: 464238984

# Time:  O(k), where k is the steps to be happy number
# Space: O(k)

class Solution(object):
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        lookup = {}
        while n != 1 and n not in lookup:
            lookup[n] = True
            n = self.nextNumber(n)
        return n == 1

    def nextNumber(self, n):
        new = 0
        for char in str(n):
            new += int(char)**2
        return new
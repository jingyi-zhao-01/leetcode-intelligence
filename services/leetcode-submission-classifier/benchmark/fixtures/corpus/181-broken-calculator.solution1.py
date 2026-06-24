# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: broken-calculator
# source_path: LeetCode-Solutions-master/Python/broken-calculator.py
# solution_class: Solution
# submission_id: f2d6944370fbcb746bef392095ce7bac91da0c17
# seed: 1130399515

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        result = 0
        while X < Y:
            if Y%2:
                Y += 1
            else:
                Y /= 2
            result += 1
        return result + X-Y
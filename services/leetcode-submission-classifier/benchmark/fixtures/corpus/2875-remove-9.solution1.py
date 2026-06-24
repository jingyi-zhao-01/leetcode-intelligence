# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-9
# source_path: LeetCode-Solutions-master/Python/remove-9.py
# solution_class: Solution
# submission_id: d648ef2a84a72034b1b71285d629d52f5701173a
# seed: 1655940046

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        result, base = 0, 1
        while n > 0:
            result += (n%9) * base
            n /= 9
            base *= 10
        return result
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-key-of-the-numbers
# source_path: LeetCode-Solutions-master/Python/find-the-key-of-the-numbers.py
# solution_class: Solution
# submission_id: 97c2ff0bb2d06c79baa0ee4cfe6f9aa42ae9b9ea
# seed: 379234058

# Time:  O(d), d = 4
# Space: O(1)

# math

class Solution(object):
    def generateKey(self, num1, num2, num3):
        """
        :type num1: int
        :type num2: int
        :type num3: int
        :rtype: int
        """
        L = 4
        result = 0
        base = pow(10, L-1)
        for _ in xrange(L):
            result = result*10+min(num1//base%10, num2//base%10, num3//base%10)
            base //= 10
        return result
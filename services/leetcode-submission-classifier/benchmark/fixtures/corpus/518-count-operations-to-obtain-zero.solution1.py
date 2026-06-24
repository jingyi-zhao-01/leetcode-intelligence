# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-operations-to-obtain-zero
# source_path: LeetCode-Solutions-master/Python/count-operations-to-obtain-zero.py
# solution_class: Solution
# submission_id: 133afb5d148907108ec4e75ee5e24d400d125946
# seed: 4095217364

# Time:  O(log(min(m, n)))
# Space: O(1)

# gcd-like solution

class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        result = 0
        while num2:
            result += num1//num2
            num1, num2 = num2, num1%num2
        return result
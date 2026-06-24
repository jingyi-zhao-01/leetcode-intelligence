# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-digit-number
# source_path: LeetCode-Solutions-master/Python/valid-digit-number.py
# solution_class: Solution
# submission_id: f1fd2a55890abe35cd04beed184b85d4155d098a
# seed: 1519528709

# Time:  O(logn)
# Space: O(1)

# math

class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        result = False
        while n:
            n, r = divmod(n, 10)
            if r != x:
                continue
            if not n:
                return False
            result = True
        return result
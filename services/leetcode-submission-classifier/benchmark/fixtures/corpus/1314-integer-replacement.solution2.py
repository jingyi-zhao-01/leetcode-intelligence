# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: integer-replacement
# source_path: LeetCode-Solutions-master/Python/integer-replacement.py
# solution_class: Solution2
# submission_id: 694216546eae6fff48b0c08a738531976c8d72cc
# seed: 446286048

# Time:  O(logn)
# Space: O(1)

class Solution2(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return [0, 0, 1, 2][n]
        if n % 4 in (0, 2):
            return self.integerReplacement(n / 2) + 1
        elif n % 4 == 1:
            return self.integerReplacement((n - 1) / 4) + 3
        else:
            return self.integerReplacement((n + 1) / 4) + 3
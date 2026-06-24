# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rotate-string
# source_path: LeetCode-Solutions-master/Python/rotate-string.py
# solution_class: Solution3
# submission_id: fae23eef50be44d1aacaeb8c1366308e81bcdf0a
# seed: 941320201

# Time:  O(n)
# Space: O(1)

class Solution3(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return len(A) == len(B) and B in A*2
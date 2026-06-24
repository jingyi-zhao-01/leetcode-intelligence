# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: separate-black-and-white-balls
# source_path: LeetCode-Solutions-master/Python/separate-black-and-white-balls.py
# solution_class: Solution
# submission_id: 7c72e436fdf7830db75438c967c2517f5348ee91
# seed: 3751925960

# Time:  O(n)
# Space: O(1)

# two pointers

class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = left = 0
        for right in xrange(len(s)):
            if s[right] != '0':
                continue
            result += right-left
            left += 1
        return result
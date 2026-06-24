# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-degree-of-a-string
# source_path: LeetCode-Solutions-master/Python/reverse-degree-of-a-string.py
# solution_class: Solution
# submission_id: d8540beaa2a8afc48a39f8c41f69e31125075fb3
# seed: 2280247623

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(i*(26-(ord(x)-ord('a'))) for i, x in enumerate(s, 1))
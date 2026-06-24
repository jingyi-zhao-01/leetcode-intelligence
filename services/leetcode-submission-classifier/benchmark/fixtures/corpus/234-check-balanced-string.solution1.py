# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-balanced-string
# source_path: LeetCode-Solutions-master/Python/check-balanced-string.py
# solution_class: Solution
# submission_id: a7311ee3e709fee4b3cb382b3d036c7356cb21b8
# seed: 1293806267

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        return sum(ord(num[i])-ord('0') for i in xrange(0, len(num), 2)) == sum(ord(num[i])-ord('0') for i in xrange(1, len(num), 2))
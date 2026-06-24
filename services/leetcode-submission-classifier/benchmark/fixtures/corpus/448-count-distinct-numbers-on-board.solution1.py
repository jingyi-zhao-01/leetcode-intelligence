# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-distinct-numbers-on-board
# source_path: LeetCode-Solutions-master/Python/count-distinct-numbers-on-board.py
# solution_class: Solution
# submission_id: 624b798677abf762d7f0ccb60c7fc5da64978cf5
# seed: 1951840871

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def distinctIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n-1 if n >= 2 else 1
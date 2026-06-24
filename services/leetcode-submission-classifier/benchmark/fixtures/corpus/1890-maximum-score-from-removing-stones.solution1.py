# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-score-from-removing-stones
# source_path: LeetCode-Solutions-master/Python/maximum-score-from-removing-stones.py
# solution_class: Solution
# submission_id: eb6b2c9cd3454b2967d45fa4a3349879ea914cc0
# seed: 3721655858

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        # assumed c is the max size
        # case1: a+b > c
        # => (a+b-c)//2 + c = (a+b+c)//2 < a+b
        # case2: a+b <= c
        # => a+b <= (a+b+c)//2
        return min((a+b+c)//2, a+b+c - max(a, b, c))
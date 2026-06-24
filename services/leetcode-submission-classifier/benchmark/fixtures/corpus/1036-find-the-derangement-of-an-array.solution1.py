# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-derangement-of-an-array
# source_path: LeetCode-Solutions-master/Python/find-the-derangement-of-an-array.py
# solution_class: Solution
# submission_id: f66179b6054476f13df1b23ae3710f7f5c784530
# seed: 1502465227

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        M = 1000000007
        mul, total = 1, 0
        for i in reversed(xrange(n+1)):
            total = (total + M + (1 if i % 2 == 0 else -1) * mul) % M
            mul = (mul * i) % M
        return total
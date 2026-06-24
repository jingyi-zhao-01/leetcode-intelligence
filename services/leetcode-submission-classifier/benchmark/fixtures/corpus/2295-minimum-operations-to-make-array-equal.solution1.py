# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-make-array-equal
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-make-array-equal.py
# solution_class: Solution
# submission_id: c8e2ce7d0dc6ab4191a81943ed7d31c1df9f191a
# seed: 2834361384

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        # total = sum(2i+1 for i in xrange(n)) = n^2
        # left_half_total = sum(2i+1 for i in xrange(n//2)) = (n//2)^2
        # result = (n//2) * (total//n) - left_half_total = (n//2)*(n-n//2) = (n//2)*((n+1)//2)
        return (n//2)*((n+1)//2)
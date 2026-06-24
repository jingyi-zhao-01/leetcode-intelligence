# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: perfect-squares
# source_path: LeetCode-Solutions-master/Python/perfect-squares.py
# solution_class: Solution
# submission_id: 21885e865d435f6c422d35443a444c5cc8dc4b87
# seed: 1406658242

# Time:  O(n * sqrt(n))
# Space: O(n)

class Solution(object):
    _num = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = self._num
        while len(num) <= n:
            num += min(num[-i*i] for i in xrange(1, int(len(num)**0.5+1))) + 1,
        return num[n]
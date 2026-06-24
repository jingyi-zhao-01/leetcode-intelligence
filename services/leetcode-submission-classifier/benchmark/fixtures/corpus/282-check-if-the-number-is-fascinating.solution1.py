# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-the-number-is-fascinating
# source_path: LeetCode-Solutions-master/Python/check-if-the-number-is-fascinating.py
# solution_class: Solution
# submission_id: af269364f66d76347d302c99d3fd2d31f056adea
# seed: 385032655

# Time:  O(logn)
# Space: O(1)

# string, bitmasks

class Solution(object):
    def isFascinating(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lookup = [0]
        def check(x):
            while x:
                x, d = divmod(x, 10)
                if d == 0 or lookup[0]&(1<<d):
                    return False
                lookup[0] |= (1<<d)
            return True
    
        return check(n) and check(2*n) and check(3*n)
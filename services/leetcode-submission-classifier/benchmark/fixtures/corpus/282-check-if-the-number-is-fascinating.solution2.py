# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-the-number-is-fascinating
# source_path: LeetCode-Solutions-master/Python/check-if-the-number-is-fascinating.py
# solution_class: Solution2
# submission_id: 140798bed26ac14f82ce3d0319fc2fbc758d88f2
# seed: 914593240

# Time:  O(logn)
# Space: O(1)

# string, bitmasks

class Solution2(object):
    def isFascinating(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = str(n)+str(2*n)+str(3*n)
        return '0' not in s and len(s) == 9 and len(set(s)) == 9
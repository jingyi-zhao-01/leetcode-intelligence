# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-time-for-given-digits
# source_path: LeetCode-Solutions-master/Python/largest-time-for-given-digits.py
# solution_class: Solution
# submission_id: f1ccc82b35172c9dd906b91a84402322c05d75f2
# seed: 2839421047

# Time:  O(1)
# Space: O(1)

import itertools

class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        result = ""
        for i in xrange(len(A)):
            A[i] *= -1
        A.sort()
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours = -(10*h1 + h2)
            mins = -(10*m1 + m2)
            if 0 <= hours < 24 and 0 <= mins < 60:
                result = "{:02}:{:02}".format(hours, mins)
                break
        return result
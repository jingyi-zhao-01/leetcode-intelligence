# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-closest-person
# source_path: LeetCode-Solutions-master/Python/find-closest-person.py
# solution_class: Solution
# submission_id: 19c7d5ce11f922f2520337ee6910e181f9365c18
# seed: 2138053053

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        return range(3)[cmp(abs(y-z), abs(x-z))]
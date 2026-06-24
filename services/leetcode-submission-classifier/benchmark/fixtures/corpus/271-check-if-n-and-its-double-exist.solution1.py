# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-n-and-its-double-exist
# source_path: LeetCode-Solutions-master/Python/check-if-n-and-its-double-exist.py
# solution_class: Solution
# submission_id: 4cef60f67f1b9c5387fbebfc40d3c2c57894d6f8
# seed: 36998146

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        lookup = set()
        for x in arr:
            if 2*x in lookup or \
               (x%2 == 0 and x//2 in lookup):
                return True
            lookup.add(x)
        return False
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: destination-city
# source_path: LeetCode-Solutions-master/Python/destination-city.py
# solution_class: Solution
# submission_id: e5c46079b48e4efdb9dee4f48d6f86a608fdbe4c
# seed: 2583766223

# Time:  O(n)
# Space: O(n)

import itertools

class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        A, B = map(set, itertools.izip(*paths))
        return (B-A).pop()
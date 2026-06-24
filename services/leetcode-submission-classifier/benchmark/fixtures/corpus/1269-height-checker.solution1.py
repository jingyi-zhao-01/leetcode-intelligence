# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: height-checker
# source_path: LeetCode-Solutions-master/Python/height-checker.py
# solution_class: Solution
# submission_id: 0ee1c6598ce1ccb2752ca5e565f8061c67e16cc8
# seed: 1890773832

# Time:  O(nlogn)
# Space: O(n)

import itertools

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        return sum(i != j for i, j in itertools.izip(heights, sorted(heights)))
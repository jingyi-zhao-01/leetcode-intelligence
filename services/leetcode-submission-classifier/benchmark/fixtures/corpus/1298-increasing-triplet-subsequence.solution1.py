# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: increasing-triplet-subsequence
# source_path: LeetCode-Solutions-master/Python/increasing-triplet-subsequence.py
# solution_class: Solution
# submission_id: 801ecfd3390a28fa4e092e6530546cbf55aa479b
# seed: 1906670075

# Time:  O(n)
# Space: O(1)

import bisect

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min_num, a, b = float("inf"), float("inf"), float("inf")
        for c in nums:
            if min_num >= c:
                min_num = c
            elif b >= c:
                a, b = min_num, c
            else:  # a < b < c
                return True
        return False
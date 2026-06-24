# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-unique-number
# source_path: LeetCode-Solutions-master/Python/largest-unique-number.py
# solution_class: Solution
# submission_id: 069b79f3d65a986938558f438c970a5405f15461
# seed: 1412789058

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def largestUniqueNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.append(-1)
        return max(k for k,v in collections.Counter(A).items() if v == 1)
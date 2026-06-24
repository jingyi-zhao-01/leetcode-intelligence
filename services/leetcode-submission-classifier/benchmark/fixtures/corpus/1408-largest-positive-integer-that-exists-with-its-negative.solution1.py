# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-positive-integer-that-exists-with-its-negative
# source_path: LeetCode-Solutions-master/Python/largest-positive-integer-that-exists-with-its-negative.py
# solution_class: Solution
# submission_id: f9f53a4b13f66ab3eb2d4da2366e07330a711a8b
# seed: 3005097688

# Time:  O(n)
# Space: O(n)

# hash table

class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = set(nums)
        return max([x for x in lookup if x > 0 and -x in lookup] or [-1])
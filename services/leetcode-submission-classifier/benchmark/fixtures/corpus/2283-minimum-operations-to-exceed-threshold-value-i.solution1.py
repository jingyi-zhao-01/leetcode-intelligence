# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-exceed-threshold-value-i
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-exceed-threshold-value-i.py
# solution_class: Solution
# submission_id: ff78a0d2498528afdcbe5cfc063ac4fd1fe1de59
# seed: 564293955

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sum(x < k for x in nums)
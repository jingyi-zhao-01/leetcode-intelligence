# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-minimum-operations-to-make-all-elements-divisible-by-three
# source_path: LeetCode-Solutions-master/Python/find-minimum-operations-to-make-all-elements-divisible-by-three.py
# solution_class: Solution
# submission_id: 7bcc43e4fec3bad734fa99d3dad40ccd56000dba
# seed: 2725289473

# Time:  O(n)
# Space: O(1)

# math

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(x%3 != 0 for x in nums)
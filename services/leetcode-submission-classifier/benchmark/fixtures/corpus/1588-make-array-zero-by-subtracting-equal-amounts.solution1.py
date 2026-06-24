# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-array-zero-by-subtracting-equal-amounts
# source_path: LeetCode-Solutions-master/Python/make-array-zero-by-subtracting-equal-amounts.py
# solution_class: Solution
# submission_id: 96072cfc0c50d1015520c933f117267d26ce8a86
# seed: 155107292

# Time:  O(n)
# Space: O(n)

# hash table

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len({x for x in nums if x})
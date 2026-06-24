# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: keep-multiplying-found-values-by-two
# source_path: LeetCode-Solutions-master/Python/keep-multiplying-found-values-by-two.py
# solution_class: Solution
# submission_id: 24b685e87d2ac2186079a35fe44736568e0eb75c
# seed: 3502066258

# Time:  O(n)
# Space: O(n)

# hash table

class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        lookup = set(nums)
        while original in lookup:
            original *= 2
        return original
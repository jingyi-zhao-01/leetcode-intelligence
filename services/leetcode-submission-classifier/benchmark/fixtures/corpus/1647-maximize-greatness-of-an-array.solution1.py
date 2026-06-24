# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-greatness-of-an-array
# source_path: LeetCode-Solutions-master/Python/maximize-greatness-of-an-array.py
# solution_class: Solution
# submission_id: 5539cfee70ad50f1f29b4c07fede5544e44d7808
# seed: 1274408094

# Time:  O(n)
# Space: O(n)

# freq table, contructive algorithms

class Solution(object):
    def maximizeGreatness(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(nums)-max(collections.Counter(nums).itervalues())
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: concatenation-of-array
# source_path: LeetCode-Solutions-master/Python/concatenation-of-array.py
# solution_class: Solution
# submission_id: f4f7a3b5b30661a8b5c00e1fc09fd9efafdadf89
# seed: 1809197122

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.extend(nums)
        return nums
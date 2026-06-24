# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-array-by-absolute-value
# source_path: LeetCode-Solutions-master/Python/sort-array-by-absolute-value.py
# solution_class: Solution2
# submission_id: 3e41eebe189a3ef42627cf9c5a30661bc18486ca
# seed: 1898802210

# Time:  O(n + r)
# Space: O(n + r)

# sort

class Solution2(object):
    def sortByAbsoluteValue(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort(key=lambda x: abs(x))
        return nums
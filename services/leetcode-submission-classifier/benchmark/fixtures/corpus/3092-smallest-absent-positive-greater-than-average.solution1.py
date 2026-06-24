# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-absent-positive-greater-than-average
# source_path: LeetCode-Solutions-master/Python/smallest-absent-positive-greater-than-average.py
# solution_class: Solution
# submission_id: 30eba1cf29f740158e8c03720e323529eb98d7f5
# seed: 357020302

# Time:  O(n)
# Space: O(n)

# hash table

class Solution(object):
    def smallestAbsent(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        lookup = set(nums)
        return next(x for x in xrange(max(total//len(nums)+1, 1), max(max(nums)+1, 1)+1) if x not in lookup and x*len(nums) > total)
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-distinct-difference-array
# source_path: LeetCode-Solutions-master/Python/find-the-distinct-difference-array.py
# solution_class: Solution
# submission_id: 92d4e1d01ac959c0d496f155353ef4461e1961d2
# seed: 1146851655

# Time:  O(n)
# Space: O(n)

# hash table, prefix sum

class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0]*len(nums)
        lookup = set()
        for i in xrange(len(nums)):
            lookup.add(nums[i])
            result[i] = len(lookup)
        lookup.clear()
        for i in reversed(xrange(len(nums))):
            result[i] -= len(lookup)
            lookup.add(nums[i])
        return result
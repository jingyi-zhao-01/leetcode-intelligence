# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: replace-elements-in-an-array
# source_path: LeetCode-Solutions-master/Python/replace-elements-in-an-array.py
# solution_class: Solution
# submission_id: 11248233c016b560818e86901290f064d81f01d3
# seed: 1781349028

# Time:  O(n + m)
# Space: O(n)

# hash table, optimized from solution2

class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        lookup = {x:i for i, x in enumerate(nums)}
        for x, y in operations:
            lookup[y] = lookup.pop(x)
        for x, i in lookup.iteritems():
            nums[i] = x
        return nums
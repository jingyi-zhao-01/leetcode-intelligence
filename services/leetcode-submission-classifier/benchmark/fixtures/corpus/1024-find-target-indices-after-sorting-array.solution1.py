# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-target-indices-after-sorting-array
# source_path: LeetCode-Solutions-master/Python/find-target-indices-after-sorting-array.py
# solution_class: Solution
# submission_id: 420ecd7cfe231f41d0a89ab73612e99f4a51ce66
# seed: 1382534044

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        less = sum(x < target for x in nums)
        return range(less, less+sum(x == target for x in nums))
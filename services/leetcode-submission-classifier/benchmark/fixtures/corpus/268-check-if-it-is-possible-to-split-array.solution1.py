# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-it-is-possible-to-split-array
# source_path: LeetCode-Solutions-master/Python/check-if-it-is-possible-to-split-array.py
# solution_class: Solution
# submission_id: 36f67989113f76c87520f9d262fbae107f0a6295
# seed: 512781790

# Time:  O(n)
# Space: O(1)

# constructive algorithms

class Solution(object):
    def canSplitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: bool
        """
        return len(nums) <= 2 or any(nums[i]+nums[i+1] >= m for i in xrange(len(nums)-1))
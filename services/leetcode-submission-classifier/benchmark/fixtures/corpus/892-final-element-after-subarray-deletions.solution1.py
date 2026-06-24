# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: final-element-after-subarray-deletions
# source_path: LeetCode-Solutions-master/Python/final-element-after-subarray-deletions.py
# solution_class: Solution
# submission_id: cf8c3d99559657dd87993341312349d9b240882f
# seed: 2991832953

# Time:  O(1)
# Space: O(1)

# greedy, game theory

class Solution(object):
    def finalElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(nums[0], nums[-1])
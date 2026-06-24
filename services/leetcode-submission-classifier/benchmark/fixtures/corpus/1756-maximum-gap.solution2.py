# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-gap
# source_path: LeetCode-Solutions-master/Python/maximum-gap.py
# solution_class: Solution2
# submission_id: 873568c40a03b79b06e1f30a091cb0f9545446e4
# seed: 2981257760

# Time:  O(n)
# Space: O(n)

class Solution2(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 2:
            return 0

        nums.sort()
        pre = nums[0]
        max_gap = float("-inf")

        for i in nums:
            max_gap = max(max_gap, i - pre)
            pre = i
        return max_gap
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divide-array-into-increasing-sequences
# source_path: LeetCode-Solutions-master/Python/divide-array-into-increasing-sequences.py
# solution_class: Solution
# submission_id: df172937c8af3348a80a42f98fc83dda7dc25089
# seed: 1490698532

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def canDivideIntoSubsequences(self, nums, K):
        """
        :type nums: List[int]
        :type K: int
        :rtype: bool
        """
        curr, max_count = 1, 1
        for i in xrange(1, len(nums)):
            curr = 1 if nums[i-1] < nums[i] else curr+1
            max_count = max(max_count, curr)
        return K*max_count <= len(nums)
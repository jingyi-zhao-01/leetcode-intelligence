# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-unique-subarray-sum-after-deletion
# source_path: LeetCode-Solutions-master/Python/maximum-unique-subarray-sum-after-deletion.py
# solution_class: Solution
# submission_id: 2cf27531185109fa602dd4fbbd44226a2aa0e7e3
# seed: 3561624729

# Time:  O(n)
# Space: O(n)

# hash table

class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = max(nums)
        return mx if mx < 0 else sum(x for x in set(nums) if x >= 0)
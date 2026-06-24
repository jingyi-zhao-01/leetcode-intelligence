# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-maximum-pair-sum-in-array
# source_path: LeetCode-Solutions-master/Python/minimize-maximum-pair-sum-in-array.py
# solution_class: Solution
# submission_id: 221051592706f42a0cdf639f7f69e0b72b63c692
# seed: 3909815258

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[i]+nums[-1-i] for i in xrange(len(nums)//2))
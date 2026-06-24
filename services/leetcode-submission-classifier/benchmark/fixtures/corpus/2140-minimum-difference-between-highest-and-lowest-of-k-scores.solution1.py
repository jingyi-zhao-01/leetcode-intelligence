# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-difference-between-highest-and-lowest-of-k-scores
# source_path: LeetCode-Solutions-master/Python/minimum-difference-between-highest-and-lowest-of-k-scores.py
# solution_class: Solution
# submission_id: 9b20086ba0422823c308948d8eff5cd477261f16
# seed: 576758143

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return min(nums[i]-nums[i-k+1] for i in xrange(k-1, len(nums)))
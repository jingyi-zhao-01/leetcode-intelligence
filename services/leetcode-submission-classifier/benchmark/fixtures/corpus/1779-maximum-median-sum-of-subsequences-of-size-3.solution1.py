# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-median-sum-of-subsequences-of-size-3
# source_path: LeetCode-Solutions-master/Python/maximum-median-sum-of-subsequences-of-size-3.py
# solution_class: Solution
# submission_id: a3886188486cb7d7c2a28190a10646df2201311e
# seed: 1212992473

# Time:  O(nlogn)
# Space: O(1)

# sort, greedy

class Solution(object):
    def maximumMedianSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[i] for i in xrange(len(nums)//3, len(nums), 2))
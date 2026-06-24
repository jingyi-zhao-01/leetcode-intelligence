# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-make-array-non-decreasing
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-make-array-non-decreasing.py
# solution_class: Solution
# submission_id: 1cbfcbbcb046e80ecf41f43d27251ce3f97169c3
# seed: 2195613392

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(max(nums[i]-nums[i+1], 0) for i in xrange(len(nums)-1))
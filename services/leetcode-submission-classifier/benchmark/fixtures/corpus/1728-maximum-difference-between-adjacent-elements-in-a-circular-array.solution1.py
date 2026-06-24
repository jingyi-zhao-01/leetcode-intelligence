# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-difference-between-adjacent-elements-in-a-circular-array
# source_path: LeetCode-Solutions-master/Python/maximum-difference-between-adjacent-elements-in-a-circular-array.py
# solution_class: Solution
# submission_id: b3e1308b8c8c900e9f207088e1c305f1fec5a61d
# seed: 1536264721

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(abs(nums[i]-nums[i-1]) for i in xrange(len(nums)))
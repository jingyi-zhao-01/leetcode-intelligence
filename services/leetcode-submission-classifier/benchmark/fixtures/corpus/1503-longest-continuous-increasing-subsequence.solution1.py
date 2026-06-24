# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-continuous-increasing-subsequence
# source_path: LeetCode-Solutions-master/Python/longest-continuous-increasing-subsequence.py
# solution_class: Solution
# submission_id: f97f4fbbec84778c7dc9b495b2aed49ecf4db502
# seed: 3132429031

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, count = 0, 0
        for i in xrange(len(nums)):
            if i == 0 or nums[i-1] < nums[i]:
                count += 1
                result = max(result, count)
            else:
                count = 1
        return result
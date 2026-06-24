# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reach-end-of-array-with-max-score
# source_path: LeetCode-Solutions-master/Python/reach-end-of-array-with-max-score.py
# solution_class: Solution
# submission_id: 19378b24877c01edcce8aa2d7708145b89f68472
# seed: 3543004696

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def findMaximumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = mx = 0
        for x in nums:
            result += mx
            mx = max(mx, x)
        return result
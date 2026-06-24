# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-game
# source_path: LeetCode-Solutions-master/Python/minimum-number-game.py
# solution_class: Solution
# submission_id: d9a0bcd763ade94246afab1051aa911523a711f3
# seed: 906387641

# Time:  O(nlogn)
# Space: O(1)

# sort

class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        for i in xrange(0, len(nums), 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums
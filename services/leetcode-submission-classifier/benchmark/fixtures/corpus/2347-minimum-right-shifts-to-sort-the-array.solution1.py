# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-right-shifts-to-sort-the-array
# source_path: LeetCode-Solutions-master/Python/minimum-right-shifts-to-sort-the-array.py
# solution_class: Solution
# submission_id: ed67be22dae3f6a55fa3a4220218303300e39eb3
# seed: 4078473495

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def minimumRightShifts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = next((i for i in xrange(len(nums)) if not nums[i] < nums[(i+1)%len(nums)]), len(nums))
        j = next((j for j in xrange(i+1, len(nums)) if not nums[j%len(nums)] < nums[(j+1)%len(nums)]), len(nums))
        return len(nums)-(i+1) if j == len(nums) else -1
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: movement-of-robots
# source_path: LeetCode-Solutions-master/Python/movement-of-robots.py
# solution_class: Solution
# submission_id: 3a3be3e90276b0b1eba828737e061d9d39998a4c
# seed: 2966719700

# Time:  O(nlogn)
# Space: O(1)

# sort, math

class Solution(object):
    def sumDistance(self, nums, s, d):
        """
        :type nums: List[int]
        :type s: str
        :type d: int
        :rtype: int
        """
        MOD = 10**9+7
        for i in xrange(len(nums)):
            nums[i] += d if s[i] == 'R' else -d
        nums.sort()
        return reduce(lambda x, y: (x+y)%MOD, ((i-(len(nums)-(i+1)))*x for i, x in enumerate(nums)))
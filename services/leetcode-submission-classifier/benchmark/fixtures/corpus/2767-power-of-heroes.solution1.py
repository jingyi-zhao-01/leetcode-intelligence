# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: power-of-heroes
# source_path: LeetCode-Solutions-master/Python/power-of-heroes.py
# solution_class: Solution
# submission_id: 26348d9fde84ca7394144caf4a753046bccc3e85
# seed: 293967894

# Time:  O(nlogn)
# Space: O(1)

# sort, combinatorics, dp

class Solution(object):
    def sumOfPower(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        nums.sort()
        result = dp = 0
        for x in nums:
            result = (result+(x**2)*(dp+x))%MOD
            dp = (dp+(dp+x))%MOD
        return result
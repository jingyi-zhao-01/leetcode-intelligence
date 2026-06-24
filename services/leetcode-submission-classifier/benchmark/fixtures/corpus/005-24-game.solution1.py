# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: 24-game
# source_path: LeetCode-Solutions-master/Python/24-game.py
# solution_class: Solution
# submission_id: 3cfd1bae7640b60cacce52d6a54c818819873810
# seed: 3517224347

# Time:  O(n^3 * 4^n) = O(1), n = 4
# Space: O(n^2) = O(1)

from operator import add, sub, mul, truediv
from fractions import Fraction

class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return abs(nums[0]-24) < 1e-6
        ops = [add, sub, mul, truediv]
        for i in xrange(len(nums)):
            for j in xrange(len(nums)):
                if i == j:
                    continue
                next_nums = [nums[k] for k in xrange(len(nums)) if i != k != j]
                for op in ops:
                    if ((op is add or op is mul) and j > i) or \
                       (op == truediv and nums[j] == 0):
                        continue
                    next_nums.append(op(nums[i], nums[j]))
                    if self.judgePoint24(next_nums):
                        return True
                    next_nums.pop()
        return False
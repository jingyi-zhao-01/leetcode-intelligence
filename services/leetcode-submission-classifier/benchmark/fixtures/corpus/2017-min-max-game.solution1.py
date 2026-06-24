# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: min-max-game
# source_path: LeetCode-Solutions-master/Python/min-max-game.py
# solution_class: Solution
# submission_id: 7b1fa32958de1bd8bd4602be0b76af7e6c761ff4
# seed: 3973499774

# Time:  O(n)
# Space: O(1)

# simulation, optimized from solution2

class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        while n != 1:
            new_q = []
            for i in xrange(n//2):
                nums[i] = min(nums[2*i], nums[2*i+1]) if i%2 == 0 else max(nums[2*i], nums[2*i+1])
            n //= 2
        return nums[0]
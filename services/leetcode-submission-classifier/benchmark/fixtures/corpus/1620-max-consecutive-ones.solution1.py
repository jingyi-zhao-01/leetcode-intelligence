# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: max-consecutive-ones
# source_path: LeetCode-Solutions-master/Python/max-consecutive-ones.py
# solution_class: Solution
# submission_id: 68658d63d2564231211901d2bb62fcec7939612e
# seed: 2124713679

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, local_max = 0, 0
        for n in nums:
            local_max = (local_max + 1 if n else 0)
            result = max(result, local_max)
        return result
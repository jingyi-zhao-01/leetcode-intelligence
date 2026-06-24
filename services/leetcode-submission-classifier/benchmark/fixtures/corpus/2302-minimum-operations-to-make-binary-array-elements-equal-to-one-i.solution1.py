# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-make-binary-array-elements-equal-to-one-i
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-make-binary-array-elements-equal-to-one-i.py
# solution_class: Solution
# submission_id: 2b8b7b673dbe4721524cc1463916800125896de9
# seed: 233338509

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in xrange(len(nums)-2):
            if nums[i]:
                continue
            nums[i+1] ^= 1
            nums[i+2] ^= 1
            result += 1
        return result if nums[-2] == nums[-1] == 1 else -1
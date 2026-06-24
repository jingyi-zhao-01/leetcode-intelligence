# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-zero-filled-subarrays
# source_path: LeetCode-Solutions-master/Python/number-of-zero-filled-subarrays.py
# solution_class: Solution
# submission_id: 027ae35ba7d98ccecdbb66e0bdcc8e7785d8997e
# seed: 960731308

# Time:  O(n)
# Space: O(1)

# two pointers, combinatorics

class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        prev = -1
        for i in xrange(len(nums)):
            if nums[i]:
                prev = i
                continue
            result += i-prev
        return result
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-non-overlapping-subarrays-with-sum-equals-target
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target.py
# solution_class: Solution
# submission_id: 93f8bce34921dac20fb3330183f05365df8fdf1a
# seed: 392201471

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lookup = {0:-1}
        result, accu, right = 0, 0, -1
        for i, num in enumerate(nums):
            accu += num
            if accu-target in lookup and lookup[accu-target] >= right:
                right = i
                result += 1  # greedy
            lookup[accu] = i
        return result
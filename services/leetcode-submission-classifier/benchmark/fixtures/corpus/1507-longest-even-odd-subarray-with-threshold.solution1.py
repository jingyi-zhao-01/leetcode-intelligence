# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-even-odd-subarray-with-threshold
# source_path: LeetCode-Solutions-master/Python/longest-even-odd-subarray-with-threshold.py
# solution_class: Solution
# submission_id: 14d6e5ac3a3958f46358b2298722efbec84abaa3
# seed: 2334256041

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        result = l = 0
        for x in nums:
            if x > threshold:
                l = 0
                continue
            if l%2 == x%2:
                l += 1
            else:
                l = int(x%2 == 0)
            result = max(result, l)
        return result
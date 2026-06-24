# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-nice-subarray
# source_path: LeetCode-Solutions-master/Python/longest-nice-subarray.py
# solution_class: Solution
# submission_id: 4bd80960daba8a70a87476db3883131cf901d739
# seed: 1939718315

# Time:  O(n)
# Space: O(1)

# sliding window, two pointers

class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = left = curr = 0
        for right in xrange(len(nums)):
            while curr&nums[right]:
                curr ^= nums[left]
                left += 1
            curr |= nums[right]
            result = max(result, right-left+1)
        return result
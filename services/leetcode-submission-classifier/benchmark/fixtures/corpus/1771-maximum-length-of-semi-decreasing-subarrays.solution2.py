# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-length-of-semi-decreasing-subarrays
# source_path: LeetCode-Solutions-master/Python/maximum-length-of-semi-decreasing-subarrays.py
# solution_class: Solution2
# submission_id: bbcc262e2bc004a260729d427a213800e401b5b9
# seed: 2389546622

# Time:  O(n)
# Space: O(n)

# mono stack

class Solution2(object):
    def maxSubarrayLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idxs = range(len(nums))
        idxs.sort(key=lambda x: nums[x], reverse=True)
        result = 0
        for left in xrange(len(nums)):
            while idxs and nums[idxs[-1]] < nums[left]:
                result = max(result, idxs.pop()-left+1)
        return result
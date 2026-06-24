# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-alternating-subarray
# source_path: LeetCode-Solutions-master/Python/longest-alternating-subarray.py
# solution_class: Solution
# submission_id: e7f3a743534f5e8f3884e4ac02757a661130ffe9
# seed: 1200135475

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def alternatingSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = l = -1
        for i in xrange(len(nums)-1):
            if l != -1 and nums[i-1] == nums[i+1]:
                l += 1
            else:
                l = 2 if nums[i+1]-nums[i] == 1 else -1
            result = max(result, l)
        return result
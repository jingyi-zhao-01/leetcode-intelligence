# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-fibonacci-subarray
# source_path: LeetCode-Solutions-master/Python/longest-fibonacci-subarray.py
# solution_class: Solution
# submission_id: e2e532a911658d9037d12b5d898747f527722411
# seed: 1769751813

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = cnt = 2
        for i in xrange(2, len(nums)):
            if nums[i] != nums[i-1]+nums[i-2]:
                cnt = 2
                continue
            cnt += 1
            result = max(result, cnt)
        return result
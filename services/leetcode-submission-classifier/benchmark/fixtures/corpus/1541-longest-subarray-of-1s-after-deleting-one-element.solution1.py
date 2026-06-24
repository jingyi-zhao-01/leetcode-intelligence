# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-subarray-of-1s-after-deleting-one-element
# source_path: LeetCode-Solutions-master/Python/longest-subarray-of-1s-after-deleting-one-element.py
# solution_class: Solution
# submission_id: 00a025c0b7c1651042840d67672c7db915fbd746
# seed: 3908133507

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, left = 0, 0
        for right in xrange(len(nums)):
            count += (nums[right] == 0)
            if count >= 2:
                count -= (nums[left] == 0)
                left += 1
        return (right-left+1)-1
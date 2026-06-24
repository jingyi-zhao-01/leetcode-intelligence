# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-subarray-of-1s-after-deleting-one-element
# source_path: LeetCode-Solutions-master/Python/longest-subarray-of-1s-after-deleting-one-element.py
# solution_class: Solution2
# submission_id: eb92d984ed571ca8f502556f122deba60cc7b69f
# seed: 3804843966

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, count, left = 0, 0, 0
        for right in xrange(len(nums)):
            count += (nums[right] == 0)
            while count >= 2:
                count -= (nums[left] == 0)
                left += 1
            result = max(result, right-left+1)
        return result-1
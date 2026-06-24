# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-subarrays-with-score-less-than-k
# source_path: LeetCode-Solutions-master/Python/count-subarrays-with-score-less-than-k.py
# solution_class: Solution
# submission_id: f11f29f22ba9a6bba8564b5ca90938789c8c1996
# seed: 2184831409

# Time:  O(n)
# Space: O(1)

# sliding window, two pointers

class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = total = left = 0
        for right in xrange(len(nums)):
            total += nums[right]
            while total*(right-left+1) >= k:
                total -= nums[left]
                left += 1
            result += right-left+1
        return result
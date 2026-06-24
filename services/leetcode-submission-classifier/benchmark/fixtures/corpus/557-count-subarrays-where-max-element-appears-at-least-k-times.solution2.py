# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-subarrays-where-max-element-appears-at-least-k-times
# source_path: LeetCode-Solutions-master/Python/count-subarrays-where-max-element-appears-at-least-k-times.py
# solution_class: Solution2
# submission_id: c8ab8690cb5bf4b389971c77c17a0c66a5c7d227
# seed: 253494583

# Time:  O(n)
# Space: O(1)

# two pointers, sliding window

class Solution2(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mx = max(nums)
        result = (len(nums)+1)*len(nums)//2
        left = cnt = 0
        for right in xrange(len(nums)):
            cnt += int(nums[right] == mx)
            while cnt == k:
                cnt -= int(nums[left] == mx)
                left += 1
            result -= right-left+1
        return result
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: continuous-subarrays
# source_path: LeetCode-Solutions-master/Python/continuous-subarrays.py
# solution_class: Solution
# submission_id: bbd1ed2e12d34ca601d027acf1aea9a2125b1a72
# seed: 596094503

# Time:  O(n)
# Space: O(1)

import collections


# two pointers

class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = left = 0
        mn, mx = float("inf"), float("-inf")
        for right in xrange(len(nums)):
            if mn <= nums[right] <= mx:
                mn, mx = max(mn, nums[right]-2), min(mx, nums[right]+2)
            else:
                mn, mx = nums[right]-2, nums[right]+2
                for left in reversed(xrange(right)):
                    if not mn <= nums[left] <= mx:
                        break
                    mn, mx = max(mn, nums[left]-2), min(mx, nums[left]+2)
                else:
                    left = -1
                left += 1
            result += right-left+1
        return result
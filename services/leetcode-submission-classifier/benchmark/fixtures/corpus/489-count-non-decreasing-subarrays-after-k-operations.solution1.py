# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-non-decreasing-subarrays-after-k-operations
# source_path: LeetCode-Solutions-master/Python/count-non-decreasing-subarrays-after-k-operations.py
# solution_class: Solution
# submission_id: 7d363b1e5ea2d3796278cb0aaedd88fbf792b8d9
# seed: 517144614

# Time:  O(n)
# Space: O(n)

import collections


# mono deque, two pointers, sliding window

class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = cnt = 0
        dq = collections.deque()
        right = len(nums)-1
        for left in reversed(xrange(len(nums))):
            while dq and nums[dq[-1]] < nums[left]:
                l = dq.pop()
                r = dq[-1]-1 if dq else right
                cnt += (r-l+1)*(nums[left]-nums[l])
            dq.append(left)
            while cnt > k:
                cnt -= nums[dq[0]]-nums[right]
                if dq[0] == right:
                    dq.popleft()
                right -= 1
            result += right-left+1
        return result
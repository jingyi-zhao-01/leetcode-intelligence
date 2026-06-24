# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: continuous-subarrays
# source_path: LeetCode-Solutions-master/Python/continuous-subarrays.py
# solution_class: Solution2
# submission_id: 5eb7a624abfd4b934949bebd319acb262533b50b
# seed: 2851011189

# Time:  O(n)
# Space: O(1)

import collections


# two pointers

class Solution2(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn, mx = collections.deque(), collections.deque()
        result = left = 0
        for right in xrange(len(nums)):
            while mn and nums[mn[-1]] > nums[right]:
                mn.pop()
            mn.append(right)
            while mx and nums[mx[-1]] < nums[right]:
                mx.pop()
            mx.append(right)
            while not nums[right]-nums[mn[0]] <= 2:
                left = max(left, mn.popleft()+1)
            while not nums[mx[0]]-nums[right] <= 2:
                left = max(left, mx.popleft()+1)
            result += right-left+1
        return result
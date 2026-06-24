# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sliding-window-maximum
# source_path: LeetCode-Solutions-master/Python/sliding-window-maximum.py
# solution_class: Solution
# submission_id: 9e0c0182c8ba9c0033b40168b56b3a88cbe3b17a
# seed: 913658367

# Time:  O(n)
# Space: O(k)

from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result, dq = [], deque()
        for i in xrange(len(nums)):
            if dq and i-dq[0] == k:
                dq.popleft()
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k-1:
                result.append(nums[dq[0]])
        return result
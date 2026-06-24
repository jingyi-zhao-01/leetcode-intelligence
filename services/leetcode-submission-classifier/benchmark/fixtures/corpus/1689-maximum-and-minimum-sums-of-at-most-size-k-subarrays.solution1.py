# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-and-minimum-sums-of-at-most-size-k-subarrays
# source_path: LeetCode-Solutions-master/Python/maximum-and-minimum-sums-of-at-most-size-k-subarrays.py
# solution_class: Solution
# submission_id: e1ea54e7a60dceda502ff17e11bf4bf8f99a6ded
# seed: 497318171

# Time:  O(n)
# Space: O(k)

import collections


# two pointers, sliding window, mono deque

class Solution(object):
    def minMaxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def count(check):
            result = total = 0
            dq = collections.deque()
            for right in xrange(len(nums)):
                while dq and not check(nums[dq[-1]], nums[right]):
                    i = dq.pop()
                    cnt = i-(dq[-1]+1 if dq else max(right-k+1, 0))+1
                    total -= cnt*nums[i]
                cnt = right-(dq[-1]+1 if dq else max(right-k+1, 0))+1
                dq.append(right)
                total += cnt*nums[right]
                result += total
                if right-(k-1) >= 0:
                    total -= nums[dq[0]]
                    if dq[0] == right-(k-1):
                        dq.popleft()
            return result
    
        return count(lambda a, b: a < b)+count(lambda a, b: a > b)
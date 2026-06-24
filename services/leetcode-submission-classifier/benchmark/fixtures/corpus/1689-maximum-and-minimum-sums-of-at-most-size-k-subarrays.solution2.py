# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-and-minimum-sums-of-at-most-size-k-subarrays
# source_path: LeetCode-Solutions-master/Python/maximum-and-minimum-sums-of-at-most-size-k-subarrays.py
# solution_class: Solution2
# submission_id: b02879883b48d9c44a280a2c24fdba75d41b5457
# seed: 330149942

# Time:  O(n)
# Space: O(k)

import collections


# two pointers, sliding window, mono deque

class Solution2(object):
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
                left = right
                while dq and not check(nums[dq[-1][0]], nums[right]):
                    i, left = dq.pop()
                    total -= (i-left+1)*nums[i]
                dq.append([right, left])
                total += (right-left+1)*nums[right]
                result += total
                if right-(k-1) >= 0:
                    total -= nums[dq[0][0]]
                    if dq[0][0] == right-(k-1):
                        dq.popleft()
                    else:
                        assert(dq[0][1] == right-(k-1))
                        dq[0][1] += 1
            return result
    
        return count(lambda a, b: a < b)+count(lambda a, b: a > b)
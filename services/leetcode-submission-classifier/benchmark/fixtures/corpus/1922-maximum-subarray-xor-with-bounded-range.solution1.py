# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-subarray-xor-with-bounded-range
# source_path: LeetCode-Solutions-master/Python/maximum-subarray-xor-with-bounded-range.py
# solution_class: Solution
# submission_id: c3722f105ec5139a7c88bbfa7c0288d022d0c40b
# seed: 1240191468

# Time:  O(nlogr), r = max(max(nums), 1)
# Space: O(n)

import collections


# two pointers, mono deque, bitmasks, prefix sum, hash table

class Solution(object):
    def maxXor(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lookup = [-1]*len(nums)
        max_dq = collections.deque()
        min_dq = collections.deque()
        left = 0
        for right in xrange(len(nums)):
            while max_dq and nums[max_dq[-1]] <= nums[right]:
                max_dq.pop()
            max_dq.append(right)
            while min_dq and nums[min_dq[-1]] >= nums[right]:
                min_dq.pop()
            min_dq.append(right)
            while nums[max_dq[0]]-nums[min_dq[0]] > k:
                if max_dq and max_dq[0] == left:
                    max_dq.popleft()
                if min_dq and min_dq[0] == left:
                    min_dq.popleft()
                left += 1
            lookup[right] = left
        result = 0
        mx = max(max(nums), 1)
        for i in reversed(xrange(mx.bit_length())):
            lookup2 = collections.defaultdict(int)
            lookup2[0] = prefix = 0
            for right in xrange(len(nums)):
                prefix ^= nums[right]>>i
                if ((result>>i)|1)^prefix in lookup2 and lookup2[((result>>i)|1)^prefix] >= lookup[right]:
                    result |= 1<<i
                    break
                lookup2[prefix] = right+1
        return result
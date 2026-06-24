# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: top-k-frequent-words
# source_path: LeetCode-Solutions-master/Python/top-k-frequent-words.py
# solution_class: Solution
# submission_id: a986765f5fed47a496a230cc1fd47ead07139adf
# seed: 874308619

# Time:  O(n + klogk) on average
# Space: O(n)

import collections
import heapq
from random import randint

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = collections.Counter(words)
        p = []
        for key, val in counts.iteritems():
            p.append((-val, key))
        self.kthElement(p, k-1)

        result = []
        sorted_p = sorted(p[:k])
        for i in xrange(k):
            result.append(sorted_p[i][1])
        return result

    def kthElement(self, nums, k):  # O(n) on average
        def PartitionAroundPivot(left, right, pivot_idx, nums):
            pivot_value = nums[pivot_idx]
            new_pivot_idx = left
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            for i in xrange(left, right):
                if nums[i] < pivot_value:
                    nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                    new_pivot_idx += 1

            nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
            return new_pivot_idx

        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_idx = randint(left, right)
            new_pivot_idx = PartitionAroundPivot(left, right, pivot_idx, nums)
            if new_pivot_idx == k:
                return
            elif new_pivot_idx > k:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k.
                left = new_pivot_idx + 1
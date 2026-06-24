# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: top-k-frequent-elements
# source_path: LeetCode-Solutions-master/Python/top-k-frequent-elements.py
# solution_class: Solution2
# submission_id: 2b778632740f2a66b38d0dab144c9dac6f723a56
# seed: 2236483784

# Time:  O(n)
# Space: O(n)

import collections

class Solution2(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = collections.Counter(nums)
        p = []
        for key, val in counts.iteritems():
            p.append((-val, key))
        self.kthElement(p, k-1)

        result = []
        for i in xrange(k):
            result.append(p[i][1])
        return result

    def kthElement(self, nums, k):
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
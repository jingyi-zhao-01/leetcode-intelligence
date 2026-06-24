# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: intersection-of-two-arrays-ii
# source_path: LeetCode-Solutions-master/Python/intersection-of-two-arrays-ii.py
# solution_class: Solution
# submission_id: 27e59e21b46da94bab0e83225e300fd8b4240794
# seed: 4011859316

# If the given array is not sorted and the memory is unlimited:
#   - Time:  O(m + n)
#   - Space: O(min(m, n))
# elif the given array is already sorted:
#   if m << n or m >> n:
#     - Time:  O(min(m, n) * log(max(m, n)))
#     - Space: O(1)
#   else:
#     - Time:  O(m + n)
#     - Soace: O(1)
# else: (the given array is not sorted and the memory is limited)
#     - Time:  O(max(m, n) * log(max(m, n)))
#     - Space: O(1)

import collections

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        def binary_search(compare, nums, left, right, target):
            while left < right:
                mid = left + (right - left) / 2
                if compare(nums[mid], target):
                    right = mid
                else:
                    left = mid + 1
            return left

        nums1.sort(), nums2.sort()  # Make sure it is sorted, doesn't count in time.

        res = []
        left = 0
        for i in nums1:
            left = binary_search(lambda x, y: x >= y, nums2, left, len(nums2), i)
            if left != len(nums2) and nums2[left] == i:
                res += i,
                left += 1

        return res
# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: intersection-of-two-arrays
# source_path: LeetCode-Solutions-master/Python/intersection-of-two-arrays.py
# solution_class: Solution2
# submission_id: 6195f1481e6641f4f3ad9f77b8dcb29b277e199f
# seed: 663350269

# Time:  O(m + n)
# Space: O(min(m, n))

class Solution2(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)

        def binary_search(compare, nums, left, right, target):
            while left < right:
                mid = left + (right - left) / 2
                if compare(nums[mid], target):
                    right = mid
                else:
                    left = mid + 1
            return left

        nums1.sort(), nums2.sort()

        res = []
        left = 0
        for i in nums1:
            left = binary_search(lambda x, y: x >= y, nums2, left, len(nums2), i)
            if left != len(nums2) and nums2[left] == i:
                res += i,
                left = binary_search(lambda x, y: x > y, nums2, left, len(nums2), i)

        return res
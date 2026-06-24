# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-pairs-satisfying-inequality
# source_path: LeetCode-Solutions-master/Python/number-of-pairs-satisfying-inequality.py
# solution_class: Solution3
# submission_id: d592cd3d665612d03ae2b7ed8d3980f6e8a11339
# seed: 3151068140

# Time:  O(nlogn)
# Space: O(n)

from sortedcontainers import SortedList
import itertools


# sorted list, binary search

class Solution3(object):
    def numberOfPairs(self, nums1, nums2, diff):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type diff: int
        :rtype: int
        """
        def merge_sort(nums, left, right, result):
            if left == right:
                return
            mid = left+(right-left)//2
            merge_sort(nums, left, mid, result)
            merge_sort(nums, mid+1, right, result)
            r = mid+1
            for l in xrange(left, mid+1):
                while r < right+1 and nums[l]-nums[r] > diff:
                    r += 1
                result[0] += right-r+1
            tmp = []
            l, r = left, mid+1
            while l < mid+1 or r < right+1:
                if r >= right+1 or (l < mid+1 and nums[l] <= nums[r]):
                    tmp.append(nums[l])
                    l += 1
                else:
                    tmp.append(nums[r])
                    r += 1
            nums[left:right+1] = tmp

        nums = [x-y for x, y in itertools.izip(nums1, nums2)]
        result = [0]
        merge_sort(nums, 0, len(nums)-1, result)
        return result[0]